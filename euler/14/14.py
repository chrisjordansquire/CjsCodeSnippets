
N = 10**6

def nextTerm(n):
	if 0 == n%2:
		return n/2
	else:
		return 3*n+1

lengths = [0]*N
lengths[1] = 1

for i in xrange(2,N):
	if lengths[i] != 0:
		pass
	collatzSeq = []
	term = i
	while(term>i-1):
		collatzSeq.append(term)
		term = nextTerm(term)
	
	count = lengths[term]+1
	while collatzSeq:
		lastSeen = collatzSeq.pop()
		if(lastSeen<N):
			lengths[lastSeen] = count
		count += 1


print lengths.index(max(lengths))


