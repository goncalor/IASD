# python modules needed
import os.path
from sys import exit

# our modules
from cnf_kb import CnfKb


def read_kb(filename):
    if not os.path.isfile(filename):
        print('ERROR: iofiles new_kb -> ' + filename + ' not found')
        exit()

    f = open(filename, 'r')

    while True:
        line=f.readline()
        if line[0] != 'c':
            break

    info = line.split()
    nbvar = int(info[2])

    new_kb = CnfKb(nbvar)

    for line in f:
        aux_list = list()
        for variable in line.split():
            variable = int(variable)
            aux_list.append(variable)

        aux_list.pop()
        new_kb.add_clause(tuple(aux_list))

    return new_kb


def write_kb(filename, kb):
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

            f.write(s + ' 0' +  '\n')
