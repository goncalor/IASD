import copy


class CnfKb:

    def __init__(self, nbvar):
        self.kb = list()
        self.nbvar = nbvar

    def add_clause(self, cnf_sentence):
        if len(cnf_sentence) == 0:
            print("ERROR: CnfKb add_clause: can't add an empty clause")
        if not isinstance(cnf_sentence, tuple):
            print("ERROR: CnfKb add_clause -> cnf_sentence must be a tuple")

        for i in range(len(cnf_sentence)):

            if not isinstance(cnf_sentence[i], int):
                print("ERROR: CnfKb add_clause: only int type tuples allowed")

            if abs(cnf_sentence[i]) > self.nbvar:
                print("ERROR: CnfKb add_clause: trying to add" + cnf_sentence[i] + "clause, there are only" +
                      self.nbvar + "clauses")

            if cnf_sentence[i] == 0:
                print("ERROR: CnfKb add_clause: 0 clause not allowed")

        self.kb.append(cnf_sentence)

    def remove_clauses(self, clause):
        if not isinstance(clause, tuple):
            print('ERROR: CnfKb remove_clauses -> clause must be tuple')

        removed = False
        for obj in list(self.kb):
            if obj == clause:
                self.kb.remove(clause)
                removed = True

        return removed

    def remove_clause(self, clause):
        if isinstance(clause, tuple):
            if clause in self.kb:
                self.kb.remove(clause)
                return True

            else:
                return False

        if isinstance(clause, int):
            self.kb.pop(clause)
            return True

        else:
            print('ERROR: CnfKb remove_clause -> clause must be either an int or a tuple')

    def get_clause(self, index):
        return self.kb[index]

    def check_empty_clause(self):
        for clause in self.kb:
            if len(clause) == 0:
                return True
        return False

    def __deepcopy__(self, memo=None):
        new_kb = CnfKb(self.nbvar)

        new_kb.kb = copy.deepcopy(self.kb, memo)

        return new_kb

    def __len__(self):
        return len(self.kb)

    def __str__(self):
        if len(self.kb) == 0:
            return '""'

        s = ''

        s += str(self.kb[0])

        if self.kb == 1:
            return s

        for i in range(1, len(self.kb)):
            s += "and"
            s += str(self.kb[i])

        return s
