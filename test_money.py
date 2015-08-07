#!/usr/bin/env python

import unittest
from money import Money


class TestMoney(unittest.TestCase):

    def test_subtract(self):
        """ Verify that the subtract function works well """
        money = Money(42)
        money.subtract(2)

        self.assertEqual(40, money.get_amount())

        self.assertEqual(money.get_amount(), 40)

    def test_add(self):
        """ Verify that we can add a number to the class amount"""
        money = Money(1)
        money.add(2)
        self.assertEqual(3, money.get_amount())
        
    def test_cavedivr_multiply(self):
        """ Verify that we can multiply a number by the class amount"""
        money = Money(29)
        money.multiply(2)
        self.assertEqual(58, money.get_amount())
        
    def test_cavedivr_divide(self):
        """ Verify that we can divide a number by the class amount"""
        money = Money(28)
        money.divide(4)
        self.assertEqual(7, money.get_amount())
    
if __name__ == '__main__':
    unittest.main()
