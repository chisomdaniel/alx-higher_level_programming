#!/usr/bin/python3
import unittest
from models.base import Base
"""Test files for the Base class
"""


class Testbaseclass(unittest.TestCase):
    """The main class"""

    def test_id(self):
        """test the base class"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b1 = Base()
        self.assertEqual(b1.id, 3)
        b1 = Base(12)
        self.assertEqual(b1.id, 12)
        b1 = Base()
        self.assertEqual(b1.id, 4)
