
class Money(object):

    """ Sample money object """
    def __init__(self, balance):
        self._amount = balance

    def subtract(self, amt):
        self._amount = self._amount - amt

    def get_amount(self):
        return self._amount

    def add(self, amt):
    	self._amount = self._amount + amt

    def multiply(self,amt):
    	self._amount = self._amount * amt

