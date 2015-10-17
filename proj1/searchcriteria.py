
class SearchCriteria:

	def __init__(self, client):
		#self.remove = self.remove
		#self.expand = self.expand
		#self.isgoal = self.isgoal
		#self.path = self.path
		pass


	def path(self, start, goal, parents):
		path = []
		node = goal.id_

		while node != start.id_:
			path.append(parents[node])
			node = parents[node][0]
		return path + [(start.id_, None)]


	def expand(self, curr, fringe, parents, known_costs):
		""" Expands the nodes that are neighbours of 'curr.' """
		for edge in curr.neigh:
			neigh = edge.neighbour(curr)

			# the cost of the neighbour is this curr's cost plus the edge cost
			neigh_known_cost = known_costs[curr.id_] + edge.info.price
			#heur = heuristic(relaxed_graph, neigh, goal)
			heur = 0

			# if a new best path was found to neigh
			if known_costs[neigh.id_] > neigh_known_cost + heur:
				# update the cost to reach neigh
				known_costs[neigh.id_] = neigh_known_cost
				# add neigh to the fringe
				fringe.append((neigh_known_cost + heur, neigh))
				# update neigh's parent
				parents[neigh.id_] = (curr.id_, edge.info.transType)

		# "Sorts are guaranteed to be stable."
		fringe.sort(key=lambda tup: tup[0], reverse=True)

		print([(item[1].id_, item[0]) for item in fringe])
		

	def isgoal(self, node, goal):
		if node == goal:
			return True
		return False


	def remove(self, fringe):
		""" Returns only the node from the (f, node) tuple """
		return fringe.pop()[1]

