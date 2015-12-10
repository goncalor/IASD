from itertools import product


class Factor:

    def __init__(self, bayesnet, vars_, vardomain):
        self.vars_ = list(vars_)
        self.table = {}

        # build the probability table for this factor
        for entry in product(*vardomain):
            self.table[entry] = bayesnet[vars_[-1]]['cpt'][entry]

        print(self.table)


    def join(self, factors, evidence):
        pass



    def eliminate(self, var):
        pass


    def __str__(self):
        return str(self.vars_)


    def __repr__(self):
        return str(self.vars_)
