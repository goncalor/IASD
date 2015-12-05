

class BNParser:
    """
    A Bayesian network input file parser.

    Assumptions:
        - VAR definition always comes before its CPT (conditional probability
          table)
    """

    def __init__(self, f):
        """
        Args:
            f: a file object that is already opened
        """
        self.parsed = {}
        self.file_ = f


    def parse(self):
        """
        Parses the file, obtaining all information from it and reporting
        erros if the file is malformed.
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
        Starts parsing a VAR, starting at the line following a 'VAR' line.
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
                    raise Exception('unexpected number of values for parameter'
                            'name')
                if name:
                    raise Exception("redefinition of a variables's name: '" +
                            name + "' --> '" + line[1] + "'")
                if line[1] in self.parsed:
                    raise Exception("redefinition of variable '" + line[1] + "'")
                name = line[1]
            elif keyword == 'values':
                values = line[1:]
            elif keyword == 'alias':
                if len(line) != 2:
                    raise Exception('unexpected number of values for parameter'
                            'alias')
                alias = line[1]
            elif keyword == 'parents':
                if len(line) == 1:
                    raise Exception('unexpected number of values for parameter'
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
        Starts parsing a CPT, starting at the line following a 'CPT' line.
        """
        var = ''

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
                    raise Exception('unexpected number of values for parameter'
                            'var')
                if line[1] not in self.parsed:
                    raise Exception("undefined reference to variable '" +
                            line[1] + "'")
                var = line[1]
            elif keyword == 'table':
                pass
            else:
                raise

                # undo last readline(). needed so that self.parse() continues on
                # the correct line, instead of skipping the current line that
                # was read by self._parse_var() "by mistake"
                self.file_.seek(prev_line_pos)
                return

            prev_line_pos = self.file_.tell()   # save current file position
            line = self.file_.readline()    # advance position by one line


    def __prepare_line(self, line):
        """ Remove leading and trailing whitespaces and comments. """
        line = line.strip()    # remove leading and trailing whitespace
        line = line.split('#', 1)[0]    # remove comments
        return line


class QueryParser:

    def __init__(self):
        pass
