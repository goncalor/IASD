from cnf_kb import CnfKb
import random
import


class GSat:

    def __init__(self, kb, restarts, max_climb):
        if not isinstance(kb, CnfKb):
            print('ERROR: GSat GSat() -> kb must be a CnfKb instance')
        self.kb = kb
        self.restarts = restarts
        self.max_climb = max_climb

    def __randomize_variables(self):
        var_list = list()

        for var in range(len(self.kb)):
            if random.randint(0,1) == 1:
                var_list.append(var)
            else:
                var_list.append(-var)

        return var_list

    def __best_successor(self, var_values):
        # TODO test this when __satisfied_clauses is done
        var_scores = list()

        for var in range(self.kb.nbvar):
            # flip value for variable var
            var_values[var] = -var_values[var]
            # get a score for the new set of values and store it
            var_scores = self.__satisfied_clauses(var_values)
            # flip it back
            var_values[var] = -var_values[var]

        max_score = max(var_scores)

        highest_scores = list()
        for i in range(var_scores):
            if var_scores[i] == max_score:
                highest_scores.append(i)

        flipped_variable = random.randint(0, len(highest_scores) - 1)
        var_values[flipped_variable] = -var_values[flipped_variable]

        return var_values



    def __satisfied_clauses(self, var_values):
        # TODO test this
        score = 0
        satisfied = 0

        # for all clauses
        for clause_index in range(len(self.kb)):
            clause = self.kb.get_clause(clause_index)
            # for each variable in the clause
            for var_index in range(len(clause)):
                # for each value in the assigned values
                for value_index in range(var_values):
                    # if variable is not negated and value is also not negated the clause is satisfied and vice-versa
                    if clause[var_index] == var_values[var_index]:
                        score += 1
                        satisfied = True
                        break
                if satisfied == True:
                    satisfied = False
                    continue

        return score

    def solve(self):

        for res in range(self.restarts):
            var_values = self.randomize_variables()









