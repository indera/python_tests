
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

    def multiply(self, amt):
        count = 0
        answer = 0
        while count < amt:
            answer += self._amount
            count = count +1

        self._amount = answer

    def divide(self, amt):
        self._amount = self._amount / amt