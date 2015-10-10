
# parses input files to build network
# parses client files
# builds solution file

import os.path
from sys import exit

def newgraph(filename):
    if not os.path.isfile(filename):
        print(filename + ' not found')
        exit()
        
    f = open(filename, 'r')

    nrCities, nrEdges = f.readline().split()

    graph = [Node(id) for id in range(nrCities + 1)]

    for line in f:
        city0, city1, transType, duration, price, ti, tf, period = line.split()

        edge = Edge(graph[city0], graph[city1], transType, duration, price, ti, tf, period)
