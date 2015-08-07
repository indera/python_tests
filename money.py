
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
<<<<<<< HEAD
        
    def multiply(self, amt):
        self._amount = self._amount * amt
=======
>>>>>>> fae5bfa99a80a6b0cdc9e2956faa7f1838f0bea3
