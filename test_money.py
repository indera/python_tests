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

    def test_atloiaco_mulitply(self):
        money = Money(2)
        money.multiply(2)
        self.assertEqual(money.get_amount(), 4)

    	
if __name__ == '__main__':
    unittest.main()
