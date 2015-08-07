import money

class Checkbook(money.Money):

    """ Sample checkbook object."""
    def __init__(self, balance):
        self._amount = balance

    def credit(self, amt):
        """ Adds the amount into your current balance. """
        self.add(amt)

    def debit(self, amt):
        """ Debits the given amount from your current balance """
        self.subtract(amt)

    def balance(self):
        """ Returns your current balance. """
        return self._amount