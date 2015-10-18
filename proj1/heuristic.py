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

        for node in self.relGraph.nodes:
            #node.info= float("inf")
            node.info = sys.maxsize

    def heurIST_it(self, startNode_id, goalNode_id):
        """
        :param startNode_id: the node for which the heuristic value is desired
        :param goalNode_id: goal node
        :return: int heuristic value
        """
        # TODO remove when it's all over
        """
        if not isinstance(startNody, Node):
            print('ERROR-> heurIST_it(): startNody must be of type Node')
            return

        if not isinstance(goalNody, Node):
            print('ERROR-> heurIST_it(): goalNody must be of type Node')
            return
        """

        startNode_id= self.relGraph.nodes[startNode_id]
        goalNode_id= self.relGraph.nodes[goalNode_id]


        fringe = list()

        fringe.append((0, startNode_id))

        #initialize all

        startNode_id.info = 0


        while len(fringe) != 0:
            curr = self.__remove(fringe)

            if self.__isgoal(curr, goalNode_id):
                # TODO create memory for the heuritic. dont forget to consult memory before generating a new value

                return goalNode_id.info

            self.__expand(fringe, curr)

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




