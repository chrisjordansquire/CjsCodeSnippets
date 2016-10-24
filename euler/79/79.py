
def solve_79():

	attempts = []
	with open('keylog.txt') as f:
		for line in f:
			attempts.append([int(i) for i in line.strip()])
	
	nodes = {}

	for line in attempts:
		for node in line:
			if node not in nodes:
				nodes[node] = set([])
		nodes[line[1]].add(line[0])
		nodes[line[2]].add(line[0])
		nodes[line[2]].add(line[1])
	
	#Do a topological sort on the nodes + inodes
	S = []

	for key in nodes.keys():
		if not nodes[key]:
			nodes.pop(key)
			S.append(key)

	out = []

	while S:
		popped_node = S.pop()
		out.append(popped_node)
		for key in nodes.keys():
			nodes[key].remove(popped_node)
			if not nodes[key]:
				nodes.pop(key)
				S.append(key)

	return ''.join([str(i) for i in out])
