import sys

class SearchCriteria:

	def __init__(self, client, heuristic):
		self.client = client
		self.heuristic = heuristic

		# restriction is the worst value the optimization criteria can have
		if 'B1' in client:
			self.restriction = client['B1']
		elif 'B2' in client:
			self.restriction = client['B2']
		else:
			self.restriction = sys.maxsize


	def __time_edgecost(self, edge, curr_time):
		time_today = curr_time % 1440

		# normal waiting time
		# remaining time to next transport
		# 	waiting is the duration of a period minus the time of the period that has already passed
		waiting_time = edge.info.period - (time_today - edge.info.ti) % edge.info.period
		# if it is the period, it means we are right on time
		if waiting_time == edge.info.period:
			waiting_time = 0

		# 	when there are no more transports today
		if time_today + waiting_time > edge.info.tf:
			waiting_time = 1440 - time_today + edge.info.ti
		# when before first departure
		elif time_today < edge.info.ti:
			waiting_time = edge.info.ti - time_today

		"""
		# debug
		print(curr_time, "\t", edge.info.transType, edge, 'wait', waiting_time, 'time', time_today, 'period', edge.info.period)
		#
		"""

		return waiting_time + edge.info.duration


	def __price_edgecost(self, edge):
		return edge.info.price


	def initfringe(self, start_node):
		return [(0, start_node)]


	def initparents(self, graph):
		# save (node id, transportation type)
		return [(None, None) for i in range(len(graph))]


	def initcosts(self, graph, fringe):
		known_costs = [(sys.maxsize, sys.maxsize) for i in range(len(graph))]
		for f, node in fringe:
			# (duration, price)
			known_costs[node.id_] = (self.client['timeAvail'], 0)	# reaching the start nodes costs nothing
		return known_costs


	def path(self, start, goal, parents, known_costs):
		path = []
		node = goal.id_

		if parents[goal.id_][0] == None:
			return '-1'

		path.append((goal.id_, None))

		# find the start from the end to build the path
		while node != start.id_:
			# parent index and the branch used to get to it
			path.append(parents[node])

			# node now "points" to the parent
			node = parents[node][0]

		path.reverse()

		s = ''
		for item in path[:-1]:
			s += '{} {} '.format(item[0], item[1])
		else:
			s += '{} {} {}'.format(goal.id_, known_costs[goal.id_][0]-self.client['timeAvail'], known_costs[goal.id_][1])

		return s


	def expand(self, curr, fringe, parents, known_costs):
		""" Expands the nodes that are neighbours of 'curr.' """
		for edge in curr.neigh:
			neigh = edge.neighbour(curr)

			# the cost of the neighbour is this curr's cost plus the edge cost
			neigh_known_cost_duration = known_costs[curr.id_][0] + \
			self.__time_edgecost(edge, known_costs[curr.id_][0])

			neigh_known_cost_price = known_costs[curr.id_][1] + \
			self.__price_edgecost(edge)

			if self.client['criterion'] == 'tempo':
				new_neigh_known_cost = neigh_known_cost_duration
				old_neigh_known_cost = known_costs[neigh.id_][0]
			else:
				new_neigh_known_cost = neigh_known_cost_price
				old_neigh_known_cost = known_costs[neigh.id_][1]

			heur = self.heuristic(self.client['from'], self.client['to'])

			# if a new best path was found to neigh
			if old_neigh_known_cost + heur > new_neigh_known_cost + heur:
				# update the cost to reach neigh
				known_costs[neigh.id_] = (neigh_known_cost_duration,
						neigh_known_cost_price)
				# add neigh to the fringe (f, neighbour)
				fringe.append((new_neigh_known_cost + heur, neigh))
				# update neigh's parent (id, transport type)
				parents[neigh.id_] = (curr.id_, edge.info.transType)

		if not fringe:
			return

		# "Sorts are guaranteed to be stable."
		fringe.sort(key=lambda tup: tup[0], reverse=True)

		if self.client['criterion'] == 'tempo':
			if known_costs[fringe[-1][1].id_][0] > self.restriction:
				del fringe[:]
		else:
			if known_costs[fringe[-1][1].id_][1] > self.restriction:
				del fringe[:]

		# (id, cost)
		#print("expanded (id, cost)", [(item[1].id_, item[0]) for item in fringe])


	def isgoal(self, node, goal):
		if node == goal:
			return True
		return False


	def remove(self, fringe):
		""" Returns only the node from the (f, node) tuple """
		return fringe.pop()[1]

