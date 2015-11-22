# our modules
from sentence import Sentence
from model import Model

# python modules needed
import os.path
from sys import exit


def read_kb(filename):
    """
    Creates a knowledge base from file in DIMACS format.
    :param filename: File's relative address.
    :return: Sentence instance.
    """
    if not os.path.isfile(filename):
        print('ERROR: iofiles read_kb -> ' + filename + ' not found')
        exit()

    f = open(filename, 'r')

    # consume comments in the preamble. comment lines start with a 'c'
    for line in f:
        if line[0] != 'c':
            break

    # the next line in the file contains info on the number of clauses and
    # variables. the line begins with a 'p' and the format (cnf).
    # example line: 'p cnf 5 3' --> 5 variables and 3 clauses
    (nbvar, nclauses)= [int(i) for i in line.split()[2:]]

    new_kb = Sentence(nbvar)

    # each of the next lines in the file represents a clause. each line ends
    # with a '0'. example line: ' 1 -5 4 0'
    # save the clauses into an object
    for line in f:
        while line[0] == ' ':
            line = line[1:len(line)]

        if line[0] == '%':
            break

        aux_list = list()
        for variable in line.split()[:-1]:   # discard the ending '0'
            variable = int(variable)
            aux_list.append(variable)

        new_kb.add_clause(tuple(aux_list))

    f.close()
    return new_kb


def write_kb(filename, kb, model, decision, time_):
    """
    Stores the solution into a DIMACS file. 
    :param filename: The name of the output file.
    :param kb: Sentence instance.
    :return:  ---
    """
    if not isinstance(kb, Sentence):
        print('ERROR: iofiles write_kb -> clauses must be a Sentence instance')

    if not isinstance(filename, str):
        print('ERROR: iofiles write_kb -> filename must be a string')

    with open(filename, 'w') as f:

        if decision == True:
            solution_field = str(1)
        elif decision == False:
            solution_field = str(0)
        else:
            solution_field = str(-1)

        variables_field = str(kb.nbvar) 
        clauses_field = str(len(kb.clauses))

        # write the solution line
        # s TYPE SOLUTION VARIABLES CLAUSES
        s = 's cnf ' + solution_field + ' ' + variables_field+ ' ' + clauses_field
        f.write(s + '\n')

        # write the timing line
        # t TYPE SOLUTION VARIABLES CLAUSES CPUSECS MEASURE1 ...
        # "MEASURE1 is required (just print 0 to abstain)"
        s = 't cnf ' + solution_field + ' ' + variables_field+ ' ' + \
                clauses_field + ' ' + str(time_) + ' 0'
        f.write(s + '\n')

        # write variable lines
        # v V
        if not model:
            return

        for var in model.get_numeric():
            f.write('v ' + str(var) + '\n')

