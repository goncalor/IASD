
# parses input files to build network
# parses client files
# builds solution file

# our created modules
import node, edge, graph
from edgeinfo import EdgeInfo

# other modules
import os.path
from sys import exit

def newGraph(filename):
	if not os.path.isfile(filename):
		print(filename + ' not found')
		exit()
					
	f = open(filename, 'r')

	nrCities, nrEdges = [int(i) for i in f.readline().split()]

	network = graph.Graph(nrCities + 1)

	for line in f:
		city0, city1, transType, duration, price, ti, tf, period = line.split()

		network.addEdge(int(city0), int(city1),
				EdgeInfo(transType, int(duration), int(price), \
						int(ti), int(tf), int(period)))

	f.close()
	return network


def read_client_list(filename):
	if not os.path.isfile(filename):
		print(filename + ' not found')
		exit()
	
	f = open(filename, 'r')

	clients = []
	nr_clients = int(f.readline())

	for line in f:
		l = line.split()
		d = {}
		d['clientNr'], d['from'], d['to'], d['timeAvail'] = \
				[int(i) for i in l[:4]]

		d['criterion'] = l[4]

		for constr in ['A1', 'A2', 'A3', 'B1', 'B2']:
			if constr in l:
				#if constraint can be converted to int
				if l[l.index(constr) + 1].isdigit():
					d[constr] = int(l[l.index(constr) + 1])
				else:
					d[constr] = l[l.index(constr) + 1]

		clients.append(d)

	f.close()
	return clients


def write_sol(filename, solutions):
	""" 'filename' is the file name of the .cli file """

	filename = filename[:filename.rindex('.')] + ".sol"

	with open(filename, 'w') as f:
		f.write("\n".join(map(lambda x: str(x), solutions)) + '\n')
