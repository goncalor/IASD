from itertools import product


class Factor:

    def __init__(self, bayesnet, vars_, vardomain):
        self.vars_ = list(vars_)
        self.table = {}

        # build the probability table for this factor
        for entry in product(*vardomain):
            self.table[entry] = bayesnet[vars_[-1]]['cpt'][entry]

        #print(self.table)


    @classmethod
    def join(self, factors):
        """
        Joins a list of factors into the product of those factors.

        Vars:
            factors: a list of factors.

        Returns:
            A new factor that is the product of the joined factors.
        """
        vars_ = []

        # store all unique variables
        for factor in factors:
            for var in factor.vars_:
                vars_.append(var)
        vars_ = list(set(vars_))
        print(vars_)



    def eliminate(self, var):
        pass




    def __contains__(self, key):
        return key in self.vars_


    def __str__(self):
        return str(self.vars_)


    def __repr__(self):
        return str(self.vars_)
