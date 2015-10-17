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

	print('Creating graph... ', end='')
	graph = iofiles.newGraph(args.map)
	print('Done.')

	print(graph)

	clients_list = iofiles.read_client_list(args.requests)

	pprint(clients_list)


	for client in clients_list:
		sc = SearchCriteria(client)

		ans = genericsearch.generic_search(graph,
				graph.nodes[client['from']],
				graph.nodes[client['to']], sc.initparents,
				sc.initcosts, sc.initfringe, sc.remove, sc.expand, sc.isgoal,
				sc.path)

		print(ans)
