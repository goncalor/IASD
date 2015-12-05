

class BNParser:
    """
    A Bayesian network input file parser.

    Assumptions:
        - VAR definition always comes before its CPT (conditional probability
          table)
        - In CPT definitions 'var' always comes before 'table'
    """

    def __init__(self, f):
        """
        Args:
            f: a file object that is already opened.
        """
        self.parsed = {}
        self.file_ = f


    def parse(self):
        """
        Parses the file, obtaining all information from it and reporting
        errors if the file is malformed.
        """
        line = self.file_.readline()
        while line != '':
            line = self.__prepare_line(line)
            print(line)

            if not line:    # empty line
                line = self.file_.readline()
                continue    # parse next line

            if line.lower() == "var":
                print('call var')
                self.__parse_var()
            elif line.lower() == 'cpt':
                print('call cpt')
                self.__parse_cpt()
            else:
                print(line)
                raise Exception("unexpected line '" + line + "'")

            line = self.file_.readline()


    def __parse_var(self):
        """
        Parses a VAR, starting at the line following a 'VAR' line.

        Raises:
            Many malformed file errors.
        """
        name = ''
        alias = ''
        parents = []
        values = []
        cpt = {}

        prev_line_pos = self.file_.tell()   # save current file position
        line = self.file_.readline()
        while line != '':
            line = self.__prepare_line(line)
            print(line)

            if not line:    # empty line
                line = self.file_.readline()
                continue    # parse next line

            line = line.split()
            keyword = line[0].lower()
            if keyword == 'name':
                if len(line) != 2:
                    raise Exception('unexpected number of values for parameter '
                            'name')
                if name:
                    raise Exception("redefinition of a variables's name: '" +
                            name + "' --> '" + line[1] + "'")
                if line[1] in self.parsed:
                    raise Exception("redefinition of variable '" + line[1] + "'")
                name = line[1]
            elif keyword == 'values':
                values = [x.lower() for x in line[1:]]
            elif keyword == 'alias':
                if len(line) != 2:
                    raise Exception('unexpected number of values for parameter '
                            'alias')
                alias = line[1]
            elif keyword == 'parents':
                if len(line) == 1:
                    raise Exception('unexpected number of values for parameter '
                            'parents')
                parents = line[1:]
            else:
                if not (name and values):   # these are mandatory
                    raise Exception('name or values missing in VAR definition')

                # save the parsed information
                self.parsed[name] = {'alias': alias, 'parents': parents,
                        'values': values, 'cpt': cpt}

                # create an alias for the name
                if alias:
                    if alias in self.parsed:
                        raise Exception("alias '" + alias + "' already exists")

                    self.parsed[alias] = self.parsed[name]

                # undo last readline(). needed so that self.parse() continues on
                # the correct line, instead of skipping the current line that
                # was read by self._parse_var() "by mistake"
                self.file_.seek(prev_line_pos)
                return

            prev_line_pos = self.file_.tell()   # save current file position
            line = self.file_.readline()    # advance position by one line


    def __parse_cpt(self):
        """
        Parses a CPT, starting at the line following a 'CPT' line.

        Raises:
            Many malformed file errors.
        """
        var = ''
        table = {}

        prev_line_pos = self.file_.tell()   # save current file position
        line = self.file_.readline()
        while line != '':
            line = self.__prepare_line(line)
            print(line)

            if not line:    # empty line
                line = self.file_.readline()
                continue    # parse next line

            line = line.split()
            keyword = line[0].lower()
            if keyword == 'var':
                if len(line) != 2:
                    raise Exception('unexpected number of values for parameter '
                            'var')
                if line[1] not in self.parsed:
                    raise Exception("undefined reference to variable '" +
                            line[1] + "'")
                var = line[1]
            elif keyword == 'table':
                if not var:
                    raise Exception("missing 'var' definition before 'table' "
                    "definition in CPT")
                print('call table')
                table = self.__parse_table(var, line)
                self.parsed[var]['cpt'] = table
            else:
                if not (var and table):
                    raise

                # undo last readline(). needed so that self.parse() continues on
                # the correct line, instead of skipping the current line that
                # was read by self._parse_var() "by mistake"
                self.file_.seek(prev_line_pos)
                return

            prev_line_pos = self.file_.tell()   # save current file position
            line = self.file_.readline()    # advance position by one line


    def __parse_table(self, varname, firstline):
        """
        Parses a 'table', starting at the line where the 'table' keyword is.

        Args:
            varname: the variable name this table refers to.
            firstline: the stripped and splited contents of the first line in
                the table definition.

        Returns:
            A dictionary with the probabilities for each case.

        Raises:
            Many malformed file errors.
        """
        table = {}
        lst = []

        # calculate the number of rows the table must have to be complete
        expected_nr_rows = len(self.parsed[varname]['values'])
        for parent in self.parsed[varname]['parents']:
            expected_nr_rows *= len(self.parsed[parent]['values'])

        # expected number of items is (nr parents + 1 (variable itself) + 1
        # (probability of this combination)) * nr rows
        items_per_row = len(self.parsed[varname]['parents']) + 2
        expected_nr_items = items_per_row * expected_nr_rows

        # process the first line if needed
        lst.extend(firstline[1:])

        # process lines
        if len(lst) == expected_nr_items:
            # all items found. check validity
            return self.__check_table(var, lst, items_per_row)
        elif len(lst) > expected_nr_items:
            raise Exception('problematic table in CPT')

        prev_line_pos = self.file_.tell()   # save current file position
        line = self.file_.readline()
        while line != '':
            line = self.__prepare_line(line)
            print(line)

            if not line:    # empty line
                line = self.file_.readline()
                continue    # parse next line

            line = line.split()
            lst.extend(line)

            if len(lst) == expected_nr_items:
                # all items found. check validity
                return self.__check_table(var, lst, items_per_row)
            elif len(lst) > expected_nr_items:
                raise Exception('problematic table in CPT')

            prev_line_pos = self.file_.tell()   # save current file position
            line = self.file_.readline()    # advance position by one line


    def __check_table(self, var, lst, items_per_row):
        """
        Checks if a table is valid. Builds a representation for it.

        Args:
            var: the variable this table refers to.
            lst: a list representing the table. This list is built by
                __parse_table().
            items_per_row: the number of items in a row of the table.

        Returns:
            A dictionary representing the table.

        Raises:
            Many malformed file errors.
        """
        table = {}
        for chunk in self.__chunk(lst, items_per_row):
            print(chunk)
            try:
                chunk[-1] = float(chunk[-1])
            except ValueError:
                raise Exception('problematic table in CPT: invalid probability')

            # TODO: build table and check values are in the domains

        return table


    def __chunk(self, l, n):
        """ Yield successive n-sized chunks from a list. """
        for i in range(0, len(l), n):
            yield l[i:i+n]


    def __prepare_line(self, line):
        """ Remove leading and trailing whitespaces and comments. """
        line = line.strip()    # remove leading and trailing whitespace
        line = line.split('#', 1)[0]    # remove comments
        return line


class QueryParser:

    def __init__(self):
        pass

