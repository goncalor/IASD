import edge

# Defines the Nod class.

class Node:

	neigh = []	# neighbours of this node
	id_ = None
	info = None

	def __init__(self, id_, info=None):
		self.id_ = id_
		self.neigh= []
		self.info = info
