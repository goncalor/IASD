# our created modules
from parser import BNParser, QueryParser, SolWriter
from bayesnet import BayesNet

# other modules
import argparse
import time

parser = argparse.ArgumentParser(description='Probabilistic reasoner based on Bayesian networks.')
parser.add_argument('bayesnet', type=argparse.FileType('r'), help='an input file where the Bayesian network is defined')
parser.add_argument('query', type=argparse.FileType('r'), help='an input file where the query and evidence are defined')
parser.add_argument('--verbose', '-v', action='store_true', help='explain what is being done')
args = parser.parse_args()

if __name__ == "__main__":

    # measure time
    start_time_program = time.time()

    print('Parsing Bayesian network from ' + args.bayesnet.name + '... ', end = '')
    bnp = BNParser(args.bayesnet)
    bnp.parse()
    print('Done.')

    print('Parsing query from ' + args.query.name + '... ', end = '')
    qparser = QueryParser(bnp, args.query)
    qparser.parse()
    evidence = qparser.get_evidence()
    vartoinf = qparser.get_var()
    print('Done.\n')

    # create the Bayesian network
    bn = BayesNet(bnp.parsed)

    # compute the poseterior probability distribution
    ppd = bn.ppd([vartoinf], evidence)

    sol_write = SolWriter(args.query.name)
    if args.verbose:
        sol_write.write_sol(ppd, qparser.query_str, qparser.evidence_str, bn.step_by_step)
    else:
        sol_write.write_sol(ppd, qparser.query_str, qparser.evidence_str)
    sol_write.close_file()

    # write solutions to a file
    print('Solution written to .sol file.')

    print("\nTotal time:", time.time() - start_time_program)


