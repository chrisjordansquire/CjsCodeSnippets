
def solve_25(k):
	f_curr = 1
	f_prev = 1
	count = 2
	while len(str(f_curr)) < k:
		count += 1
		f_curr = f_curr + f_prev
		f_prev = f_curr - f_prev
	return count


