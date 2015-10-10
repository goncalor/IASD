#test
import graph
import edge
import node

mygraph= graph.Graph(3)

mygraph.addEdge(1, 2, 1, 1, 10, 100, 200, 50)
mygraph.addEdge(2, 3, 2, 3, 20, 100, 200, 50)
mygraph.addEdge(3, 1, 3, 2, 30, 100, 200, 50)


#print all nodes and their info
for i in range(len(mygraph.nodes)):
    print('NODE ' + str(i))
    print('nodeID ' + str(mygraph.nodes[i].id))
    
    for j in range(len(mygraph.nodes[i].neigh)):
        #if this is the nodeA print nodeB
        if mygraph.nodes[i].neigh[j].nodeA.id == mygraph.nodes[i].id:
            print('\tneighbour: ' + str(mygraph.nodes[i].neigh[j].nodeB.id))
        #else this is nodeB, print nodeA
        else:
            print('\tneighbour: ' , mygraph.nodes[i].neigh[j].nodeA.id)    
    
#print all edges and their info
for i in range(len(mygraph.edges)):
    print('EDGE ' , i)
    print('nodeA ' , mygraph.edges[i].nodeA.id )
    print('nodeB ' , mygraph.edges[i].nodeB.id)
    print('trnas ' , mygraph.edges[i].transType)
    print('duration ', mygraph.edges[i].duration)
    print('price ' , mygraph.edges[i].price)
    print('ti ' , mygraph.edges[i].ti)
    print('tf ' , mygraph.edges[i].tf)
    print('period ' , mygraph.edges[i].period)
    print('\n\n')


print(mygraph.sorted_price()[0].nodeA.id, mygraph.sorted_price()[0].nodeB.id)
print(mygraph.sorted_price()[1].nodeA.id, mygraph.sorted_price()[1].nodeB.id)
print(mygraph.sorted_price()[2].nodeA.id, mygraph.sorted_price()[2].nodeB.id)

    
