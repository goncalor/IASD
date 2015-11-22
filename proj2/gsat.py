from cnf_kb import CnfKb
from model import Model
import random


class GSat:

    def __init__(self, kb, restarts, max_climb):
        if not isinstance(kb, CnfKb):
            print('ERROR: GSat GSat() -> kb must be a CnfKb instance')
        self.kb = kb
        self.restarts = restarts
        self.max_climb = max_climb
        self.solution = None


    def __randomize_variables(self):
        """ returns a list with a random model """
        var_list = list()

        for var in range(0, self.kb.nbvar):
            if random.randint(0, 1) == 1:
                var_list.append(var+1)
            else:
                var_list.append(-(var+1))

        return var_list


    def __best_successor(self, var_values):
        """
        Args:
            var_values: A model
        Returns:
            A model that is a best successor of the 'var_values' model. And the
            score of that model. Returns a tuple.
        """
        var_scores = list()

        for var in range(self.kb.nbvar):
            # flip value for variable var
            temp_values = list(var_values)
            temp_values[var] = -temp_values[var]
            temp_values = tuple(temp_values)
            # get a score for the new set of values and store it

            var_scores.append(self.__satisfied_clauses(temp_values))

        # TODO: this can be made more efficient. but must think about
        # randomization (or remove it)
        max_score = max(var_scores)

        highest_scores = list()
        for i in range(len(var_scores)):
            if var_scores[i] == max_score:
                highest_scores.append(i)

        flipped_variable = highest_scores[random.randint(0, len(highest_scores) - 1)]
        aux_values = list(var_values)
        aux_values[flipped_variable] = -aux_values[flipped_variable]

        return aux_values, max_score


    def __satisfied_clauses(self, var_values):
        """
        Args:
            var_values: A model
        Returns:
            The number of satisfied clauses.
        """
        score = 0
        satisfied = 0

        # for all clauses
        for clause_index in range(len(self.kb)):
            clause = self.kb.get_clause(clause_index)
            # for each variable in the clause
            for var_index in range(len(clause)):
                # for each value in the assigned values
                for value_index in range(len(var_values)):
                    # if variable is not negated and value is also not negated the clause is satisfied and vice-versa
                    if clause[var_index] == var_values[value_index]:
                        score += 1
                        satisfied = True
                        break
                if satisfied:
                    satisfied = False
                    break

        return score


    def solve(self):
        for res in range(self.restarts):
            values = self.__randomize_variables()

            for climb in range(self.max_climb):

                values, score = self.__best_successor(values)

                if score == len(self.kb):
                    self.solution = Model(values=[i > 0 for i in values])
                    return True

        return False
