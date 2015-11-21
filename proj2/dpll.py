from model import Model
from cnf_kb import CnfKb
from copy import copy, deepcopy

"""
Implements a DPLL SAT solver class.

    Algorithm DPLL
      Input: A set of clauses Φ.
      Output: A Truth Value.

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

Φ ∧ l denotes the simplified result of substituting "true" for l in Φ.
"""

class DPLL:

    def __init__(self):
        pass


    def run(self, sentence, model):
        """
        Runs DPLL to check whether a sentence is satisfiable.

        Args:
            sentence: The whose satisfiability will be checked.
            model: A starting Model

        Returns:
            True if the sentence is satisfiable. False otherwise.
        """
        print(">> DPLL call")
        if sentence.is_satisfied_by(model):
            print("sentence", sentence)
            print("SOLUTION!\n> > > > > ", model)
            return True
        if sentence.check_empty_clause():
            return False

        new_model = deepcopy(model)
        new_sentence = deepcopy(sentence)

        # find unit clauses. assign values to them
        for clause in sentence:
            #print(clause)
            if len(clause) == 1:
                # assign the needed value to make the clause true
                new_model.assign(abs(clause[0]), clause[0] > 0)
                # remove the unit clause
                new_sentence.remove_clause(clause)

        # find pure symbols. assign values to them
        for symbol in new_sentence.pure_symbols():
            new_model.assign(abs(symbol), symbol > 0)

        # simplify the sentence according to the new model
        new_sentence.simplify(new_model)

        print(new_model, len(new_sentence), end=' ')

        # pick an unassigned literal from the model
        # TODO: accept other methods for choosing a literal
        try:
            literal = new_model.next_unassigned()
            print(literal)
        except:
            print("literals exhausted")
            return False


        # TODO: check this
        return self.run(new_sentence, copy(new_model).assign(literal, True)) \
                or self.run(new_sentence, copy(new_model).assign(literal,
                    False))


"""

- use degree heuristic for choose-literal()
"""
