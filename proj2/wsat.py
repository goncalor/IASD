from sentence import Sentence
from model import Model
import random

class WSat:

    def __init__(self, kb, p, max_flips):
        if not isinstance(kb, Sentence):
            print('ERROR: WSat WSat() -> clauses must be a Sentence instance')
        self.sentence = kb
        self.p = p
        self.max_flips = max_flips
        self.solution = None

    def __randomize_variables(self):
        var_list = list()

        for var in range(0, self.sentence.nbvar):
            if random.randint(0, 1) == 1:
                var_list.append(var+1)
            else:
                var_list.append(-(var+1))

        return var_list

    def __satisfied_clauses(self, var_values):
        """
        Args:
            var_values: A model
        Returns:
            The number of satisfied clauses.
        """
        score = 0

        # for all clauses
        for clause in self.sentence:
            # for each variable in the clause
            for var in clause:
                if var in var_values:
                    score += 1
                    break

        return score

    def __random_clause(self):
        clause_nr = random.randint(0, len(self.sentence) - 1)

        return self.sentence.clauses[clause_nr]

    def __flip_variable(self):
        random_nr = random.random()

        return self.p > random_nr

    def __random_var_from_clause(self, clause):
        return random.sample(clause, 1)[0]

    def __best_successor(self, var_values):
        var_scores = list()

        for var in range(self.sentence.nbvar):
            # flip value for variable var
            temp_values = list(var_values)
            temp_values[var] = -temp_values[var]
            temp_values = tuple(temp_values)
            # get a score for the new set of values and store it

            var_scores.append(self.__satisfied_clauses(temp_values))

        max_score = max(var_scores)

        highest_scores = list()
        for i in range(len(var_scores)):
            if var_scores[i] == max_score:
                highest_scores.append(i)

        flipped_variable = highest_scores[random.randint(0, len(highest_scores) - 1)]
        aux_values = list(var_values)
        aux_values[flipped_variable] = -aux_values[flipped_variable]

        return aux_values

    def solve(self):
        var_values = self.__randomize_variables()

        clause_nr = len(self.sentence)

        for i in range(self.max_flips):
            if self.__satisfied_clauses(var_values) == clause_nr:
                self.solution = Model(values=[i > 0 for i in var_values])
                return True

            clause = self.__random_clause()

            if self.__flip_variable():
                variable = self.__random_var_from_clause(clause)

                var_values = list(var_values)
                for var in var_values:
                    if abs(var) == variable:
                        index = var_values.index(var)
                        var_values.pop(index)
                        var = -var
                        var_values.insert(index, var)

                var_values = tuple(var_values)

            else:
                var_values = self.__best_successor(var_values)

        return False

