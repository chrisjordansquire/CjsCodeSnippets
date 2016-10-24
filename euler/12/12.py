import numpy as np


def num_factors_from_p_powers(p_powers):
	p_powers = np.array(p_powers)
	p_powers[0] += 1
	for i in range(1,len(p_powers)):
		p_powers[i] = np.sum(p_powers[0:i]) * p_powers[i]
	return np.sum(p_powers)

def num_factors(n):
	if n==1:
		return 1
	factors = {}
	i = 1
	while n != 1:
		i += 1
		if n % i == 0:
			count = 0
			while n % i == 0:
				count += 1
				n = n/i
			factors[i] = count
	return num_factors_from_p_powers(factors.values())


def solve_eu12(k):
	greater_than_k_factors = False
	
	i = 1
	triangle_number = 0

	while not greater_than_k_factors:
		triangle_number += i
		i += 1

		n = num_factors(triangle_number)
		greater_than_k_factors = n > k

	return i-1,triangle_number, n




