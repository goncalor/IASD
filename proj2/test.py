
import copy

from cnf_kb import CnfKb
import iofiles


kb3 = iofiles.read_kb('in.txt')

kb3.add_clause((1, 2, 3))
kb3.add_clause((1, 2, 3))
kb3.add_clause((1,))

kb3.remove_variable(3)
kb3.remove_variable(1)
kb3.remove_variable(2)

print(kb3)

var = 2
print(str(var) + ' is pure: ' + str(kb3.pure_symbol(var)))
print(kb3.pure_symbol())

print(kb3.unit_variables())


