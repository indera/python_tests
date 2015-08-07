#!/usr/bin/env python

import unittest
from money import Money


class TestMoney(unittest.TestCase):
    def test_asura_multiply(self):
        money = Money(2)
        money.multiply(3)
        self.assertEqual(6, money.get_amount())

    def test_subtract(self):
        """ Verify that the subtract function works well """
        money = Money(42)
        money.subtract(2)
        self.assertEqual(money.get_amount(), 40)

    def test_add(self):
        """ Verify that we can add a number to the class amount """

        money = Money(1)
        money.add(2)
        self.assertEqual(3, money.get_amount())


    def test_mbuchholz_multipy(self):
        """Verify that we can multiply numbers"""
        money = Money(10)
        money.multiply(2)
        self.assertEqual(20, money.get_amount())

    def test_mbuchholz_divide(self):
        """Verify that we can divide numbers"""
        money = Money(10)
        money.divide(2)
        self.assertEqual(5, money.get_amount())

    def test_mbuchholz_remainder(self):
        """Verify that we can get the remainder of a number"""
        money = Money(10)
        money.remainder(3)
        self.assertEqual(1, money.get_remainder())

    def test_mbuchholz_converter(self):
        """Verify we can return a currency converted"""
        money = Money(2)
        money.converter(.91)
        self.assertEqual(1.82, money.get_converter())
        




if __name__ == '__main__':
    unittest.main()
