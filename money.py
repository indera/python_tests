
class Money(object):

    """ Sample money object """
    def __init__(self, balance):
        self._amount = balance

    def subtract(self, amt):
        if self._amount < amt:
            raise Exception("Not enough money")

        self._amount = self._amount - amt

    def get_amount(self):
        return self._amount

    def add(self, amt):
        self._amount = self._amount + amt

    def multiply(self, amt):
        self._amount *= amt

    def divide(self, amt):
        self._amount /= amt

    def get_division_remainder(self, div):
        res = self._amount % div
        return res

    def convert_to(self, to='EUR'):
        rates = {
            'EUR': 0.9116,  # Euro
            'MDL': 0.0523,  # Moldavian Leu
            'ISK': 0.0074,  # Icelandic Krona
            'BIT': 0.01  # bit coin
        }

        return round(self._amount/rates[to], 2)

    def convert_to_isk(self):
        return self.convert_to('ISK')

    def convert_to_eur(self):
        return self.convert_to('EUR')

    def convert_to_mdl(self):
        return self.convert_to('MDL')

    def convert_to_bit(self):
        return self.convert_to('BIT')
