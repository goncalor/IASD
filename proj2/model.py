
class Model:
    """ Defines a model for the world.  """

    def __init__(self, nvars=0, values=[]):
        """
        Args:
            nvars: The number of variables in this world. If 'nvars' is
            specified, 'values' is not used.
            values: A list of values for the variables in this world. The
            variables should have values None, False or True.
        """
        if nvars:
            self.values = [None for i in range(nvars+1)]
        elif values:
            self.values = list([None] + values)
        else:
            raise Exception("Empty model")

    
    def flip(self, varnum):
        """
        Flips the value of a variable in the model. If no value has yet been
        assigned to that variable its new value will be True.
        
        Args:
            varnum: The number of the variable to flip.

        Returns:
            The new value of the flipped variable.
        """
        self.values[varnum] = not self.values[varnum]
        return self.values[varnum]


    def assign(self, varnum, val):
        """
        Assigns a value to a variable in the model.

        Args:
            varnum: The number of the variable that will be assigned.
            val: The new value for the assigned variable.
        """
        self.values[varnum] = val

    def __getitem__(self, key):
        return self.values[key]
    
    def __str__(self):
        return str(self.values)

