
import copy

from cnf_kb import CnfKb
from wsat import WSat
import iofiles
from gsat import GSat


kb3 = iofiles.read_kb('problems/uf20-01.cnf')

print(kb3)

walk = WSat(kb3, 0.5, 1000)
greedy = GSat(kb3, 5, 200)

print(walk.solve())
print(greedy.solve())



