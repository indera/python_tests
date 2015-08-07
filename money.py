
class Money(object):

    """ Sample money object """
    def __init__(self, balance):
        self._amount = balance

    def subtract(self, amt):
        self._amount = self._amount - amt

    def add(self, amt):
        self._amount = self._amount + amt    

    def get_amount(self):
        return self._amount
