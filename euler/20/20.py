import math

def sum_digits_k_factorial(k):
	factorial_string = str(math.factorial(k))
	factorial_digits = [int(i) for i in factorial_string]
	return sum(factorial_digits)
