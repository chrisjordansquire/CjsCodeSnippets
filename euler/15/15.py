
def n_paths(n_blocks):

	n_nodes = n_blocks + 1
	n_paths_list = []
	for i in range(n_nodes):
		n_paths_list.append([0]*n_nodes)
	
	for i in range(n_nodes):
		for j in range(n_nodes):
			if j==0 or i==0:
				n_paths_list[i][j] = 1
			else:
				n_paths_list[i][j] += n_paths_list[i-1][j]
				n_paths_list[i][j] += n_paths_list[i][j-1]
	return n_paths_list[n_blocks][n_blocks]
