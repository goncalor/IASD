# Defines the Edge class.

import node


class Edge:

	def __init__(self, nodeA, nodeB, transType, duration, price, ti, tf, period):
		self.nodeA = nodeA
		self.nodeB = nodeB
		self.transType = transType
		self.duration = duration
		self.price = price
		self.ti = ti
		self.tf = tf
		self.period = period
		
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
