
import copy

from cnf_kb import CnfKb
import iofiles


kb3 = iofiles.read_kb('in.txt')

print(kb3)

iofiles.write_kb('out', kb3)



