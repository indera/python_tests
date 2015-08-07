#!/usr/bin/env python

import unittest
from money import Money
from checkbook import Checkbook


class TestCheckbook(unittest.TestCase):

  def test_credit(self):
    checkbook = Checkbook(1000)
    checkbook_expected_balance = 1100

    checkbook.credit(100)

    self.assertEqual(checkbook.balance(), checkbook_expected_balance)

  def test_debit(self):
    checkbook = Checkbook(1000)
    checkbook_expected_balance = 900

    checkbook.debit(100)

    self.assertEqual(checkbook.balance(), checkbook_expected_balance)

  def test_balance(self):
    checkbook = Checkbook(1000)
    checkbook_expected_balance = 1000

    self.assertEqual(checkbook.balance(), checkbook_expected_balance)

     
if __name__ == '__main__':
    unittest.main()
