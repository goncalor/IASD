__author__ = 'Henrique'

from operator import attrgetter

import graph
import sys
from node import Node
from edge import Edge


class Heuristic:

    heurType=''         # price or duration
    relGraph= None      # graph

    def __init__(self, graphy, cost_type):
        """
        :param graph: graph with no useless transport
        :param key: which key to optimize, price or duration
        :return:
        """
        if not isinstance(graphy, graph.Graph):
            print('ERROR-> Heuristic construtor: graphy must be of type Graph')
            return

        if not (cost_type == 'price' or cost_type == 'duration'):
            print('ERROR-> Heuristic construtor: cost_type must be "price" or "duration"')
            return

        heurType= cost_type

        if cost_type == 'price':
            self.relGraph= graphy.relax_price()
        else:
            self.relGraph= graphy.relax_duration()

    def heurIST_it(self, startNody, goalNody):
        """
        :param startNody: the node for which the heuristic value is desired
        :param goalNody: goal node
        :return: int heuristic value
        """
        if not isinstance(startNody, Node):
            print('ERROR-> heurIST_it(): startNody must be of type Node')
            return

        if not isinstance(goalNody, Node):
            print('ERROR-> heurIST_it(): goalNody must be of type Node')
            return

        fringe = list()

        fringe.append((0, startNody))

        #make this general
        for nody in self.relGraph.nodes:
            nody.info = sys.maxsize
        startNody.info = 0

        while len(fringe) != 0:
            curr = self.__remove(fringe)

            print('heurist_it curr.id_', curr.id_)

            if self.__isgoal(curr, goalNody):
                return "found you"

            self.__expand(fringe, curr)

        return sys.maxsize

    def __isgoal(self, nody, goal):
        """
        :param nody: current node
        :param goal: goal node
        :return:
        """
        if nody == goal:
            return True
        else:
            return False


    def __expand(self, fringe, curr):

        for edgy in curr.neigh:
            neighby = edgy.neighbour(curr)

            aux= 'info.' + self.heurType
            cost = curr.info + getattr(edgy, 'info.' + self.heurType)

            if neighby.info > cost:
                neighby.info = cost
                fringe.append((cost, neighby))

        # "Sorts are guaranteed to be stable."
        fringe.sort(key=lambda tup: tup[0], reverse=True)

        print([(item[1].id_, item[0]) for item in fringe])

    def __remove(self, fringe):
        """ Returns only the node from the (f, node) tuple """
        return fringe.pop()[1]




