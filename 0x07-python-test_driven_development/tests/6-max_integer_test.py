#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Writing unit tests for the max_integer function"""
    def test_empty(self):
        """test with an empty list"""
        self.assertAlmostEqual(max_integer([]), None)

    def test_list(self):
        """Test using a list"""
        self.assertAlmostEqual(max_integer([2]), 2)
        self.assertAlmostEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertAlmostEqual(max_integer([5, 2, 3, 1]), 5)
