__author__ = 'Henrique'

from operator import attrgetter

from graph import Graph
import sys
from node import Node
from edge import Edge


class Heuristic:

    heurDict={'custo' : 'price', 'tempo' : 'duration'}

    def __init__(self, graph, cost_type):
        """
        :param graph: graph with no useless transport
        :param key: which key to optimize, custo or tempo
        :return:
        """

        if not isinstance(graph, Graph):
            print('ERROR-> Heuristic construtor: graphy must be of type Graph')
            return

        if not (cost_type == 'custo' or cost_type == 'tempo'):
            print('ERROR-> Heuristic construtor: cost_type must be "custo" or "tempo"')
            return

        cost_type= Heuristic.heurDict[cost_type]

        self.heurType= cost_type

        if cost_type == 'price':
            self.relGraph= graph.relax_price()
        else:
            self.relGraph= graph.relax_duration()

        self.heurValues= list()
        for node_id in range(len(self.relGraph.nodes)):
            self.heurValues.append(None)



    def heurIST_it(self, startNode_id, goalNode_id):
        """
        :param startNode_id: the node for which the heuristic value is desired
        :param goalNode_id: goal node
        :return: int heuristic value
        """

        #if the value is already calculated, return it instead of recalculating it
        if self.heurValues[startNode_id] != None:
            # debug
            #print('ja calculado', startNode_id, self.heurValues[startNode_id])
            #
            return self.heurValues[startNode_id]
        """
        #debug
        else:
            print('a calcular', startNode_id)
        #
        """

        startNode= self.relGraph.nodes[startNode_id]
        goalNode= self.relGraph.nodes[goalNode_id]

        # initialize all
        for node in self.relGraph.nodes:
            # (cost value, parent)
            node.info= (sys.maxsize, None)

        fringe = list()
        fringe.append((0, startNode))

        startNode.info = (0, None)

        while fringe:
            curr = self.__remove(fringe)

            if self.__isgoal(curr, goalNode):
                nodeList= list()
                heurList= list()

                self.heurValues[goalNode.id_] = 0

                auxNode = goalNode
                while auxNode.info[1] != None:
                    nodeList.append(auxNode)
                    heurList.append(auxNode.info[0])

                    auxNode= auxNode.info[1]

                nodeList.append(startNode)
                heurList.append(0)

                # debug
                #print([node.id_ for node in nodeList])
                #print(heurList)
                #

                heurList.reverse()

                for i in range(len(nodeList)):
                    self.heurValues[nodeList[i].id_]= heurList[i]

                """
                # debug
                print(self.heurValues)
                #
                """

                return self.heurValues[startNode.id_]

            self.__expand(fringe, curr)

        self.heurValues[startNode.id_]= sys.maxsize

        return sys.maxsize


    def __isgoal(self, node, goal):
        """
        :param nody: current node
        :param goal: goal node
        :return:
        """
        if node == goal:
            return True
        else:
            return False


    def __expand(self, fringe, curr):

        #for each edge in the neighbours of the node we are expanding
        for edge in curr.neigh:
            neigh = edge.neighbour(curr)

            #the new cost of the neighbour is the current node cost plus the
            cost = curr.info[0] + getattr(edge.info, self.heurType)

            if neigh.info[0] > cost:
                neigh.info = (cost, curr)
                fringe.append((cost, neigh))

        # "Sorts are guaranteed to be stable."
        fringe.sort(key=lambda tup: tup[0], reverse=True)

        #print([(item[1].id_, item[0]) for item in fringe])

    def __remove(self, fringe):
        """ Returns only the node from the (f, node) tuple """
        return fringe.pop()[1]
