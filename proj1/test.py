#test
import graph
import edge
import node
import edgeinfo
from copy import deepcopy

mygraph= graph.Graph(2+1)

#http://www.csse.monash.edu.au/~lloyd/tildeAlgDS/Graph/PICS/WtUndMST5.gif
info= edgeinfo.EdgeInfo( 0, 3, 10,100, 200, 50)
mygraph.addEdge(1, 2, info)
info= edgeinfo.EdgeInfo( 0, 3, 15, 100, 200, 50)
mygraph.addEdge(1, 2, info)

info= edgeinfo.EdgeInfo( 0, 3, 20, 100, 200, 50)
new_edge= edge.Edge(mygraph.nodes[1], mygraph.nodes[2], info)

mygraph.addEdge(new_edge)



print('ola\n')

print(mygraph)


