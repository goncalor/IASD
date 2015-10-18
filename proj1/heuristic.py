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
        #debug
        else:
            startNode_id=startNode_id
            #print('a calcular', startNode_id)
        #

        startNode= self.relGraph.nodes[startNode_id]
        goalNode= self.relGraph.nodes[goalNode_id]

        #initialize all
        for node in self.relGraph.nodes:
            node.info= sys.maxsize

        fringe = list()
        fringe.append((0, startNode))

        startNode.info = 0

        while fringe:
            curr = self.__remove(fringe)

            if self.__isgoal(curr, goalNode):
                # TODO create memory for the heuristic. don't forget to consult memory before generating a new value

                self.heurValues[startNode.id_]= goalNode.info
                return goalNode.info

            # if we found a node with heuristic value calculate the heuristic to it and sum it to it's heurValue
            #it is assumed that
            if self.heurValues[curr.id_] != None:
                heur = self.heurIST_it(startNode_id, curr.id_)
                self.heurValues[startNode_id]= heur + self.heurValues[curr.id_]

                return self.heurValues[startNode_id]

            self.__expand(fringe, curr)
        else:
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
            cost = curr.info + getattr(edge.info, self.heurType)

            if neigh.info > cost:
                neigh.info = cost
                fringe.append((cost, neigh))

        # "Sorts are guaranteed to be stable."
        fringe.sort(key=lambda tup: tup[0], reverse=True)

        #print([(item[1].id_, item[0]) for item in fringe])

    def __remove(self, fringe):
        """ Returns only the node from the (f, node) tuple """
        return fringe.pop()[1]




