#!/usr/bin/env python

import unittest
from money import Money

class TestMoneyAndrei(unittest.TestCase):

    def test_multiply(self):
        money = Money(2)
        money.multiply(3)
        self.assertEqual(6, money.get_amount())

    def test_add(self):
        money = Money(12.5)
        money.add(1.0/2)
        self.assertEquals(13, money.get_amount())

    def test_divide(self):
        money = Money(1.0)
        money.divide(2)
        self.assertEquals(0.5, money.get_amount())

        """
        money2 = Money(0.0)
        money2.divide(0)
        self.assertRaises(ZeroDivisionError)
        """


    def test_get_division_remainder(self):
        money = Money(10)
        self.assertEquals(1.0, money.get_division_remainder(3))

    def test_convert_currency(self):
        money = Money(100)
        self.assertEquals(109.70, money.convert_to_eur())
        self.assertEquals(1912.05, money.convert_to_mdl())
        self.assertEquals(13513.51, money.convert_to_isk())


if __name__ == '__main__':
    unittest.main()
