#!/usr/bin/env python

import unittest
from money import Money


class TestMoney(unittest.TestCase):

    def test_subtract(self):
        """ Verify that the subtract function works well"""
        money = Money(42)
        money.subtract(2)
        self.assertEqual(money.get_amount(), 40)

    def test_add(self):
    	""" Verify that we can add a number to the class amount"""
    	money = Money(1)
    	money.add(2)

    	self.assertEqual(3, money.get_amount())

    def test_nrejack_multiply(self):
    	""" Verify that we can multiply the class amount by a number"""
    	money = Money(10)
    	money.multiply(3)

    	self.assertEqual(30, money.get_amount())

    def test_nrejack_divide(self):
    	""" Verify that we can divide the class amount by a number"""
    	money = Money(666)
    	money.divide(3)

    	self.assertEqual(222, money.get_amount())

    def test_nrejack_remainder(self):
    	""" Verify that we can return a remainder after dividing the class amount by a number. """
    	money = Money(100)
    	expected_remainder = money.remainder(3)

    	self.assertEqual(expected_remainder, 1)

   	def test_nrejack_convert(self, target_currency):
   		money = Money(1000)
   		
   		# this is vacation.
   		# we're only concerned with whole units of currency
   		# no pocket change please
   		# except for loonies and toonies
   		
   		euros = 912
   		thai_baht = 35138
   		cad = 1313

   		expected_euros = money.convert('EUR')
   		expected_thai_baht = money.convert('THB')
   		expected_canadian_dollars = money.convert('CAD')

   		self.assertEqual(expected_euros, euros)
   		self.assertEqual(expected_thai_baht, thai_baht)
   		self.assertEqual(expected_canadian_dollars, cad)


if __name__ == '__main__':
    unittest.main()
