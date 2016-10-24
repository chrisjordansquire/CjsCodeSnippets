import itertools

def solve_29(a,b):
	product_list = itertools.product(range(2,a+1), range(2,b+1))
	list_all_num = [i**j for i,j in product_list]
	return len(set(list_all_num))

