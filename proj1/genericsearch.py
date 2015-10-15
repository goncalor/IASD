import sys

def generic_search(graph, start_node, goal):

	fringe = [(0, start_node)]
	parent = [(None, None) for i in range(len(graph))]
	known_cost = [sys.maxsize for i in range(len(graph))]

	known_cost[start_node.id_] = 0	# reaching the start node costs nothing

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

		# the cost of the neighbour is this curr's cost plus the edge cost
		neigh_known_cost = known_cost[neigh.id_] + edge.info.price
		#heur = heuristic(relaxed_graph, neigh, goal)
		heur = 0

		# if a new best path was found to neigh
		if known_cost[neigh.id_] > neigh_known_cost + heur:
			# update the cost to reach neigh
			known_cost[neigh.id_] = neigh_known_cost
			# add neigh to the fringe
			fringe.append((neigh_known_cost + heur, neigh))
			# update neigh's parent
			parent[neigh.id_] = (curr.id_, edge.info.transType)

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

