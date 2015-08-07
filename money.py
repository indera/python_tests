
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

    def multiply(self,amt):
    	self._amount = self._amount * amt

    def divide(self, amt):
    	self._amount = self._amount / amt

    def remainder(self, amt):
    	""" Returns the remainder after dividing the balance with the given number"""
    	return self._amount % amt

    def convert(self, target_currency):
    	""" Returns the balance converted into a new currency """
    	conversion_factor_dict = {
			'USD' : 1,
			'EUR' : 0.911847,
			'THB' : 35.1375,
			'CAD' : 1.31298
			}
	return self._amount * conversion_factor_dict[target_currency]