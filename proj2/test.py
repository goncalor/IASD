
import copy

from sentence import Sentence
from wsat import WSat
import iofiles
from gsat import GSat
import time



kb3 = Sentence(14)

kb3.add_clause((-3,-14))
kb3.add_clause((14,))
kb3.add_clause((9,))
kb3.add_clause((14,-5))
kb3.add_clause((5,3,-9))
kb3.add_clause((3,))

print(kb3.pure_symbols())


"""
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



"""