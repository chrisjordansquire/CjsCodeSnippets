import numpy as np
import cvxopt
import collections
import random

# Used to benchmark a few different approximation algorithms for set cover
# problems using set cover examples from the OR-Library: 
# http://people.brunel.ac.uk/~mastjjb/jeb/orlib/scpinfo.html

class SetCoverProblem:

    def __init__(self, number_elements, number_sets, sets,
                 elements_to_sets, costs):
        assert(len(sets) == len(costs) == number_sets)
        self.number_elements = number_elements
        self.number_sets = number_sets
        self.sets = sets
        self.elements_to_sets = elements_to_sets
        self.costs = costs

    def cover_cost(self, cover):
        return sum([self.costs[i] for i in cover])

    def is_cover(self, set_indices):
        uncovered = set(range(self.number_elements))
        for idx in set_indices:
            uncovered = uncovered.difference(set(self.sets[idx]))
        return len(uncovered) == 0

    def redundant_sets_from_cover(self, cover):
        number_times_covered = collections.defaultdict(lambda: 0)
        for idx in cover:
            for element in self.sets[idx]:
                number_times_covered[element] += 1
        redundant_sets = []
        for idx in cover:
            if all(number_times_covered[element] > 2 for element in self.sets[idx]):
                redundant_sets.append(idx)
        return redundant_sets


def read_or_lib_example(filename):
    with open(filename) as f:
        file_contents_str = f.read()
    file_contents_int = [int(n) for n in file_contents_str.split()]
    rows = file_contents_int[0]
    columns = file_contents_int[1]
    costs = file_contents_int[2:columns+2]
    sets = [[] for i in range(columns)]
    elements_to_sets = []
    index = columns+2
    element = 0
    while index < len(file_contents_int):
        set_size = file_contents_int[index]
        for set_index in file_contents_int[index+1:index+1+set_size]:
            sets[set_index-1].append(element)
        elements_to_sets.append([i-1 for i in
                                 file_contents_int[index+1:index+1+set_size]])
        index += set_size + 1
        element += 1

    return SetCoverProblem(rows, columns, sets, elements_to_sets, costs)


def greedy_solution(set_cover: SetCoverProblem):
    def price_sets(set_cover, covered, chosen_sets):
        prices = []
        for index, _set in enumerate(set_cover.sets):
            cost = set_cover.costs[index]
            newly_covered = len(set(_set).difference(covered))
            if newly_covered > 0:
                price = cost / newly_covered
                prices.append((index, price))
        return prices

    covered = set()
    chosen_sets = []
    while len(covered) != set_cover.number_elements:
        prices = price_sets(set_cover, covered, chosen_sets)
        chosen_set = min(prices, key=lambda s: s[1])
        chosen_sets.append(chosen_set[0])
        covered = covered.union(set_cover.sets[chosen_set[0]])

    return chosen_sets


def fractional_rounding_solution(set_cover: SetCoverProblem):
    costs = cvxopt.matrix(set_cover.costs, tc='d')
    h = cvxopt.matrix(([0] * set_cover.number_sets) +
                      ([-1] * set_cover.number_elements), tc='d')
    Gvalues = [-1] * set_cover.number_sets
    GrowIndices = list(range(set_cover.number_sets))
    GcolumnIndices = list(range(set_cover.number_sets))
    for idx, set_ in enumerate(set_cover.sets):
        Gvalues.extend([-1] * len(set_))
        for element in set_:
            GrowIndices.append(set_cover.number_sets + element)
            GcolumnIndices.append(idx)
    G = cvxopt.spmatrix(Gvalues, GrowIndices, GcolumnIndices, tc='d')
    solution_dict = cvxopt.solvers.lp(costs, G, h)
    cutoff = max(map(len, set_cover.elements_to_sets))
    print("cutoff is ", cutoff)
    test_cutoff = 1
    is_cover = False
    while not is_cover:
        test_cutoff += 0.1
        chosen_sets = set(
                np.where(np.array(solution_dict['x']).flatten() > 1 / test_cutoff)[0]
        )
        is_cover = set_cover.is_cover(chosen_sets)
    print("needed cutoff is: ", test_cutoff)
    return chosen_sets


def primal_dual_solution(set_cover: SetCoverProblem):
    covered = set()
    uncovered = set(range(set_cover.number_elements))
    chosen_sets = []
    dual_slack = np.array(set_cover.costs, dtype='int64')
    while len(covered) != set_cover.number_elements:
        chosen_element = random.sample(uncovered, 1)[0]
        element_dual_slack_indices = set_cover.elements_to_sets[chosen_element]
        element_dual_slacks = dual_slack[element_dual_slack_indices]
        sets_to_add = np.array(element_dual_slack_indices)[
           np.where(element_dual_slacks == element_dual_slacks.min())
        ]
        dual_slack[element_dual_slack_indices] -= element_dual_slacks.min()
        chosen_sets.extend(sets_to_add)
        for set_idx in sets_to_add:
            covered = covered.union(set_cover.sets[set_idx])
        uncovered = uncovered.difference(covered)
    return chosen_sets


def fit_all(set_cover:SetCoverProblem=None, filename:str=None):
    if filename:
        set_cover = read_or_lib_example(filename)
    elif not set_cover:
        raise RuntimeError("Must give either filename or SetCover instance")
    print("elements: ", set_cover.number_elements)
    print("sets: ", set_cover.number_sets)
    greedy_cover = greedy_solution(set_cover)
    print("greedy is cover?: ", set_cover.is_cover(greedy_cover))
    print("greedy cost: ", set_cover.cover_cost(greedy_cover))
    fr_cover = fractional_rounding_solution(set_cover)
    print("fr is cover?: ", set_cover.is_cover(fr_cover))
    print("fr cost: ", set_cover.cover_cost(fr_cover))
    pd_cover = primal_dual_solution(set_cover)
    print("pd is cover?: ", set_cover.is_cover(pd_cover))
    print("pd cost: ", set_cover.cover_cost(pd_cover))


def randomSetCoverInstace(number_elements,
                          min_number_sets):
    sets = []
    costs = []
    elements_to_sets = [list() for i in range(number_elements)]
    set_idx = 0
    covered = set()
    while set_idx <= min_number_sets and len(covered) < number_elements:
        set_size = random.randint(1, int(number_elements/80)+1)
        s = random.sample(range(number_elements), set_size)
        sets.append(s)
        for element in s:
            elements_to_sets[element].append(set_idx)
        set_idx += 1
        costs.append(random.randint(2, min_number_sets/10))

    return SetCoverProblem(number_elements,
                           len(sets),
                           sets,
                           elements_to_sets,
                           costs)


def pathological_set_cover(number_elements, eps):
    sets = [[i] for i in range(number_elements)]
    sets.append(list(range(number_elements)))
    elements_to_sets = [[i, number_elements] for i in range(number_elements)]
    costs = [1/(number_elements-i) for i in range(number_elements)]
    costs.append(1+eps)

    return SetCoverProblem(number_elements,
                           len(sets),
                           sets,
                           elements_to_sets,
                           costs)
