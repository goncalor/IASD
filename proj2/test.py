from cnf_kb import CnfKb
import copy

kb = CnfKb(3)

print(kb)
kb.add_clause((-1,-2,-3))
print(kb)
kb.add_clause((1,2,3))
print(kb)

kb2 = copy.deepcopy(kb)

print(kb.check_empty_clause())
kb.kb.append(())
kb.kb.append(())
print(kb.check_empty_clause())
print('kb:')
print(kb)
print('kb 2:')
print(kb2)

print('len kb ' + str(len(kb)))
print('len kb2 ' + str(len(kb2)))

kb.remove_clauses(())
print('kb:')
print(kb)





