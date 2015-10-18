# our created modules
import iofiles
import genericsearch
from searchcriteria import SearchCriteria

# other modules
import argparse
from pprint import pprint


parser = argparse.ArgumentParser(description='Solves "travel agent" problems.')
parser.add_argument('map', help='.map file defining the network')
parser.add_argument('requests', help='.cli file defining clients\' requests')
args = parser.parse_args()

if __name__ == "__main__":

	print('Creating graph... ', end = '')
	graph = iofiles.newGraph(args.map)
	print('Done.')

	print(graph)

	# debug
	print('all edges')
	for edge in graph.edges:
		print(edge.info.transType, edge, 'duration', edge.info.duration, 'ti', edge.info.ti, 'period', edge.info.period)

	clients_list = iofiles.read_client_list(args.requests)

	# debug
	for client in clients_list:
		print(client['clientNr'], client['criterion'], client)
	#

	for client in clients_list:
		sc = SearchCriteria(client)

		# TODO remove copy, possibly
		cliGraph= graph.deepcopy()
		if 'A1' in client:
			cliGraph = graph.removeEdges('transType', client['A1'])
		elif 'A2' in client:
			cliGraph = graph.removeEdges('duration', client['A2'])
		elif 'A3' in client:
			cliGraph = graph.removeEdges('price', client['A3'])
			"""
			# debug
			print('===graph===')
			print(graph)
			print('===cliGraph===')
			print(cliGraph)
			break
			#
			"""
		"""
		# debug
		for edge in cliGraph.edges:
			print(edge.info.transType, edge, 'duration', edge.info.duration, 'ti', edge.info.ti, 'period', edge.info.period, 'tf', edge.info.tf)
		#
		"""


		ans = genericsearch.generic_search(
				cliGraph,
				cliGraph.nodes[client['from']],
				cliGraph.nodes[client['to']], sc.initparents,
				sc.initcosts, sc.initfringe, sc.remove, sc.expand, sc.isgoal,
				sc.path)

		print(client['clientNr'], ans)
