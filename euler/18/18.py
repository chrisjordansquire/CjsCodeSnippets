
def solve_18(file_name):
	f = open(file_name)
	triangle = []
	for line in f:
		triangle.append([int(s) for s in line.split(' ')])
	f.close()


	best_paths = []

	for row in triangle:
		if not best_paths:
			best_paths.append([(row[0], None)])
		else:
			best_paths.append([])
			for i,value in enumerate(row):
				n = len(row)
				if i == 0:
					prev = best_paths[-2][0][0]
					best_paths[-1].append((value+prev, 0))
				elif i == n-1:
					prev = best_paths[-2][i-1][0]
					best_paths[-1].append((value+prev,i-1))
				else:
					path1 = best_paths[-2][i-1][0] + value
					path2 = best_paths[-2][i][0] + value
					if path1 > path2:
						best_paths[-1].append((path1, i-1))
					else:
						best_paths[-1].append((path2, i))

	max_val = float('-Inf')
	idx = 0
	for i, tup in enumerate(best_paths[-1]):
		if tup[0] > max_val:
			max_val = tup[0]
			prev = i

	path = [prev]
	i = -1
	while prev is not None:
		prev  = best_paths[i][prev][1]
		i -= 1
		path.append(prev)
	path.pop()
	path.reverse()

	return max_val, path







