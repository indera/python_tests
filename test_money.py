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

if __name__ == '__main__':
    unittest.main()
