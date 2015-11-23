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
        #print("sentence no inicio", sentence)
        #print(">> DPLL call")
        if sentence.is_satisfied_by(model):
            self.solution = model
            return True
        if sentence.check_empty_clause():
            return False

        new_model = copy(model)
        new_sentence = copy(sentence)

        #print('cena', sentence)
        #print('modelo', model.values)

        #print(new_sentence)
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
                    #print('foi daqui')
                    #print(clause)
                    return False


        #print(new_sentence)

        # find pure symbols. assign values to them
        for symbol in new_sentence.pure_symbols():

            if new_model[abs(symbol)] != None:
                #print("SCREEEEEEEEEEEEEEEEEEAM!\nSCREEEEEEEEEEEEEEEEEEAM")
                continue
            new_model.assign(abs(symbol), symbol > 0)



        #print(new_model)
        #print(new_sentence)
        # simplify the sentence according to the new model
        new_sentence.simplify(new_model)

        """
        # debug
        for clause in new_sentence:
            for var in clause:
                if new_model[abs(var)] != None:
                    print(new_sentence)
                    print(new_model.values)
                    exit()
        #
        """

        #print(new_sentence)

        #print(new_model, len(new_sentence), end=' ')

        # pick an unassigned literal from the model
        # TODO: accept other methods for choosing a literal
        # e.g.: use degree heuristic
        """
        try:
            literal = new_model.next_unassigned()
            #print(literal)
        except:
            #print("literals exhausted")
            return False
        """

        if len(new_sentence.clauses) == 0:
            self.solution = model
            return True
        elif len(new_sentence.clauses[0]) == 0:
            return False


        literal = abs(new_sentence.clauses[0][0])

        if new_model[literal] != None:
            print('barraca')

        return self.run(new_sentence, copy(new_model).assign(literal, True)) \
                or self.run(new_sentence, copy(new_model).assign(literal,
                    False))

