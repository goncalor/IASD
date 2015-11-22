
import copy

from sentence import Sentence
from wsat import WSat
import iofiles
from gsat import GSat
import time


kb3 = iofiles.read_kb('problems/uf50-01.cnf')

print(kb3)

walk = WSat(kb3, 0.5, 1000)
greedy = GSat(kb3, 5, 200)

start = time.time()
print(walk.solve())
print(str(time.time() - start) + ' seconds')

start = time.time()
print(greedy.solve())
print(str(time.time() - start) + ' seconds')



