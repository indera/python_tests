
class Money(object):

    """ Sample money object """
    def __init__(self, balance):
        self._amount = balance
        self._remainder = 0
        self._conversion = 0

    def subtract(self, amt):
        self._amount = self._amount - amt

    def add(self, amt):
        self._amount = self._amount + amt

    def multiply(self, amt):
        self._amount = self._amount * amt

    def divide(self, amt):
        self._amount = self._amount / amt

    def remainder(self,amt):
        self._remainder = self._amount % amt

    def convert(self,conversionRate):
        self._conversion = self._amount / conversionRate
        self._conversion = round(self._conversion,2)

    def get_amount(self):
        return self._amount

    def get_remainder(self):
        return self._remainder

    def get_conversion(self):
        return self._conversion
