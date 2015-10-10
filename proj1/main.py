# our created modules
import iofiles

# other modules
import argparse


parser = argparse.ArgumentParser(description='Solves "travel agent" problems.')
parser.add_argument('map', help='.map file defining the network')
parser.add_argument('requests', help='.cli file defining clients\' requests')
args = parser.parse_args()

if __name__ == "__main__":

    print('Creating graph... ', end='')
    graph = iofiles.newGraph(args.map)
    print('Done.')
