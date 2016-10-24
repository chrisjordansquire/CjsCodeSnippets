import numpy as np
import itertools 

# Write this as an exercise for myself.
# It is shockingly and embarrassingly slow compared to Norvig's
# code in ihttp://norvig.com/sudoku.html.

class sudoku:

    def __init__(self, d, sqrtN=2):
        """
        sqrtN: the size of the sub-matrices
        In typial sudoku sqrtN=3.
        """
        sqrtN2 = (sqrtN, sqrtN)
        N = sqrtN**2
        N2 = (N,N)
        self.grid = np.zeros(N2, dtype='object')
        self.csets = []
        self.count = itertools.count()
        #columns all different
        for i in range(N):
            self.csets.append([(i, k) for k in range(N)])

        #rows all different
        for j in range(N):
            self.csets.append([(k, j) for k in range(N)])

        #sub-matrixes all different
        arr_sqrtN2 = np.zeros(sqrtN2)
        for (i,j),_ in np.ndenumerate(arr_sqrtN2):
            self.csets.append([(i1+sqrtN*i, j1+sqrtN*j) for (i1, j1),_ 
                               in np.ndenumerate(arr_sqrtN2)])

        #initialize grid
        arr_N2 = np.zeros(N2)
        for idx,_ in np.ndenumerate(arr_N2):
            self.grid[idx] = {i:set() for i in range(1, N+1)} 

        self.assumed = []
        self.toAssume = []
        for idx in d:
            self.assume(idx, d[idx])

    def assume(self, idx, value):
        id =next(self.count)
        self.assumed.append([idx, value, id, 0])
        self._set(idx, value, id)
        
        assume_queue = [(idx, value)]

        itr = 0
        while itr < len(assume_queue):
            prop_idx, prop_value = assume_queue[itr]
            for cset in self.csets:
                if prop_idx in cset:
                    for cset_idx in cset:
                        if prop_idx != cset_idx:
                            self._ban(cset_idx, prop_value, id)
                            self._isNewConstant(cset_idx, assume_queue, id)
            itr = itr+1
            if itr>90:
                raise Exception("foo")
          
    def _isNewConstant(self, idx, assume_queue, id):
        idx_dict = self.grid[idx]
        allowed_values = map(lambda x : len(x)==0, idx_dict.itervalues())
        if sum(allowed_values)==1:
            #Test being constant is result of new constraint
            if set([id]) in idx_dict.itervalues():
                value_idx = allowed_values.index(True)
                value = idx_dict.keys()[value_idx]
                if [idx, value] not in assume_queue:
                    assume_queue.append([idx, value])

    def _ban(self, idx, value, id):
        idx_dict = self.grid[idx]
        idx_dict[value].add(id)

    def _set(self, idx, value, id):
        idx_dict = self.grid[idx]

        for digit in idx_dict:
            if digit != value:
                idx_dict[digit].add(id)

    def unassume(self):
        idx, val, id, _= self.assumed.pop()
        self.assumed[-1][-1] += 1
        for idx_dict in self.grid.flat:
            for vset in idx_dict.itervalues():
                if id in vset: 
                    vset.remove(id)

    def solve(self):
        while not self.solved():
            if self.feasible():
                idx = self.nextNode()
                if idx:
                    self.toAssume.append("unassume")
                    for value, allowed in self.grid[idx].iteritems():
                        if len(allowed)==0:
                            self.toAssume.append([idx, value])
            else:
                self.unassume()
        
            arg = self.toAssume.pop()
            if arg == "unassume":
                while arg == "unassume":
                    self.unassume()
                    arg = self.toAssume.pop()
            self.assume(*arg)

    def currentGrid(self):

        x = np.zeros(self.grid.shape)
        sizes = self.gridStateSizes()
        for idx, valueDict in np.ndenumerate(self.grid):
            if sizes[idx] == 1:
                for key in valueDict:
                    if len(valueDict[key]) == 0:
                        x[idx] = key
            if sizes[idx] == 0:
                x[idx] = -1
        return x

    def feasible(self):
        sizes = self.gridStateSizes()
        return np.all(sizes>0)

    def solved(self):
        sizes = self.gridStateSizes()
        return np.all(sizes==1)

    def nextNode(self):
        sizes = self.gridStateSizes()
        sizes = filter(lambda x : x[1]>1, np.ndenumerate(sizes))
        sizes = sorted(sizes, key=lambda x:x[1])
        nodeCounter = self.assumed[-1][-1]
        if nodeCounter < len(sizes):
            node = sizes[nodeCounter][0]
        else:
            node = None
        return node

    def gridStateSizes(self):
        return alen(self.grid)


alen = np.vectorize(lambda x: sum(1 for v in x.itervalues() if len(v)==0))                    

def stateSize(s):
    lenArr = alen(s.base)
    lenArr = [int(i) for i in lenArr.flat]
    return 

norvig_dict = {(0,0):4, (1,1):3, (2,3):7, (0,6):8, 
               (0,8):5, (3, 1):2, (3,6):6, (4,4):8,
               (4,6):4, (5,4):1, (6,3):6, (6,5):3,
               (6,7):7, (7,0):5, (7,3):2, (8,0):2, (8,2):4}

def main():
    b = sudoku({(0,0): 4})
    b.propConstants

if __name__ == "_main__":
    main()
