import edge

# Defines the Node class.

class Node:

	neigh = []	# neighbours of this node
	id_ = None
	info = None

	def __init__(self, id_, info=None):
		self.id_ = id_
		self.neigh= []
		self.info = info

	def __str__(self):
		return str(self.id_) + ': ' + str([edge.nodeA.id_ if edge.nodeA is
			not self else edge.nodeB.id_ for edge in self.neigh])
