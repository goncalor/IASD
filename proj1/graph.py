
from node import Node
from edge import Edge
from operator import attrgetter
from copy import deepcopy
from transport import Transport

class Graph:

	nodes= []
	edges= []

	def __init__(self, nrNodes=0, lst=None):
		self.nodes= []
		self.edges= []

		if lst != None:
			id_ = 0
			for item in lst:
				self.nodes.append(Node(id_, item))
		else:
			for id_ in range(nrNodes):
				self.nodes.append(Node(id_))

	def addEdge(self, *args):
		#nodeA_id, nodeB_id, info
		if len(args) == 3:
			nodeA= self.nodes[args[0]]
			nodeB= self.nodes[args[1]]
			info= args[2]

			new_edge= Edge(nodeA, nodeB, args[2])

			nodeA.neigh.append(new_edge)
			nodeB.neigh.append(new_edge)
			self.edges.append(new_edge)

		#edge
		elif len(args) == 1:
			if not isinstance(args[0], Edge):
				print('ERROR-> addEdge: expected 1 arg of type Edge')
				return
			args[0].nodeA.neigh.append(args[0])
			args[0].nodeB.neigh.append(args[0])
			self.edges.append(args[0])

	def removeEdge(self, rem_edge):

		if not isinstance(rem_edge, Edge):
			print('not instance')
			return


		#remove the edge from the edges list
		self.edges.remove(rem_edge)

		#remove the edge from each nodes' neighbours
		rem_edge.nodeA.neigh.remove(rem_edge)
		rem_edge.nodeB.neigh.remove(rem_edge)


	def sorted_price(self):
		return sorted(self.edges, key= attrgetter('info.price'))

	def sorted_duration(self):
		return sorted(self.edges, key= attrgetter('info.duration'))

	def __len__(self):
		return len(self.nodes)

	def __str__(self):
		s = ''
		for node in self.nodes:
			s += str(node) + '\n'

		return s

	def deepcopy(self):
		new_graph= Graph(len(self.nodes))

		for edge in self.edges:
			# if info becomes non static, clone it!
			new_graph.addEdge(edge.nodeA.id_, edge.nodeB.id_, edge.info)

		return new_graph

	def relax_price(self):
		relgraph= deepcopy(self)

		for current_node in range(1, len(relgraph.nodes)):

			#create a list of DIFFERENT neighbours
			neighbour_list= list()
			for current_edge in range(0, len(relgraph.nodes[current_node].neigh)):
				if relgraph.nodes[current_node].neigh[current_edge].neighbour(relgraph.nodes[current_node]) not in neighbour_list:
					neighbour_list.append(relgraph.nodes[current_node].neigh[current_edge].neighbour(relgraph.nodes[current_node]))


			optimal_edges= list()
			for neigh in neighbour_list:
				#find the first edge that points to this neighbour
				for edge in relgraph.nodes[current_node].neigh:
					#if this edge points to this neighbour store it in edge_aux
					if edge.neighbour(relgraph.nodes[current_node]) == neigh:
						edge_aux= edge	#auxiliar variable to find the optimal edge
						break

				#find the optimal edge for neighbour neigh
				for edge in relgraph.nodes[current_node].neigh:
					#if the edge leads to neigh and if its price is inferior to the edge_aux, store it in edge_aux (auxiliar variable)
					if edge.neighbour(relgraph.nodes[current_node]) == neigh and edge.info.price < edge_aux.info.price:
						edge_aux=edge

				optimal_edges.append(edge_aux)

			#remove all edges from the current node to add the optimal right next
			while len(relgraph.nodes[current_node].neigh) > 0:
				relgraph.removeEdge(relgraph.nodes[current_node].neigh[0])

			for edgy in optimal_edges:
				relgraph.addEdge(edgy)

		return relgraph

	def relax_duration(self):
		relgraph= deepcopy(self)

		for current_node in range(1, len(relgraph.nodes)):

			#create a list of DIFFERENT neighbours
			neighbour_list= list()
			for current_edge in range(0, len(relgraph.nodes[current_node].neigh)):
				if relgraph.nodes[current_node].neigh[current_edge].neighbour(relgraph.nodes[current_node]) not in neighbour_list:
					neighbour_list.append(relgraph.nodes[current_node].neigh[current_edge].neighbour(relgraph.nodes[current_node]))


			optimal_edges= list()
			for neigh in neighbour_list:
				#find the first edge that points to this neighbour
				for edge in relgraph.nodes[current_node].neigh:
					#if this edge points to this neighbour store it in edge_aux
					if edge.neighbour(relgraph.nodes[current_node]) == neigh:
						edge_aux= edge	#auxiliar variable to find the optimal edge
						break

				#find the optimal edge for neighbour neigh
				for edge in relgraph.nodes[current_node].neigh:
					#if the edge leads to neigh and if its price is inferior to the edge_aux, store it in edge_aux (auxiliar variable)
					if edge.neighbour(relgraph.nodes[current_node]) == neigh and edge.info.duration < edge_aux.info.duration:
						edge_aux=edge

				optimal_edges.append(edge_aux)

			#remove all edges from the current node to add the optimal right next
			while len(relgraph.nodes[current_node].neigh) > 0:
				relgraph.removeEdge(relgraph.nodes[current_node].neigh[0])

			for edgy in optimal_edges:
				relgraph.addEdge(edgy)

		return relgraph

	def removeEdges(self, attr_name, attr):

		if not (attr_name == 'price' or attr_name == 'duration' or attr_name == 'transType'):
			print('ERROR-> removeEdges: cost_type must be "price" or "duration" or "transType"')
			return

		new_graph= self.deepcopy()

		if attr_name == 'price':
			for edge in list(new_graph.edges):
				if edge.info.price > attr:
					new_graph.removeEdge(edge)

			return new_graph

		elif attr_name == 'duration':
			for edge in list(new_graph.edges):
				if edge.info.duration > attr:
					new_graph.removeEdge(edge)

			return new_graph

		elif attr_name == 'transType':
			for edge in list(new_graph.edges):

				if edge.info.transType == Transport(attr):
					new_graph.removeEdge(edge)

			return new_graph



















