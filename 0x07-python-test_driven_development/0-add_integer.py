#!/usr/bin/python3
"""  How to use this script

This module contains a function to add
two integers and return the sum

check out the test file in ``tests/0-add_integer.txt``

"""


def add_integer(a: int, b: int = 98) -> int:
    """Adds two integers and return the sum

    Args:
        a (int): the first number
        b (int, optional): the second number, defaults to 98
          if only one argument is passed

    Return:
        returns the sum of the two arguments

    Raises:
        TypeError: if type a or b is not an int or float

    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
