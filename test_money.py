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
        """ Verify that the add function works well"""
        money = Money(42)
        money.add(2)
        self.assertEqual(money.get_amount(), 44)

    def test_multiply(self):
        """ Verify that the multiply function works well"""
        money = Money(3)
        money.multiply(10)
        self.assertEqual(money.get_amount(), 30)

    def test_remainder(self):
        money = Money(4)
        remainder = money.remainder(3)
        self.assertEqual(remainder, 1)

    def test_conversion_to_inr(self):
        money = Money(100)
        rupees = money.convert(MockUsdToInrConverter())
        self.assertEquals(rupees, 5000)


class MockUsdToInrConverter(object):
    def convert(self, amount):
        return amount * 50


if __name__ == '__main__':
    unittest.main()
