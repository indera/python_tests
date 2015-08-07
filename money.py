
class Money(object):

    """ Sample money object """
    def __init__(self, balance):
        self._amount = balance
        self.foreign_currency = 0

    def subtract(self, amt):
        self._amount = self._amount - amt

    def get_amount(self):
        return self._amount

    def get_foreign_currency(self):
        return self.foreign_currency

    def add(self, amt):
        self._amount = self._amount + amt

    def multiply(self, amt):
        count = 0
        answer = 0
        while count < amt:
            answer += self._amount
            count = count +1
        self._amount = answer

    def divide(self, amt):
        self._amount = self._amount / amt

    def remainder(self, amt):
        remainder = self._amount % amt
        return remainder

    def dollar_conversion(self, rate):
        self.foreign_currency = self._amount * rate
        return self.foreign_currency