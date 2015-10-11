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
		return str(self.id_) + ': ' + str([edge.nodeA.id_ if edge.nodeA.id_ != self
			else edge.nodeA.id_ for edge in self.neigh])
