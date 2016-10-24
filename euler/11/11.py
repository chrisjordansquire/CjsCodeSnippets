from operator import mul

f = open('array.txt')

arr = [[int(i) for i in l.split()] for l in f]

f.close()

arrt = [[l[i] for l in arr] for i in range(20)]

arrd = [[arr[i][i+c] for i in range(20) if (i+c<20 and i+c>=0)]
		for c in range(-19,20)]

arrdOpp = [[arr[i][c-i] for i in range(20) if (c-i<20 and c-i>=0)]
		for c in range(39)]

def prod4(l):
	n = len(l)
	if n<4:
		return []
	else:
		return [reduce(mul,l[i:i+4]) for i in range(n-3)] 

comb = []
comb.extend(arr)
comb.extend(arrt)
comb.extend(arrd)
comb.extend(arrdOpp)

out = [prod4(l) for l in comb]

print max([max(l) for l in out if len(l)>0])
