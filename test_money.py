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
        """ Verify that the subtract function works well"""
        money = Money(42)
        money.add(2)
        self.assertEqual(money.get_amount(), 44)

    def test_taeber_multiple(self):
        money = Money(3)
        money.multiply(2)
        self.assertEqual(money.get_amount(), 6)
        money.multiply(1.0/6)
        self.assertEqual(money.get_amount(), 1)


if __name__ == '__main__':
    unittest.main()
