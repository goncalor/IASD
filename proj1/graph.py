
from node import Node
from edge import Edge
from operator import attrgetter
from copy import deepcopy

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

		
	def addEdge(self, nodeA_id, nodeB_id, info):
		nodeA= self.nodes[nodeA_id]
		nodeB= self.nodes[nodeB_id]
		
		new_edge= Edge(nodeA, nodeB, info)

		nodeA.neigh.append(new_edge)
		nodeB.neigh.append(new_edge)
		self.edges.append(new_edge)

	def removeEdge(self, rem_edge):
		#go through edges searching for the edge to remove
		for i in range(len(self.edges)):
			if rem_edge == self.edges[i]:
				self.edges.remove(i)
				#assuming there is only one edge with the same price and the same duration
				break

		for i in range(len(rem_edge.nodeA.neigh)):
			if rem_edge == rem_edge.nodeA.neigh[i]:
				rem_edge.nodeA.neigh.remove(i)

		for i in range(len(rem_edge.nodeB.neigh)):
			if rem_edge == rem_edge.nodeB.neigh[i]:
				rem_edge.nodeB.neigh.remove(i)

		
	def sorted_price(self):
		return sorted(self.edges, key= attrgetter('info.price'))
		
	def sorted_duration(self):
		return sorted(self.edges, key= attrgetter('info.duration'))
	
		
	def __str__(self):
		s = ''
		for node in self.nodes:
			s += str(node) + '\n'

		return s

	def deepcopy(self):
		new_graph= Graph(0)

		new_graph.nodes= deepcopy(self.nodes)
		new_graph.edges= deepcopy(self.edges)

		return new_graph

	def relax_price(self):
		relgraph= deepcopy(self)

		#go through node list to remove non optimal connections
		for current_node in range(1, len(relgraph.nodes)):
			#pick one edge
			for current_edge in range(0, len(relgraph.nodes[current_node].neigh)):
				#check if all others are edges
				for checking_edge in range(current_edge, len(relgraph.nodes[current_node].neigh)):
					#if the edge we are currently checking is to the same neighbour as the current edge
					if relgraph.nodes[current_node].neigh[current_edge].neighbour(relgraph.nodes[current_node]) == \
						relgraph.nodes[current_node].neigh[checking_edge].neighbour(relgraph.nodes[current_node]):

						#and if the price of the edge we are checking is bigger
						if relgraph.nodes[current_node].neigh[checking_edge].info.price > \
							relgraph.nodes[current_node].neigh[current_edge].info.price :
							#remove the checking edge
							relgraph.removeEdge(relgraph.edges[checking_edge])

						#if the price of the edge we are checking is smaller
						if relgraph.nodes[current_node].neigh[checking_edge].info.price < \
							relgraph.nodes[current_node].neigh[current_edge].info.price :
							#remove the current edge
							relgraph.removeEdge(relgraph.edges[current_edge])

						#if the price is equal
						if relgraph.nodes[current_node].neigh[checking_edge].info.price == \
							relgraph.nodes[current_node].neigh[current_edge].info.price :

							#if the checking edge has a bigger duration
							if relgraph.nodes[current_node].neigh[checking_edge].info.duration > \
							relgraph.nodes[current_node].neigh[current_edge].info.duration:
								#remove the checking edge
								relgraph.removeEdge(relgraph.edges[checking_edge])

							#otherwise we can remove the other
							else:
								relgraph.removeEdge(relgraph.edges[current_edge])
















