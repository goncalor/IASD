# Defines the Edge class.

import node


class Edge:

	nodeA = None
	nodeB = None
	info = None

	def __init__(self, nodeA, nodeB, info=None):
		self.nodeA = nodeA
		self.nodeB = nodeB
		self.info = info

	def neighbour(self, node):
		if node == self.nodeA:
			return self.nodeB
		elif node == self.nodeB:
			return self.nodeA
		else:
			return None


	def __eq__(self, edge):
		#check if the nodes the edge connects are the same
		if (self.nodeA == edge.nodeA and self.nodeB == edge.nodeB) \
				or (self.nodeA == edge.nodeB and self.nodeB == edge.nodeA):
			#if the the edges connected and the price and duration are the same, the edge is the same
			if self.info.price == edge.info.price and self.info.duration == edge.info.duration:
				return True
		else:
			return False


