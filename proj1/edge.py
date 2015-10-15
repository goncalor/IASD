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

	def neighbour(self, nody):
		""" Returns the node 'nody' is connected to. """
		#maybe change comparison to 'is'
		if nody == self.nodeA:
			return self.nodeB
		elif nody == self.nodeB:
			return self.nodeA
		else:
			return None

	def __str__(self):
		return '[' + str(self.nodeA.id_) + ',' + str(self.nodeB.id_) + ']'


	def __eq__(self, other):

		if not isinstance(other, Edge):
			return False

		#check if the nodes the edge connects are the same
		if (self.nodeA == other.nodeA and self.nodeB == other.nodeB) \
				or (self.nodeA == other.nodeB and self.nodeB == other.nodeA):
			#if the the edges connected and the price and duration are the same, the edge is the same
			if self.info.price == other.info.price and self.info.duration == other.info.duration:
				return True
		else:
			return False


