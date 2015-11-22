

from sentence import Sentence
from wsat import WSat
import iofiles
from gsat import GSat
import time
from model import Model


# kb3 = iofiles.read_kb('problems/uf50-01.cnf')
kb3 = Sentence(5)

kb3.add_clause({1, 2, 3})
kb3.add_clause({1, 2})
kb3.add_clause({3, 4, 5})
kb3.add_clause({-5})


print(kb3)
"""
greedy = GSat(kb3, 5, 200)


start = time.time()
solved = greedy.solve()
print(solved)
if solved:
    print(greedy.solution.values)
print(str(time.time() - start) + ' seconds')
"""

walk = WSat(kb3, 0.5, 1000)

start = time.time()
solved = walk.solve()
if solved:
    print(walk.solution.values)
print(str(time.time() - start) + ' seconds')



