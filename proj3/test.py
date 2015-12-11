
from parser import BNParser
from parser import QueryParser
from bayesnet import BayesNet

bnfile = open('tests/01.bn')
qfile = open('tests/01.in')

bnparser = BNParser(bnfile)

bnparser.parse()

qparser = QueryParser(bnparser, qfile)

print('dicionario', bnparser.parsed)

qparser.parse()



print(qparser.get_var())
print(qparser.get_evidence())