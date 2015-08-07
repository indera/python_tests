#!/usr/bin/env python

import unittest
from checkbook import Checkbook
from money import Money


class TestCheckbook(unittest.TestCase):

    def test_balance(self):
        checkbook = Checkbook(Money(100))
        self.assertEqual(100, checkbook.get_balance())

    def test_credit(self):
        checkbook = Checkbook(Money(100))
        checkbook.credit(Money(50))
        self.assertEqual(100, checkbook.get_starting_balance())
        self.assertEqual(150, checkbook.get_balance())

    def test_debit(self):
        checkbook = Checkbook(Money(100))
        checkbook.debit(Money(200))
        self.assertEqual(-100, checkbook.get_balance())


if __name__ == '__main__':
    unittest.main()
