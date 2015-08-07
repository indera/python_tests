#!/usr/bin/env python

import unittest
from money import Money


class TestMoney(unittest.TestCase):

    # Addition
    def test_add(self):

        money = Money(1)
        money.add(2)

        self.assertEqual(3, money.get_amount())

    # Substraction
    def test_subtract(self):
        money = Money(42)
        money.subtract(2)

        self.assertEqual(40, money.get_amount())

    # Multiplication
    def test_multiply(self):

        money = Money(8)
        money.multiply(8)

        self.assertEqual(64, money.get_amount())

    # Division
    def test_divide(self):
        money = Money(64)

        self.assertEqual(8, money.divide(8))

    # Division with remainder
    def test_divide_with_remainder(self):
        money = Money(100)

        self.assertEqual(12, money.divide(8))
        self.assertEqual(4, money.get_remainder())

    # Convert currency types GRD
    def test_convert_currency_GRD(self):
        money = Money(1500)
        money.convert('GRD')
        self.assertEqual(511125, money.get_converted_amount())

    # Convert currency types GRP
    def test_convert_currency_GRP(self):
        money = Money(1500)
        money.convert('GBP')
        self.assertEqual(975.0000000000000333066907388, money.get_converted_amount())

if __name__ == '__main__':
    unittest.main()
