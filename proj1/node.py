import edge

# Defines the Nod class.

class Node:

	neigh=[]	#neighbours
	id= -1	#city id

	def __init__(self, id):
		self.neigh= list()
		self.id= id

