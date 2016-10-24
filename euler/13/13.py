f = open('numbers.txt')

sum = 0
for line in f:
	sum += int(line[0:12])

f.close()

print sum
