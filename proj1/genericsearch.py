import sys

def generic_search(graph, start_node, goal, initparents, initcosts, initfringe,
		remove, expand, isgoal, path):

	#initialise the fringe
	fringe = initfringe(start_node)
	parents = initparents(graph)
	known_costs = initcosts(graph, fringe)

	while fringe:
		curr = remove(fringe)

		print(curr.id_)

		if isgoal(curr, goal):
			return path(start_node, goal, parents)
		expand(curr, fringe, parents, known_costs)

	# no path found
	return []

