#test
import graph
import edge
import node
import edgeinfo
from copy import deepcopy

mygraph= graph.Graph(2+1)

#EdgeInfo(transType, duration, price, ti, tf, period)

info= edgeinfo.EdgeInfo( 0, 4 , 5, 100, 200, 50)
mygraph.addEdge(1, 2, info)

info= edgeinfo.EdgeInfo( 0, 4, 10, 100, 200, 50)
mygraph.addEdge(1, 2, info)

info= edgeinfo.EdgeInfo( 0, 4, 15, 100, 200, 50)
new_edge= edge.Edge(mygraph.nodes[1], mygraph.nodes[2], info)
mygraph.addEdge(new_edge)


print('ola\n')

print(mygraph)
print('\n relax: ')
#print(mygraph.relax_price())
