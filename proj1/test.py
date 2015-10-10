#test
import graph
import edge
import node

mygraph= Graph(3)

addEdge(0, 1, 1, 1, 10, 100, 200, 101)
addEdge(1, 2, 2, 3, 20, 100, 200, 101)
addEdge(2, 0, 3, 2, 30, 100, 200, 101)


#print all nodes and their info
for i=0:len(mygraph.nodes)
    print('NODE ' + i + '\n')
    print('nodeID ' + mygraph.nodes[i].id + '\n')
    
    for j=0:len(mygraph.nodes[i].neigh)
        #if this is the nodeA print nodeB
        if mygraph.nodes[i].neigh[j].nodeA.id == mygraph.nodes[i].id
            print('\tneighbour: ' + mygraph.node[i].neigh[j].nodeB.id + '\n')
        #else this is nodeB, print nodeA
        else
            print('\tneighbour: ' + mygraph.node[i].neigh[j].nodeA.id + '\n')    
    
#print all edges and their info
for i= 0:len(mygraph.edges)
    print('EDGE ' + i + '\n')
    print('nodeA ' + mygraph.edges[i].nodeA + '\n')
    print('nodeB ' + mygraph.edges[i].nodeB + '\n')
    print('trnas ' + mygraph.edges[i].transType + '\n')
    print('duration ' + mygraph.edges[i].duration + '\n')
    print('price ' + mygraph.edges[i].price + '\n')
    print('ti ' + mygraph.edges[i].ti + '\n')
    print('tf ' + mygraph.edges[i].tf + '\n')
    print('period ' + mygraph.edges[i].period + '\n')
    print('\n\n')
    
