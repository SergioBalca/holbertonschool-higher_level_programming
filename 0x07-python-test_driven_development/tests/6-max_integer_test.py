#!/usr/bin/python3
import unittest

"""Module to perform tests using the unittest module
"""

max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        
        """All tests are passeble by the function max_integer
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([10, 12, 13, 2, 3]), 13)
        self.assertEqual(max_integer([-4, -3, -2, -1,]), -1)
        self.assertEqual(max_integer([-2, 1, 2, 3]), 3)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([]), None)




