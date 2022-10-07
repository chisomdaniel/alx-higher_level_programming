#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
"""Test file for the rectangle class"""


class Testbaseclass(unittest.TestCase):
    """The test class"""
    def test_id(self):
        """testing the inheritance"""
        
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r1 = Rectangle(2, 10)
        self.assertEqual(r1.id, 2)

        r2 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r2.id, 12)

    def test_exception(self):
        self.assertRaises(TypeError, Rectangle, (10, "2"))
