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
		

	def sorted_price():
		pass
	

	def sorted_time():
		pass
"""
	def __eq__(self, edge):
		if (self.nodeA == edge.nodeA and self.nodeB == edge.nodeB) \
				or (self.nodeA == edge.nodeB && self.nodeB == edge.nodeA):
			return True
		else:
			return False
"""			
