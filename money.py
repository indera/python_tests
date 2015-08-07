from decimal import *
import json
import urllib2
import pprint


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

    def dollar_conversion(self, value=None, original=None, new=None):
        list_of_currencies = {'Argenitian Peso' : 'ARS', 'Australia Dollar' : 'AUD', 'Bitcoin' : 'BTC', 'Brazil Real' : 'BRL', 'Canada Dollar' : 'CAD', 'Chile Peso' : 'CLP',
                              'China Yuan Renminbi' : 'CNY', 'Czech Republic Koruna' : 'CZK', 'Denmark Krone' : 'DKK', 'Euro Member Countries' : 'EUR', 'Fiji Dollar':'FJD',
                              'Honduras Lempira' : 'HNL', 'Hong Kong Dollar' : 'HKD', 'Hungary Forint':'HUF','Iceland Krona':'ISK','India Rupee':'INR','Indonesia Rupiah':'IDR',
                              'Israel Shekel':'ILS','Japan Yen':'JPY','Korea (South) Won':'KRW','Malaysia Ringgit':'MYR','Mexico Peso':'MXN','New Zealand Dollar':'NZD',
                              'Norway Krone':'NOK','Pakistan Rupee':'PKR','Philippines Peso':'PSO','Poland Zloty':'PLN','Russia Ruble':'RUB','Singapore Dollar':'SGD',
                              'Sweden Krona':'SEK','Switzerland Franc':'CHF','Taiwan New Dollar':'TWD','Thailand Baht':'THB','Turkey Lira':'TRY','United Kingdom Pound':'GBP',
                              'United States Dollar':'USD','Viet Nam Dong':'VND'}

        pp = pprint.PrettyPrinter(indent=4)

        pp.pprint(list_of_currencies)

        if value == None:
            value = raw_input('Enter amount of money to convert: ')

        if original == None:
            original = raw_input('Enter home currency type (ex: USD, EUR, GBP): ')
            original = original.upper()

        if new == None:
            new = raw_input('Enter destination currency type (ex: USD, EUR, GBP): ')
            new = new.upper()

        json_dict = json.load(urllib2.urlopen('https://currency-api.appspot.com/api/%s/%s.json' % (original, new)))
        rate = json_dict['rate']
        self.foreign_currency = Decimal(value) * Decimal(rate)
        return self.foreign_currency