import sys

def generic_search(graph, start_node, goal, initparents, initcosts, initfringe,
		remove, expand, isgoal, path):

	# initialise the fringe
	fringe = initfringe(start_node)
	# for each node there should be no parents
	parents = initparents(graph)
	# known costs should be infinite
	known_costs = initcosts(graph, fringe)

	while fringe:
		curr = remove(fringe)

		#print(curr.id_)
		#print("path", path(start_node, curr, parents))

		if isgoal(curr, goal):
			return path(start_node, goal, parents, known_costs)
		expand(curr, fringe, parents, known_costs)

	# no path found
	return []

