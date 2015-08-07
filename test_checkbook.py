#!/usr/bin/env python

import unittest
from checkbook import Checkbook


class TestCheckbook(unittest.TestCase):

    def test_mbuchholz_credit(self):
        checkbook = Checkbook(1000)
        checkbook.credit(100)
        self.assertEqual(1100, checkbook.get_balance())
















if __name__ == '__main__':
    unittest.main()
