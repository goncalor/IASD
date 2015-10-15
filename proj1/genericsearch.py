import sys

def generic_search(graph, start_node, goal):

	fringe = [(0, start_node)]

	#make this general
	for node in graph.nodes:
		node.info = sys.maxsize
	start_node.info = 0

	while fringe:
		curr = remove(fringe)

		print(curr.id_)

		if isgoal(curr, goal):
			return "found you"
		expand(fringe, curr)

	return "cannot find goal"


def expand(fringe, curr):

	for edge in curr.neigh:
		neigh = edge.neighbour(curr)

		neigh_known_cost = curr.info + edge.info.price
		#heur = heuristic(relaxed_graph, neigh, goal)
		heur = 0

		if neigh.info > neigh_known_cost + heur:
			neigh.info = neigh_known_cost
			fringe.append((neigh_known_cost + heur, neigh))

	# "Sorts are guaranteed to be stable."
	fringe.sort(key=lambda tup: tup[0], reverse=True)

	print([(item[1].id_, item[0]) for item in fringe])
	

def isgoal(node, goal):
	if node == goal:
		return True
	return False


def remove(fringe):
	""" Returns only the node from the (f, node) tuple """
	return fringe.pop()[1]

