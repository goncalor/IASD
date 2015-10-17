#test
import graph
import edge
import node
import edgeinfo
from copy import deepcopy
import heuristic
import sys

mygraph= graph.Graph(6+1)

#http://www.csse.monash.edu.au/~lloyd/tildeAlgDS/Graph/PICS/WtUndMST5.gif
#duration price
info= edgeinfo.EdgeInfo( 'comboio', 3, 4, 100, 200, 50)
mygraph.addEdge(1, 4, info)
info= edgeinfo.EdgeInfo( 'aviao', 4, 5, 100, 200, 50)
mygraph.addEdge(2, 4, info)
info= edgeinfo.EdgeInfo( 'aviao', 4, 5, 100, 200, 50)
mygraph.addEdge(2, 5, info)


info= edgeinfo.EdgeInfo( 'aviao', 4, 5, 100, 200, 50)
mygraph.addEdge(1, 2, info)
info= edgeinfo.EdgeInfo( 'aviao', 20, 21, 100, 200, 50)
mygraph.addEdge(1, 2, info)
info= edgeinfo.EdgeInfo( 'aviao', 3, 4, 100, 200, 50)
mygraph.addEdge(2, 3, info)
info= edgeinfo.EdgeInfo( 'aviao', 2, 3, 100, 200, 50)
mygraph.addEdge(3, 4, info)
info= edgeinfo.EdgeInfo( 'aviao', 3, 4, 100, 200, 50)
mygraph.addEdge(4, 5, info)
info= edgeinfo.EdgeInfo( 'aviao', 1, 2, 100, 200, 50)
mygraph.addEdge(5, 6, info)
info= edgeinfo.EdgeInfo( 'aviao', 5, 6, 100, 200, 50)
mygraph.addEdge(6, 1, info)


print('ola\n')

print(mygraph)

print(mygraph.edges[0].info.transType)




