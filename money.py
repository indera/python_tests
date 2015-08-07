
class Money(object):

    """ Sample money object """
    def __init__(self, balance):
        self._amount = balance
        self._remainder = 0
        self._converter = .91
        
    def subtract(self, amt):
        self._amount = self._amount - amt

    def add(self, amt):
        self._amount = self._amount + amt    

    def get_amount(self):
        return self._amount

    def get_remainder(self):
        return self._remainder

    def get_converter(self):
        return self._converter

    def add(self, amt):
        self._amount = self._amount + amt

    def multiply(self, amt):
        self._amount = self._amount * amt

    def divide(self, amt):
        self._amount = self._amount / amt

    def remainder(self, amt):
        self._remainder = self._amount % amt

    def converter(self, amt):
        self._converter = self._amount * amt
        
