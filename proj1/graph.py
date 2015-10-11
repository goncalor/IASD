
from node import Node
from edge import Edge

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

		
	def sorted_price(self):
		return sorted(self.edges, key= attrgetter('price'))
		
	def sorted_duration(self):
		return sorted(self.edges, key= attrgetter('duration'))
	
		
	def __str__(self):
		s = ''
		for node in self.nodes:
			s += str(node) + '\n'

		return s

