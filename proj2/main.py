# our created modules
import iofiles
from model import Model
from gsat import GSat
from wsat import WSat
from dpll import DPLL

# other modules
import argparse
import time


parser = argparse.ArgumentParser(description='Solves Boolean Satisfiability Problems (SAT).')
parser.add_argument('--gsat', '-gs', action='store_true', help='use GSAT')
parser.add_argument('--wsat', '-ws', action='store_true', help='use WalkSAT')
parser.add_argument('--dpll', '-dp', action='store_true', help='use DPLL algorithm')
parser.add_argument('sentence', type=argparse.FileType('r'), nargs='+',
        help='a file in DIMASC format, containing a sentence')
args = parser.parse_args()

if __name__ == "__main__":

    # measure time
    start_time_program = time.time()

    for f in args.sentence:
        print('Reading sentence from ' + f.name + '... ', end = '')
        sentence = iofiles.read_kb(f.name)
        print('Done.\n')
        filename_no_ext = f.name[:f.name.rindex('.')]

        if args.gsat:
            print('Solving with GSAT... ')
            start_time = time.time()

            greedy = GSat(sentence, 5, 200)
            greedy.solve()

            print('Done.')
            time_save = time.time() - start_time
            print("GSAT time:", time_save, '\n')
            #print(greedy.solution)

            if greedy.solution:
                print("Satisfiable.")
                iofiles.write_kb(filename_no_ext+".gsat.sol", sentence,
                        greedy.solution, True, time_save)
            else:
                print("No solution found.")
                iofiles.write_kb(filename_no_ext+".gsat.sol", sentence,
                        greedy.solution, None, time_save)

        if args.wsat:
            print('Solving with WalkSAT... ')
            start_time = time.time()

            walk = WSat(sentence, 0.5, 1000)
            walk.solve()

            print('Done.')
            time_save = time.time() - start_time
            print("WalkSAT time:", time_save, '\n')
            #print(walk.solution)

            if walk.solution:
                print("Satisfiable.")
                iofiles.write_kb(filename_no_ext+".wsat.sol", sentence,
                        walk.solution, True, time_save)
            else:
                print("No solution found.")
                iofiles.write_kb(filename_no_ext+".wsat.sol", sentence,
                        walk.solution, None, time_save)

        if args.dpll:
            print('Solving with DPLL... ')
            start_time = time.time()

            dpll = DPLL()
            dpll.run(sentence, Model(sentence.nbvar))

            print('Done.')
            time_save = time.time() - start_time
            print("DPLL time:", time_save, '\n')
            if dpll.solution:
                print("Satisfiable.")
                iofiles.write_kb(filename_no_ext+".dpll.sol", sentence,
                        dpll.solution, True, time_save)
            else:
                print("Unsatisfiable.")
                iofiles.write_kb(filename_no_ext+".dpll.sol", sentence,
                        dpll.solution, False, time_save)


    # write solutions to a file
    print('Solutions were written to .sol files.')

    print("\nTotal time:", time.time() - start_time_program)

