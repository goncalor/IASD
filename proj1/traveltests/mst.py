__author__ = 'Henrique'

from copy import deepcopy
import node
import edge

class MST:

    nodes= []
    edges= []

    def __init__(self, nodesList, sortedEdges):
        self.nodes= deepcopy(nodesList)
        tempEdges= deepcopy(sortedEdges)

        #cleanse all neighbours
        for i in range(len(self.nodes)):
           self.nodes[i].neigh=[]

        for i in range(len(sortedEdges)):
            #redirect edges nodes for the MST nodes
            tempEdges[i].nodeA= self.nodes[tempEdges[i].nodeA.id]
            tempEdges[i].nodeB= self.nodes[tempEdges[i].nodeB.id]

            #if the nodeA is not connected add this edge
            if len(tempEdges[i].nodeA.neigh) == 0:
                #add edge to the edges list
                self.edges.append(tempEdges[i])
                #add edge to neighbours of the nodes
                self.nodes[tempEdges[i].nodeA.id].neigh.append(tempEdges[i])
                self.nodes[tempEdges[i].nodeB.id].neigh.append(tempEdges[i])
                continue
            elif len(tempEdges[i].nodeB.neigh) == 0:
                #add edge to the edges list
                self.edges.append(tempEdges[i])
                #add edge to neighbours of the nodes
                self.nodes[tempEdges[i].nodeA.id].neigh.append(tempEdges[i])
                self.nodes[tempEdges[i].nodeB.id].neigh.append(tempEdges[i])

