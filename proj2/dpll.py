from model import Model
from cnf_kb import CnfKb

"""
Implements a DPLL SAT solver class.
"""

class DPLL:

    def __init__(self):
        pass



    def run(self, sentence):
        pass





"""
function DPLL(Φ)
   if Φ is a consistent set of literals
       then return true;
   if Φ contains an empty clause
       then return false;
   for every unit clause l in Φ
      Φ ← unit-propagate(l, Φ);
   for every literal l that occurs pure in Φ
      Φ ← pure-literal-assign(l, Φ);
   l ← choose-literal(Φ);

   return DPLL(Φ ∧ l) or DPLL(Φ ∧ not(l));

"""
