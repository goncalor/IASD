
import copy

from cnf_kb import CnfKb
import iofiles
from gsat import GSat


kb3 = iofiles.read_kb('problems/uf20-01.cnf')

print(kb3)

greedy = GSat(kb3, 5, int(1.5 * kb3.nbvar))

print(greedy.solve())



