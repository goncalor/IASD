import sys

def generic_search(graph, start_node, goal, remove, expand, isgoal, path):

	fringe = [(0, start_node)]
	# save the node id and the transportation type
	parents = [(None, None) for i in range(len(graph))]
	known_costs = [sys.maxsize for i in range(len(graph))]

	known_costs[start_node.id_] = 0	# reaching the start node costs nothing

	while fringe:
		curr = remove(fringe)

		print(curr.id_)

		if isgoal(curr, goal):
			return path(start_node, goal, parents)
		expand(curr, fringe, parents, known_costs)

	# no path found
	return []

