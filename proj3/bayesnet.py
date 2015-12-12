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
        self.step_by_step = ''


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

        hidden_vars = set(self.net.keys()) - set(query) - set(evidence)
        hidden_vars = list(hidden_vars)

        # TODO apply an ordering function
        ordering = hidden_vars

        step_nr = 0
        for var in ordering:
            self.__add_new_state_verbose(step_nr, factors)

            step_nr += 1

            # join and sum factors that include var
            subset = []
            for factor in factors:
                if var in factor:
                    subset.append(factor)

            self.__add_factor_table_verbose(subset)

            new_factor = Factor.join(subset)
            new_factor.eliminate(var)

            self.step_by_step += '\n\n\tEliminate ' + str(var)

            for i in subset:
                factors.remove(i)
            factors.append(new_factor)

            self.__add_new_factor_verbose(new_factor)

        self.step_by_step += '\n\n' + str(step_nr) + ' Factors: ' + str(factors)
        #print('\nsolucao step by step:\n\n', self.step_by_step)

        final_factor = Factor.join(factors)

        # remove evidence columns
        for var in evidence:
            if var not in query:
                final_factor.eliminate(var)

        # build the final, normalized table
        norm_constant = 0
        for row in final_factor.table:
            norm_constant += final_factor[row]

        ppd_table = final_factor.table  # aliasing
        for row in ppd_table:
            ppd_table[row] = ppd_table[row] / norm_constant

        #print('ppd table', ppd_table)

        return ppd_table

    def __add_new_state_verbose(self, step_nr, factors):
        self.step_by_step += '\n\n' + str(step_nr) + ' Factors: ' + str(factors)

    def __add_factor_table_verbose(self, subset):
        self.step_by_step += '\n\tJoin ' + str(subset)
        for fac in subset:
            self.step_by_step += '\n\n\t\t' + str(list(fac.vars_.keys()))
            for row in fac.table:
                self.step_by_step += '\n\t\t' + str(row) + ' ' + str(fac.table[row])

    def __add_new_factor_verbose(self, new_factor):
        self.step_by_step += '\n\n\t\tNew Factor: '
        for row in new_factor.table:
                self.step_by_step += '\n\t\t\t' + str(row) + ' ' + str(new_factor.table[row])

    def __getitem__(cls, varname):
        return cls.net[varname]
