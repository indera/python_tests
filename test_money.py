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

    def test_divide(self):
        """ Verify that we can multiple a number to the class amount"""
        money = Money(4)
        money.divide(2)
        self.assertEqual(2, money.get_amount())

    def test_remainder(self):
        """ Verify that we can divide and get remainder"""
        money = Money(3)
        remainder = money.get_remainder(2)
        self.assertEqual(1, remainder)

    def test_converter(self):
        """ will the currency exchange work"""
        money = Money(10)
        conversion = money.converter()
        self.assertEqual(6.50, conversion) 

if __name__ == '__main__':
    unittest.main()