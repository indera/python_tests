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
        """
        verify that we can add a number to the class amount
        """
        money = Money(1)
        money.add(2)
        self.assertEqual(3, money.get_amount())
>>>>>>> e51a4edd0f65455cc690e1aeddfac257cb469a06

    def test_atloiaco_mulitply(self):
        money = Money(2)
        money.multiply(2)
        self.assertEqual(1,1)

    def test_nrejack_multiply(self):
    	""" Verify that we can multiply the class amount by a number"""
    	money = Money(10)
    	money.multiply(3)

    	self.assertEqual(30, money.get_amount())

     def test_taeber_multiple(self):
        # Better have my money!
        money = Money(3)
        money.multiply(2)
        self.assertEqual(money.get_amount(), 6)
        money.multiply(1.0/6)
        self.assertEqual(money.get_amount(), 1)

if __name__ == '__main__':
    unittest.main()
