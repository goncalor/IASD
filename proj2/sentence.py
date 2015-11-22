from copy import copy, deepcopy


class Sentence:

    def __init__(self, nbvar):
        """
        Initializes the clauses as an empty list and sets the number of variables nbvar.
        :param nbvar: Integer with the number of variables in the knowledge base.
        :return: ---
        """
        if not isinstance(nbvar, int):
            print("ERROR: Sentence Sentence() -> nbvar must be an integer")

        self.clauses = list()
        self.nbvar = nbvar

    def add_clause(self, cnf_sentence):
        """
        This function adds a CNF clause to the knowledge base. Empty clauses are not allowed.
        :param cnf_sentence: CNF clause in a set.
        :return: Nothing.
        """
        #if len(cnf_sentence) == 0:
        #    print("ERROR: Sentence add_clause -> can't add an empty clause")

        self.__insert(cnf_sentence)

    def __insert(self, cnf_sentence):
        """
        Private method for inserting in list
        :param cnf_sentence:
        :return: ---
        """
        self.clauses.append(cnf_sentence)

    def remove_clauses(self, clause):
        """
        Removes all clauses equal to the argument provided.
        :param clause: Clause to eliminate in CNF set.
        :return: Nothing.
        """
        if not isinstance(clause, set):
            print('ERROR: Sentence remove_clauses -> clause must be set')

        old_size = len(self)

        self.clauses = [cl for cl in self.clauses if clause != cl]

        return len(self) < old_size

    def remove_clause(self, clause):
        """
        Removes the clause provided in the argument. If clause is a set, it
        searches and deletes it. If clause is an integer, deletes the clause in
        that index.
        :param clause: Either a CNF set or an integer.
        :return: If the argument is a set, returns true or false if clause is removed or not. If the argument is an
                    integer returns the removed CNF set.
        """
        if isinstance(clause, set):
            if clause in self.clauses:
                self.clauses.remove(clause)
                return True

            else:
                return False

        if isinstance(clause, int):
            return self.clauses.pop(clause)

        else:
            print('ERROR: Sentence remove_clause -> clause must be either an int or a set')

    def get_clause(self, index):
        """
        Returns the clause in the given index.
        :param index: Index of the clause, must be an integer.
        :return: CNF set.
        """
        if not isinstance(index, int):
            print('ERROR: Sentence get_clause -> index must be an integer')

        return self.clauses[index]

    # TODO: change name to 'has_empty_clause'
    def check_empty_clause(self):
        """
        Checks if there are empty clauses in the knowledge base.
        :return: Boolean.
        """
        for clause in self:
            if len(clause) == 0:
                return True
        return False

    def remove_variable(self, variable):
        """
        Removes one variable from all clauses in the knowledge base
        :param variable: Variable to remove. Must be an integer between 1 and nbvar.
        :return: ---
        """
        if not isinstance(variable, int):
            print('ERROR: Sentence pure_symbol -> variable must be of type int')

        if variable == 0 or abs(variable) > self.nbvar:
            print('ERROR: Sentence remove_clause -> variable is 0 or not defined')

        for clause_index in range(len(self.clauses)):
            if variable in self.clauses[clause_index]:
                self.clauses[clause_index].remove(variable)

    def unit_variables(self):
        """
        Returns all unit variables in the knowledge base. Negation (-) is included
        :return: set of CNF sets.
        """
        units = set()

        for clause in self.clauses:
            if len(clause) == 1:
                # units.append(list(clause)[0])
                units.union(clause)

        return units

    def is_pure_symbol(self, symbol):
        """
        Finds whether a symbol is pure.

        Args:
            symbol: The symbol we want to check for pureness. A negative value
            represents negation.
        Returns:
            True if 'symbol' is pure (includes the case in which the symbol is
            not found in the sentece). False if 'symbol' is not pure.
        """
        for clause in self:
            if -symbol in clause:
                return False

        return True

    def pure_symbols(self):
        """
        Returns a list with all the pure symbols in the sentence. Negative
        values represent the negation of the a symbol.
        :return: list of
        """
        findings = [None] * (self.nbvar+1)
        pure = [None] * (self.nbvar+1)

        for clause in self:
            for var in clause:
                if findings[abs(var)] == None:  # first time found
                    findings[abs(var)] = var
                    pure[abs(var)] = True
                elif pure[abs(var)] and findings[abs(var)] + var == 0:
                        pure[abs(var)] = False  # not pure

        return [symbol for symbol in findings if symbol and pure[abs(symbol)]]

    def __remove_var_from_clause(self, variable, clause):
        """
        Removes the variable from the clause. If the variable is negated, the argument must be negated and vice-versa.
        Clause might be either a clause or an index. If it is a clause it will check the first clause in knowledge base
        that match this one. If clause is an integer it will check if a clause in given index. Returns true if removed.
        :param variable: Integer.
        :param clause: Set of integers.
        :return: Boolean.
        """
        if isinstance(clause, set):
            for cl in self:
                if cl == clause:
                    clause.remove(variable)
                    return True

            return False
            """
            for clause_index in range(len(self.clauses)):
                if clause == self.clauses[clause_index] and variable in self.clauses[clause_index]:

                    clause = self.remove_clause(clause_index)
                    new_clause = [var for var in clause if var != variable]
                    new_clause = tuple(new_clause)
                    self.__insert(new_clause, clause_index)

                    if len(new_clause) < len(clause):
                        return True
                    else:
                        return False
            """

        if isinstance(clause, int):
            clause = self.clauses[clause]
            if cl == clause:
                    clause.remove(variable)
                    return True
            else:
                return False
            """
            clause = self.remove_clause(clause_index)
            new_clause = [var for var in clause if var != variable]
            new_clause = tuple(new_clause)
            self.__insert(new_clause, clause_index)
            if len(new_clause) < len(clause):
                return True
            else:
                return False
            """

    @staticmethod
    def __is_subset(subclause, clause):
        """
        If subclause is a subset of clause, returns true
        :param subclause: CNF set.
        :param clause: CNF set.
        :return: Boolean.
        """
        return subclause <= clause

    def is_satisfied_by(self, model):
        """
        Finds is a given model satisfies the sentence.

        Args:
            model: The model the sentence will be tested with.

        Returns:
            True if 'model' satisfies the sentence. False otherwise.
        """
        #print(model)

        for clause in self:
            for var in clause:
                if (var > 0 and model[var]) or (var < 0 and
                        model[abs(var)] == False):
                    break   # this clause is true. check next clause
            else:
                return False

        return True

    def simplify(self, model):
        """
        Simplifies the sentence as possible taking into account a given model.
        Clauses that are true with the model are removed. Symbols that are false
        according to the model are removed from the clauses.

        Args:
            model: The model the sentence will simplified against.

        Returns:

        """
        for clause in copy(self):
            new_clause = set(clause)
            add_new = True
            for var in clause:
                if (var > 0 and model[var]) or (var < 0 and 
                        model[abs(var)] == False):
                    # this var makes the clause true. remove the clause
                    add_new = False
                    break
                elif model[abs(var)] != None:
                    # this var does not help making the clause true. remove the
                    # var from the clause
                    new_clause.remove(var)
            self.remove_clause(clause)
            if add_new:
                self.add_clause(new_clause)

        # TODO: remove supersets. here or in the beginning?

    def solve(self, solver):
        """
        Solves this sentence, using the specified solver class. By calling
        this method the setence is not affected.

        Args:
            solver: A solver object, which implements a run() method, which
            receives a sentence.

        Returns:
            The value returned by solver.run().
        """
        return solver.run(self.__deepcopy__())

    def __copy__(self):
        # TODO Test this
        new_kb = Sentence(self.nbvar)

        new_kb.clauses = copy(self.clauses)

        return new_kb

    def __deepcopy__(self, memo=None):
        new_kb = Sentence(self.nbvar)

        new_kb.clauses = deepcopy(self.clauses, memo)

        return new_kb

    def __iter__(self):
        self.__currclause = 0
        return self

    def __next__(self):
        if self.__currclause < len(self.clauses):
            tmp = self.clauses[self.__currclause]
            self.__currclause += 1
            return tmp
        else:
            raise StopIteration()

    def __len__(self):
        return len(self.clauses)

    def __str__(self):
        if len(self.clauses) == 0:
            return '""'

        s = ''

        for clause in self:
            s += str(clause)
            s += "and"

        return s[:-3]
