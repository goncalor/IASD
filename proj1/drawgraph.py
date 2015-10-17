import networkx as nx
import matplotlib.pyplot as plt
import sys
import iofiles

graph = {}
no_show = False

def check_args():
	""" checks if a file was supplied to the script """
	if len(sys.argv) < 2:
		print("Usage: python " + sys.argv[0] + " <internet_file> [--no-show]\n")
		exit()
	elif len(sys.argv) == 3 and sys.argv[2] == "--no-show":
		global no_show
		no_show = True

def loadgraph():
	""" loads the graph from a file into memory """
	global graph

	filename = sys.argv[1]

	try:
		f = open(filename, 'r')
	except IOError:
		print("Failed to open '" + filename + "'.")
		exit()

	print('Creating graph... ', end='')
	graph = iofiles.newGraph(filename)
	print('Done.')

	f.close()	# close the file


def draw_graph(graph):
	""" prepares the graph to be shown or exported """
	G = nx.Graph()
	labels = {}

	for edge in graph.edges:
		G.add_edge(edge.nodeA.id_, edge.nodeB.id_)

		labels[(edge.nodeA.id_, edge.nodeB.id_)] = (edge.info.price,
		edge.info.duration, edge.info.transType)



	#pos = nx.circular_layout(G)
	pos = nx.spring_layout(G)
	#pos = nx.shell_layout(G)

	nx.draw_networkx_nodes(G, pos, node_color = "w")
	nx.draw_networkx_edges(G, pos, edge_color = "k")
	nx.draw_networkx_labels(G, pos)
	nx.draw_networkx_edge_labels(G, pos, edge_labels = labels)


check_args()
loadgraph()
draw_graph(graph)

plt.savefig(sys.argv[1] + ".png")
if not no_show:
	plt.show()

