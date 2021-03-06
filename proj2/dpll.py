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
        self.solution = None

    def run(self, sentence, model):
        """
        Runs DPLL to check whether a sentence is satisfiable.

        Args:
            sentence: The whose satisfiability will be checked.
            model: A starting Model

        Returns:
            True if the sentence is satisfiable. False otherwise.
        """
        if sentence.is_satisfied_by(model):
            self.solution = model
            return True
        if sentence.check_empty_clause():
            return False

        new_model = copy(model)
        new_sentence = copy(sentence)

        # find unit clauses. assign values to them
        for clause in sentence:
            if len(clause) == 1:
                if new_model[abs(clause[0])] == None:
                    # assign the needed value to make the clause true
                    new_model.assign(abs(clause[0]), clause[0] > 0)
                    # remove the unit clause
                    new_sentence.remove_clause(clause)
                elif (new_model[abs(clause[0])] and clause[0] < 0) \
                        or (not new_model[abs(clause[0])] and clause[0] > 0):
                    return False

        # find pure symbols. assign values to them
        for symbol in new_sentence.pure_symbols():
            if new_model[abs(symbol)] != None:
                continue
            new_model.assign(abs(symbol), symbol > 0)

        # simplify the sentence according to the new model
        new_sentence.simplify(new_model)

        # pick an unassigned literal from the model
        # TODO: accept other methods for choosing a literal
        # e.g.: use degree heuristic
        if len(new_sentence.clauses) == 0:
            self.solution = new_model
            return True
        elif len(new_sentence.clauses[0]) == 0:
            return False


        literal = abs(new_sentence.clauses[0][0])

        return self.run(new_sentence, copy(new_model).assign(literal, True)) \
                or self.run(new_sentence, copy(new_model).assign(literal,
                    False))

