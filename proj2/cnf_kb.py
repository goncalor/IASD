

class CnfKb:

    def __init__(self):
        self.kb = list()

    def add_clause(self, cnf_sentence):
        if len(cnf_sentence) == 0:
            print("ERROR: CnfKb add_clause: can't add an empty clause")

        self.kb.append(cnf_sentence)

    def check_empty_clause(self):
        for i in self.kb:
            if len(self.kb[i]) == 0:
                return True
        return False

    
