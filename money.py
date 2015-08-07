
class Money(object):

    """ Sample money object """
    def __init__(self, balance):
        self._amount = balance

    def subtract(self, amt):
        self._amount = self._amount - amt

    def add(self, amt):
        self._amount = self._amount + amt

    def multiply(self, factor):
        self._amount = self._amount * factor

    def divide(self, factor):
        self._amount = self._amount / factor

    def convert(self, currency):
        converted = self._amount * (self.rates[currency]/self.rates[self.currency])
        return(converted)

    def get_amount(self):
        return self._amount
