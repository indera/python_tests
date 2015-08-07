
class Money(object):

    # Sample Money Object Instantiation
    def __init__(self, balance):
        self._amount = balance
        self._converted_amount = None
        self._remainder = None

    def get_conversion(self, symbol):
        if symbol == 'GRD':
            return 340.750

    # Accessor Methods for Class Variables
    def get_amount(self):
        return self._amount

    def get_converted_amount(self):
        return self._converted_amount

    def get_remainder(self):
        return self._remainder

    # Addition
    def add(self, amt):
        self._amount = self._amount + amt

    # Subtraction
    def subtract(self, amt):
        self._amount = self._amount - amt

    # Multiplication
    def multiply(self, amt):
        self._amount = self._amount * amt

    # Division
    def divide(self, amt):

        whole, decimals = divmod(self._amount, amt)
        self._remainder = decimals

        return whole

    # Conversion of one currency to another
    def convert(self, conversion_symbol):
        conversion_amount = self.get_conversion(conversion_symbol)
        self._converted_amount = self._amount * conversion_amount

