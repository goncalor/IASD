import sys

class SearchCriteria:

	def __init__(self, client):

		# define how the cost to reach the next node is calculated
		if client['criterion'] == 'tempo':
			self.edgecost = self.__time_edgecost
		elif client['criterion'] == 'custo':
			self.edgecost = self.__price_edgecost

		#self.remove = self.remove
		#self.expand = self.expand
		#self.isgoal = self.isgoal
		#self.path = self.path


	def __time_edgecost(self, edge):

		#TODO complete this!
		return edge.info.duration


	def __price_edgecost(self, edge):
		return edge.info.price


	def initfringe(self, start_node):
		return [(0, start_node)]


	def initparents(self, graph):
		# save the node id and the transportation type
		return [(None, None) for i in range(len(graph))]


	def initcosts(self, graph, fringe):
		known_costs = [sys.maxsize for i in range(len(graph))]
		for f, node in fringe:
			known_costs[node.id_] = 0	# reaching the start nodes costs nothing
		return known_costs


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
			neigh_known_cost = known_costs[curr.id_] + self.edgecost(edge)
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

