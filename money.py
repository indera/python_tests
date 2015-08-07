from decimal import *
import json
import urllib2


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

    def dollar_conversion(self):
        original = input('Enter home currency type (ex: USD, EUR, GBP): ')
        new = input('Enter destination currency type (ex: USD, EUR, GBP): ')
        json_dict = json.load(urllib2.urlopen('https://currency-api.appspot.com/api/%s/%s.json' % (original, new)))
        rate = json_dict['rate']
        self.foreign_currency = Decimal(self._amount) * Decimal(rate)
        return self.foreign_currency