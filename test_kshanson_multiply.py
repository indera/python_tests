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

    def test_multiply(self):
        """ Verify that we can multiple a number to the class amount"""
        money = Money(2)
        money.multiply(3)
        self.assertEqual(6, money.get_amount())

if __name__ == '__main__':
    unittest.main()