from itertools import product
from collections import OrderedDict
from pprint import pprint, pformat


class Factor:

    def __init__(self, vars_, table):
        """
        Args:
            vars_: an OrderedDict whose keys are variable's names and values are
                their domains.
            table: a dictionary with the probability table for this factor.
        """
        self.vars_ = vars_
        self.table = table
        print(self.table)


    @classmethod
    def join(self, factors):
        """
        Joins a list of factors into the product of those factors.

        Vars:
            factors: a list of factors.

        Returns:
            A new factor that is the product of the joined factors.
        """
        vars_ = OrderedDict()

        # store all unique variables and their domains
        for factor in factors:
            vars_.update(factor.vars_)
        print(vars_)

        # initialise table for the new factor. initialisation is to 1 because
        # the entries will later be involved in products
        table = {}
        for row in product(*list(vars_.values())):
            table[row] = 1

        # store the index in the tuples of the table that correspond to each
        # variable
        var_index = dict(zip(list(vars_.keys()), list(range(len(vars_.keys())))))
        print(var_index)

        # compute each of the rows in the table of the factor
        for row in table:
            for factor in factors:
                tmplst = []
                for var in factor:
                    tmplst.append(row[var_index[var]])

                foreign_row = tuple(tmplst)
                table[row] *= factor[foreign_row]
                #print(factor[foreign_row])
        #pprint(table)

        return Factor(vars_, table)


    def eliminate(self, var):
        pass


    def __contains__(self, key):
        return key in self.vars_


    def __getitem__(cls, row):
        return cls.table[row]


    def __iter__(self):
        self.itercurrent = 0
        self.iterlst = list(self.vars_.keys())
        return self


    def __next__(self):
        if self.itercurrent == len(self.vars_):
            raise StopIteration
        else:
            ret = self.iterlst[self.itercurrent]
            self.itercurrent += 1
            return ret


    def __str__(self):
        return "{}\n{}".format(str(list(self.vars_.keys())),
                pformat(self.table))


    def __repr__(self):
        return str(list(self.vars_.keys()))
