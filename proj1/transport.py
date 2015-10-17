__author__ = 'henrique'


class Transport:

    # C come back, I forgive, I need typedf enum
    __trans_dictionary= {'autocarro' : 0, 'aviao' : 1, 'barco' : 2, 'comboio' : 3}  #from name to number
    __trans_invDictionary= {0 : 'autocarro', 1 : 'aviao', 2 : 'barco', 3 : 'comboio'}                 #from number to name

    def __init__(self, trans_name):
        """
        :param trans_name: string with the transport name: autocarro, aviao, barco, comboio
        :return:
        """

        if trans_name not in Transport.__trans_dictionary:
            print('ERROR-> Transport constructor: unkown transport', trans_name)
            return

        self.trans= Transport.__trans_dictionary[trans_name]

    def transDescription(self):
        return Transport.__trans_invDictionary[self.trans] + ':' + str(self.trans)

    def __eq__(self, other):

        if not isinstance(other, Transport):
            return False

        if self.trans == other.trans:
            return True
        else:
            return False

    def __str__(self):
        return Transport.__trans_invDictionary[self.trans]

    def __repr__(self):
        return Transport.__trans_invDictionary[self.trans]
