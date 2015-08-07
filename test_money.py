#!/usr/bin/env python

import unittest
from money import Money


class TestMoney(unittest.TestCase):

    def test_subtract(self):
        """ Verify that the subtract function works well """
        money = Money(42)
        money.subtract(2)
        self.assertEqual(money.get_amount(), 40)

    def test_add(self):
        """ Verify that the add function works """
        money = Money(1)
        money.add(2)

        self.assertEqual(3, money.get_amount())




    def test_cpb_multiply(self):
    	""" Verify that we can multiply """
    	money = Money(16)
    	money.multiply(12)

    	self.assertEqual(192, money.get_amount())

    def test_cpb_divide(self):
        """ Verify that we can divide """
        money = Money(8)
        money.divide(4)

        self.assertEqual(2, money.get_amount())



if __name__ == '__main__':
    unittest.main()
