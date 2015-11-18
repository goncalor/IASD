# python modules needed
import os.path
from sys import exit

# our modules
from cnf_kb import CnfKb


def read_kb(filename):
    """
    Creates a knowledge base from file in DIMACS format.
    :param filename: File's relative address.
    :return: CnfKb instance.
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

    new_kb = CnfKb(nbvar)

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


def write_kb(filename, kb):
    """
    Writes knowledge base in DIMACS format file.
    :param filename: Output file's relative address
    :param kb: CnfKb instance.
    :return:  ---
    """
    if not isinstance(kb, CnfKb):
        print('ERROR: iofiles write_kb -> kb must be a CnfKb instance')

    if not isinstance(filename, str):
        print('ERROR: iofiles write_kb -> filename must be a string')

    filename += '.txt'

    with open(filename, 'w') as f:

        # write the first line of the DIMACS format
        s = 'p cnf ' + str(kb.nbvar) + ' ' + str(len(kb))
        f.write(s + '\n')

        # write the cnf sentences
        for i in range(len(kb)):
            clause = kb.get_clause(i)

            # case it is an empty clause
            if len(clause) == 0:
                f.write('0')
                continue

            # case it is a 1 variable clause
            s = str(clause[0])
            if len(clause) == 1:
                f.write(s + ' 0')
                continue

            # case clause has more than one variable
            for j in range(1, len(clause)):
                s += ' ' + str(clause[j])

            f.write(s + ' 0' + '\n')
