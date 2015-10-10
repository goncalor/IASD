
# parses input files to build network
# parses client files
# builds solution file

# our created modules
import node, edge, graph

# other modules
import os.path
from sys import exit

def newGraph(filename):
	if not os.path.isfile(filename):
		print(filename + ' not found')
		exit()
					
	f = open(filename, 'r')

	nrCities, nrEdges = [int(i) for i in f.readline().split()]

	network = graph.Graph(nrCities)

	for line in f:
		city0, city1, transType, duration, price, ti, tf, period = line.split()

		network.addEdge(int(city0), int(city1), transType, \
				int(duration), int(price), int(ti), int(tf), int(period))

	return network


def readClientList(filename):
	if not os.path.isfile(filename):
		print(filename + ' not found')
		exit()
	
	f = open(filename, 'r')

	clients = []
	nrClients = int(f.readline())

	for line in f:
		l = line.split()
		d = {}
		d['clientNr'], d['from'], d['to'], d['timeAvail'], \
				d['criterion'] = l[:5]

		for constr in ['A1', 'A2', 'A3', 'B1', 'B2']:
			if constr in l:
				d[constr] = l[l.index(constr) + 1]

		clients.append(d)

	return clients
