from factor import Factor
from itertools import product
from collections import OrderedDict

class BayesNet:

    def __init__(self, bayesnet):
        """
        Args:
            bayesnet: A dictionary containing the description of a Bayesian network.
        """
        self.net = bayesnet


    def ppd(self, query, evidence):
        """
        Computes a posterior probability distribution for the current network,
        given some query variable and some evidence.

        Args:
            query:
            evidence: a dictionary of evidence variables. {'varname': varvalue}

        Returns:
            A dictionary whose keys are tuples of query values. The values of
            the dictionary are the values of the PPD.
        """
        factors = []

        # build a list with the initial factors
        for k in self.net:
            if k == self.net[k]['alias']:    # skip aliases
                continue
            parents = self.net[k]['parents']
            # build a list with the domains of the parents
            # use values from the evidence if available
            dom = [self.net[parent]['values'] if parent not in evidence else
                    [evidence[parent]] for parent in parents]
            # add this variables' domain, or value from evidence if available
            dom += [self.net[k]['values'] if k not in evidence else
                    [evidence[k]]]

            # the variables for this factor are the parents of the variable and
            # the variable
            vars_ = parents + [k]
            # build the probability table for this factor
            table = {}
            for row in product(*dom):
                table[row] = self[vars_[-1]]['cpt'][row]

            #print(k, dom)
            factors.append(Factor(OrderedDict(zip(vars_, dom)), table))

        print(factors)

        # debug
        tmp = []
        for factor in factors:
            if 'Burglary' in factor:
                tmp.append(factor)
        #print(tmp)
        print(Factor.join(tmp))


    def __getitem__(cls, varname):
        return cls.net[varname]
