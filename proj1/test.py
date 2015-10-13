#test
import graph
import edge
import node
import edgeinfo
from copy import deepcopy

mygraph= graph.Graph(6+1)

#http://www.csse.monash.edu.au/~lloyd/tildeAlgDS/Graph/PICS/WtUndMST5.gif
info= edgeinfo.EdgeInfo( 0, 3, 4, 100, 200, 50)
mygraph.addEdge(1, 4, info)
info= edgeinfo.EdgeInfo( 0, 4, 5, 100, 200, 50)
mygraph.addEdge(2, 4, info)
info= edgeinfo.EdgeInfo( 0, 4, 5, 100, 200, 50)
mygraph.addEdge(2, 5, info)

info= edgeinfo.EdgeInfo( 0, 4, 5, 100, 200, 50)
mygraph.addEdge(1, 2, info)
info= edgeinfo.EdgeInfo( 0, 3, 4, 100, 200, 50)
mygraph.addEdge(2, 3, info)
info= edgeinfo.EdgeInfo( 0, 2, 3, 100, 200, 50)
mygraph.addEdge(3, 4, info)
info= edgeinfo.EdgeInfo( 0, 3, 4, 100, 200, 50)
mygraph.addEdge(4, 5, info)
info= edgeinfo.EdgeInfo( 0, 1, 2, 100, 200, 50)
mygraph.addEdge(5, 6, info)
info= edgeinfo.EdgeInfo( 0, 5, 6, 100, 200, 50)
mygraph.addEdge(6, 1, info)


print('ola\n')

print(mygraph.sorted_price()[0].nodeA, mygraph.sorted_price()[0].nodeB)
print(mygraph.sorted_price()[1].nodeA, mygraph.sorted_price()[1].nodeB)
print(mygraph.sorted_price()[2].nodeA, mygraph.sorted_price()[2].nodeB)

print('\n')

print(mygraph.sorted_duration()[0].nodeA, mygraph.sorted_duration()[0].nodeB)
print(mygraph.sorted_duration()[1].nodeA, mygraph.sorted_duration()[1].nodeB)
print(mygraph.sorted_duration()[2].nodeA, mygraph.sorted_duration()[2].nodeB)


print(mygraph.edges[0].nodeA.id_, mygraph.edges[0].nodeB.id_)
print(mygraph.edges[0].neighbour(mygraph.nodes[1]))