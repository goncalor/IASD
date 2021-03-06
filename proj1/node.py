import edge
# Defines the Node class.

class Node:

	def __init__(self, id_, info=None):
		self.id_ = id_
		self.neigh= []
		self.info = info

	def __str__(self):
		return str(self.id_) + ': ' + str([edge.nodeA.id_ if edge.nodeA is
			not self else edge.nodeB.id_ for edge in self.neigh])


	def __eq__(self, other):
		""" Returns True if the IDs of the nodes match;
		or if other is not a Node. """
		if not isinstance(other, Node):
			return False
		if self.id_ == other.id_:
			return True
		else:
			return False
