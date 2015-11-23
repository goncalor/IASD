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
        :param cnf_sentence: CNF clause in a tuple.
        :return: Nothing.
        """
        #if len(cnf_sentence) == 0:
        #    print("ERROR: Sentence add_clause -> can't add an empty clause")
        if not isinstance(cnf_sentence, tuple):
            print("ERROR: Sentence add_clause -> cnf_sentence must be a tuple")

        for i in range(len(cnf_sentence)):
            if not isinstance(cnf_sentence[i], int):
                print("ERROR: Sentence add_clause -> only int type tuples allowed")

            if abs(cnf_sentence[i]) > self.nbvar:
                print("ERROR: Sentence add_clause -> trying to add" +
                        cnf_sentence[i] + "variable, there are only" +
                        self.nbvar + "variables")

            if cnf_sentence[i] == 0:
                print("ERROR: Sentence add_clause -> 0 clause not allowed")

        self.__insert(cnf_sentence)


    def __insert(self, cnf_sentence, index=None):
        """
        Private method for inserting in list
        :param cnf_sentence:
        :return: ---
        """
        if index is None:
            self.clauses.append(cnf_sentence)
        else:
            self.clauses.insert(index, cnf_sentence)

    def remove_clauses(self, clause):
        """
        Removes all clauses equal to the argument provided.
        :param clause: Clause to eliminate in CNF tuple.
        :return: Nothing.
        """
        if not isinstance(clause, tuple):
            print('ERROR: Sentence remove_clauses -> clause must be tuple')

        old_size = len(self)

        self.clauses = list(filter(clause.__ne__, self.clauses))

        return len(self) < old_size

    def remove_clause(self, clause):
        """
        Removes the clause provided in the argument. If clause is a tuple, it
        searches and deletes it. If clause is an integer, deletes the clause in
        that index.
        :param clause: Either a CNF tuple or an integer.
        :return: If the argument is a tuple, returns true or false if clause is removed or not. If the argument is an
                    integer returns the removed CNF tuple.
        """
        if isinstance(clause, tuple):
            clause_set = set(clause)
            for cl in self.clauses:
                if clause_set == set(cl):
                    self.clauses.remove(cl)
                    return True

            return False

        if isinstance(clause, int):
            return self.clauses.pop(clause)

        else:
            print('ERROR: Sentence remove_clause -> clause must be either an int or a tuple')

    def get_clause(self, index):
        """
        Returns the clause in the given index.
        :param index: Index of the clause, must be an integer.
        :return: CNF tuple.
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
                clause = self.remove_clause(clause_index)
                new_clause = [var for var in clause if var != variable]
                new_clause = tuple(new_clause)
                self.clauses.insert(clause_index, new_clause)

    def unit_variables(self):
        """
        Returns all unit variables in the knowledge base. Negation (-) is included
        :return: List of CNF tuples.
        """
        units = list()

        for clause in self.clauses:
            if len(clause) == 1:
                units.append(clause[0])

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
            for var in clause:
                if var == -symbol:
                    return False

        return True

    def pure_symbols(self):
        """
        Returns a list with all the pure symbols in the sentence. Negative
        values represent the negation of the a symbol.
        """
        findings = [None] * (self.nbvar+1)
        pure = [None] * (self.nbvar+1)

        for clause in self:
            for var in clause:
                if findings[abs(var)] == None:  # first time found
                    findings[abs(var)] = var
                    pure[abs(var)] = True
                elif pure[abs(var)] and (findings[abs(var)] + var == 0):
                    pure[abs(var)] = False  # not pure

        return [symbol for symbol in findings if symbol and pure[abs(symbol)]]

    def __remove_var_from_clause(self, variable, clause):
        """
        Removes the variable from the clause. If the variable is negated, the argument must be negated and vice-versa.
        Clause might be either a clause or an index. If it is a clause it will check the first clause in knowledge base
        that match this one. If clause is an integer it will check if a clause in given index. Returns true if removed.
        :param variable: Integer.
        :param clause: Tuple of integers.
        :return: Boolean.
        """
        if isinstance(clause, tuple):
            clause_set = set(clause)
            for clause_index in range(len(self.clauses)):
                if clause_set == set(self.clauses[clause_index]) and variable in self.clauses[clause_index]:

                    removed_clause = self.remove_clause(clause_index)
                    new_clause = [var for var in removed_clause if var != variable]
                    new_clause = tuple(new_clause)
                    #print('var', variable, 'clause', removed_clause, 'new_clause', new_clause)
                    self.__insert(new_clause, clause_index)

                    if len(new_clause) < len(clause):
                        return new_clause
                    else:
                        return clause

        """
        for clause_index in range(len(self.clauses)):
            if clause == self.clauses[clause_index]:
                poped_clause = self.clauses.pop(clause_index)
                new_clause = [var for var in poped_clause if var != variable]
                new_clause = tuple(new_clause)
                #self.__insert(new_clause, clause_index)
                self.clauses.insert(clause_index, new_clause)

                if len(new_clause) < len(poped_clause):
                    return True
                else:
                    return False
        """
        if isinstance(clause, int):
            clause_index = clause
            clause = self.remove_clause(clause_index)
            new_clause = [var for var in clause if var != variable]
            new_clause = tuple(new_clause)
            self.__insert(new_clause, clause_index)
            if len(new_clause) < len(clause):
                return True
            else:
                return False



    @staticmethod
    def __is_subset(subclause, clause):
        """
        If subclause is a subset of clause, returns true
        :param subclause: CNF tuple.
        :param clause: CNF tuple.
        :return: Boolean.
        """
        if not isinstance(subclause, tuple) or not isinstance(clause, tuple):
            print('ERROR: Sentence is_subset -> subclause and clause must be tuples')

        return frozenset(subclause) <= frozenset(clause)

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
                if (var > 0 and model[abs(var)]) or (var < 0 and
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
        """
        for clause in copy(self):
            new_clause = list(clause)
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
                self.add_clause(tuple(new_clause))
        """

        for clause in copy(self.clauses):
            already_removed = False
            new_clause = list(clause)
            for var in new_clause:
                if (var > 0 and model[abs(var)] == True) or (var < 0 and model[abs(var)] == False):
                    # clause is true
                    #print('removi clause', var, clause)
                    if not already_removed:
                        self.remove_clause(clause)
                    else:
                        self.remove_clause(cl)
                    break
                elif (var < 0 and model[abs(var)] == True) or (var > 0 and model[abs(var)] == False) and var in clause:
                    #model[abs(var)] != None and var in clause:
                    #print('removi var', var, clause)
                    if not already_removed:
                        cl = self.__remove_var_from_clause(var, clause)
                        already_removed = True
                    else:
                        cl = self.__remove_var_from_clause(var, cl)
        """
        # debug
        for clause in self.clauses:
            for var in clause:
                if model[abs(var)] != None:
                    print(self.clauses)
                    print(model.values)
                    exit()
        #
        """

        #self.__remove_supersets()

    def __remove_supersets(self):
        """ Removes clauses that are supersets of other clauses. """
        laux = []

        for clause_index in range(len(self)):
            for clause_index2 in range(clause_index+1, len(self)):
                if frozenset(self.clauses[clause_index]) <= frozenset(self.clauses[clause_index2]):
                    laux.append(self.clauses[clause_index2])

        for clause in laux:
            self.remove_clause(clause)

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

        new_kb.clauses = list(self.clauses)

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
