#!/usr/bin/python3
"""This file contain a test python class

It has no attribute or obje

"""


class Square:
    """This class defines a square

    Attributes:
        size (private): is the size of the square.

    """

    def __init__(self, size=0):

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
