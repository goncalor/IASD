# our created modules
import iofiles
import genericsearch
from searchcriteria import SearchCriteria
from heuristic import Heuristic

# other modules
import argparse
import time
from pprint import pprint


parser = argparse.ArgumentParser(description='Solves "travel agent" problems.')
parser.add_argument('map', help='.map file defining the network')
parser.add_argument('requests', help='.cli file defining clients\' requests')
parser.add_argument('--no-heuristic', '-nh', action='store_true', help='use uninformed search')
args = parser.parse_args()

if __name__ == "__main__":

	print('Creating graph... ', end = '')
	graph = iofiles.newGraph(args.map)
	print('Done.')

	"""
	#debug
	print(graph)

	print('all edges')
	for edge in graph.edges:
		print(edge.info.transType, edge, 'duration', edge.info.duration, 'ti', edge.info.ti, 'period', edge.info.period)
	#
	"""
	clients_list = iofiles.read_client_list(args.requests)

	"""
	# debug
	for client in clients_list:
		print(client['clientNr'], client['criterion'], client)
	#
	"""

	sols = []

	print('Computing paths... ', end = '')

	# measure time
	start_time = time.time()

	for client in clients_list:

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

		heuristic= Heuristic(graph, client['criterion'])

		if args.no_heuristic:
			sc = SearchCriteria(client, lambda a, b: 0)
		else:
			sc = SearchCriteria(client, heuristic.heurIST_it)

		ans = genericsearch.generic_search(
				cliGraph,
				cliGraph.nodes[client['from']],
				cliGraph.nodes[client['to']], sc.initparents,
				sc.initcosts, sc.initfringe, sc.remove, sc.expand, sc.isgoal, sc.path)

		sols.append('{} {}'.format(client['clientNr'], ans))

		""""
		tmp = 0
		for value in heuristic.heurValues:
			print('heur', tmp, value)
			tmp += 1
		"""

		print(client['criterion'], "\t", client['clientNr'], ans)

	print('Done.')

	# write solutions to a file
	print('Preserving solutions... ', end = '')
	iofiles.write_sol(args.requests, sols)
	print('Done.')

	print("\ntotal time:", time.time() - start_time)

