class Checkbook(object):

    """ Sample checkbook object """
    def __init__(self, balance):
        self._balance = balance



    def get_balance(self):
        return self._balance


    def credit(self, amt):
        self._balance = self._balance + amt
