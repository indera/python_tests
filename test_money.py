#!/usr/bin/env python

import unittest
from unittest import TestCase
from money import Money


class TestMoney(unittest.TestCase):
    def test_subtract(self):
        """ Verify that the subtract function works well"""
        money = Money(42)
        money.subtract(2)
        self.assertEqual(money.get_amount(), 40)

    def test_add(self):
        """ verify we can add a number to the class amount"""
        money = Money(1)
        money.add(2)
        self.assertEqual(3, money.get_amount())

    def test_multiply(self):
        """
        Verify that the multiply method of the Money class multiplies an amount by the first parameter
        """
        money = Money(25)
        money.multiply(3)
        self.assertEqual(money.get_amount(),75)

    def test_divide(self):
        """
        Verify that the divide method of the Money class divides the _amount property by the first parameter
        """
        money = Money(25)
        money.divide(5)
        self.assertEqual(money.get_amount(),5)

    def test_convert(self):
        """
        Verify that the method convert_currency in the money class produces the correct results
        """
        # Arrange for test
        rates = {
            "USD": 1.00,
            "EUR": 2.00,
            "GBP": 1.50
        }
        money = Money(30)
        money.currency = "USD"
        money.rates = rates

        # Act (run test)
        euros = money.convert("EUR")

        # Assert values
        self.assertAlmostEqual(euros, 60, places=2)


if __name__ == '__main__':
    unittest.main()
