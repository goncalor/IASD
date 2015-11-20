from model import Model
from cnf_kb import CnfKb
from copy import copy

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
        if sentence.is_satisfied_by(model)
            return True
        if sentence.check_empty_clause()
            return False

        new_model = copy(model)
        new_sentence = copy(sentence)
        model_modified = False

        # find unit clauses. assign values to them
        for clause in sentence:
            if len(clause) == 1:
                # assign the needed value to make the clause true
                new_model.assign(abs(clause[0]), clause[0] > 0)
                # remove the unit clause
                new_sentence.remove_clause(clause)
                model_modified = True

        # find pure symbols. assign values to them
        for symbol in new_sentence.pure_symbols():
            new_model.assign(abs(symbol), symbol > 0)
            model_modified = True

        # simplify the sentence according to the new model
        if model_modified:
            new_sentence.simplify(new_model)

        # pick an unassigned literal from the model
        # TODO: accept other methods for choosing a literal
        literal = new_model.next_unassigned()

        # TODO: check this
        new_model.flip(next_unassigned)
        return self.run(new_sentence, new_model)


"""

- use degree heuristic for choose-literal()
"""
