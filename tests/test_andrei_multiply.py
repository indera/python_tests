#!/usr/bin/env python

import unittest
from money import Money

class TestMoneyAndrei(unittest.TestCase):

    def test_multiply(self):
        money = Money(2)
        money.multiply(3)
        self.assertEqual(6, money.get_amount())

if __name__ == '__main__':
    unittest.main()
