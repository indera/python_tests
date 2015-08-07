from money import Money

class Checkbook(object):
    def __init__(self, starting_balance=None):
        self.starting_balance = starting_balance or Money(0)
        self.balance = Money(starting_balance.get_amount())

    def get_balance(self):
        return self.balance.get_amount()

    def get_starting_balance(self):
        return self.starting_balance.get_amount()

    def credit(self, amount):
        self.balance.add(amount.get_amount())

    def debit(self, amount):
        self.balance.subtract(amount.get_amount())
