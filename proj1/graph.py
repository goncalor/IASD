
import node
import edge

class Graph:

	nodes= []
	edges= []
	
	def __init__(self, nodes_nr):
		nodes= list()
		edges= list()
		
		for id in range(nodes_nr + 1):
			nodes.append(node.Node(id))
		
		
	def addEdge(self, nodeA_id, nodeB_id, transType, duration, price, ti, tf, period):
		nodeA= self.nodes[nodeA_id]
		nodeB= self.nodes[nodeB_id]
		
		new_edge= Edge(nodeA, nodeB, transType, duration, price, ti, tf, period)
		edges.append(new_edge)
		
		nodeA.neigh.append(new_edge)
		nodeB.neigh.append(new_edge)
		
		
	def sorted_price(self):
		return sorted(self.edges, key= attrgetter('price'))
		
	def sorted_duration(self):
		return sorted(self.edges, key= attrgetter('duration'))
	
		
		
		
		
