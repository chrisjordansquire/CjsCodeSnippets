import operator 

upper = 1000
p_trip = None  

for i in xrange(upper):
	for j in xrange(1,i):
		if(i**2+j**2 == (1000-i-j)**2):
			p_trip = (i,j,1000-i-j)
print p_trip
print reduce(operator.mul, p_trip)
