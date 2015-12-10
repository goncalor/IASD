from factor import Factor

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
            #print(k, dom)
            factors.append(Factor(self, parents + [k], dom))

        if self.verbose:
            print(factors)


    def __getitem__(cls, varname):
        return cls.net[varname]
