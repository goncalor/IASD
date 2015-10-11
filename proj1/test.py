#test
import graph
import edge
import node
import edgeinfo

mygraph= graph.Graph(3+1)

info= edgeinfo.EdgeInfo( 0, 3, 10, 100, 200, 50)
mygraph.addEdge(1, 2, info)

info= edgeinfo.EdgeInfo( 0, 5, 20, 100, 200, 50)
mygraph.addEdge(2, 3, info)

info= edgeinfo.EdgeInfo( 0, 4, 30, 100, 200, 50)
mygraph.addEdge(3, 1, info)

print('ola\n')

print(mygraph.sorted_price()[0].nodeA, mygraph.sorted_price()[0].nodeB)
print(mygraph.sorted_price()[1].nodeA, mygraph.sorted_price()[1].nodeB)
print(mygraph.sorted_price()[2].nodeA, mygraph.sorted_price()[2].nodeB)

print('\n')

print(mygraph.sorted_duration()[0].nodeA, mygraph.sorted_duration()[0].nodeB)
print(mygraph.sorted_duration()[1].nodeA, mygraph.sorted_duration()[1].nodeB)
print(mygraph.sorted_duration()[2].nodeA, mygraph.sorted_duration()[2].nodeB)