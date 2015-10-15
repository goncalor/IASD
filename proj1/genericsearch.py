

def generic_search(graph, start_nodes, goal):

	fringe = list(start_nodes)
	curr = None

	while fringe:
		curr = remove(fringe)
		if isgoal(curr):
			return "found you"
		expand(fringe, curr)

	return "cannot find goal"

