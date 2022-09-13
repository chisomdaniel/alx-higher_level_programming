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

    @property
    def size(self):
        """size: `int` is retrived using the method
        and also set using it's setter method
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ A public method that returns area of the square"""
        return self.__size ** 2
