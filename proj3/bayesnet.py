from factor import Factor
from itertools import product
from collections import OrderedDict
import pprint

class BayesNet:

    def __init__(self, bayesnet, verbose=False):
        """
        Args:
            bayesnet: A dictionary containing the description of a Bayesian network.
        """
        self.net = bayesnet
        self.verbose = verbose


    def ppd(self, query, evidence):
        """
        Computes a posterior probability distribution for the current network,
        given some query variable and some evidence.
        :param query:
        :param evidence: a dictionary of evidence variables. {'varname': varvalue}
        :return: A dictionary whose keys are tuples of query values. The values of
            the dictionary are the values of the PPD.
        """
        factors = []

        # build a list with the initial factors
        for k in self.net:
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

            factors.append(Factor(OrderedDict(zip(vars_, dom)), table))

        if self.verbose:
            print(factors)

        hidden_vars = set(self.net.keys()) - set(query) - set(evidence)
        hidden_vars = list(hidden_vars)

        # TODO apply an ordering function
        # TODO!!!! undo this
        #ordering = hidden_vars
        ordering = ['Alarm', 'Earthquake']

        for var in ordering:
            # join and sum factors that include var
            subset = []
            for factor in factors:
                if var in factor:
                    subset.append(factor)
            new_factor = Factor.join(subset)
            new_factor.eliminate(var)

            for i in subset:
                factors.remove(i)
            factors.append(new_factor)

        print(new_factor)
        print(factors)
        factors = [Factor.join(factors)]
        print(factors)
        print(factors[0])


    def __getitem__(cls, varname):
        return cls.net[varname]
