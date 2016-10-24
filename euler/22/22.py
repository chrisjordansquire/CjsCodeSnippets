
def name_score(name):
	score = 0
	for char in name:
		score += 1 + ord(char) - ord('A')
	return score


def solve_22():
	f = open('names.txt')
	list_names_unprocessed = next(f).split(',')
	f.close()

	list_names = [s.strip('"') for s in list_names_unprocessed]
	name_scores = [(i+1)*name_score(name) for i,name in enumerate(list_names)]
	total_sum = sum(name_scores)
	return total_sum

