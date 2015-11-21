# our created modules
import iofiles
from model import Model
from gsat import GSat
from wsat import WSat
from dpll import DPLL

# other modules
import argparse
import time
from pprint import pprint


parser = argparse.ArgumentParser(description='Solves Boolean Satisfiability Problems (SAT).')
parser.add_argument('--gsat', '-gs', action='store_true', help='use GSAT')
parser.add_argument('--wsat', '-ws', action='store_true', help='use WalkSAT')
parser.add_argument('--dpll', '-dp', action='store_true', help='use DPLL algorithm')
parser.add_argument('sentence', type=argparse.FileType('r'), nargs='+', \
        help='a file in DIMASC format, containing a sentence')
args = parser.parse_args()

if __name__ == "__main__":


    # measure time
    start_time_program = time.time()

    for f in args.sentence:
        print('Reading sentence from ' + f.name + '... ', end = '')
        sentence = iofiles.read_kb(f.name)
        print('Done.\n')

        if args.gsat:
            print('Solving with GSAT... ')
            start_time = time.time()

            greedy = GSat(sentence, 5, 200)
            greedy.solve()

            print('Done.')
            print("GSAT time:", time.time() - start_time, '\n')
            #print(greedy.solution)

            if greedy.solution:
                print("Satisfiable.")
            else:
                print("Unsatisfiable.")

        if args.wsat:
            print('Solving with WalkSAT... ')
            start_time = time.time()

            walk = WSat(sentence, 0.5, 1000)
            walk.solve()

            print('Done.')
            print("WalkSAT time:", time.time() - start_time, '\n')
            #print(walk.solution)

            if walk.solution:
                print("Satisfiable.")
            else:
                print("Unsatisfiable.")

        if args.dpll:
            print('Solving with DPLL... ')
            start_time = time.time()

            ret = DPLL().run(sentence, Model(sentence.nbvar))

            print('Done.')
            print("DPLL time:", time.time() - start_time, '\n')
            if ret:
                print("Satisfiable.")
            else:
                print("Unsatisfiable.")



    # write solutions to a file
    print('Preserving solutions... ', end = '')
    # TODO: save solution
    print('Done.')

    print("\nTotal time:", time.time() - start_time_program)

