#!/usr/bin/python3
"""This file contain a test python class

It has no attribute or obje

"""


class Square:
    """This class defines a square

    Attributes:
        size (private): is the size of the square.
        position (private): the position it should be printed

    """

    def __init__(self, size=0, position=(0, 0)):
        self.position = position

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

    @property
    def position(self):
        """position: `tuple`, represents the coordinate
        to follow when printing the square
        """
        return self.__postion

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """Represents the square with the # symbol"""
        if self.__size == 0:
            print("")
            return
        print("{}".format("\n"*self.__position[1]), end="")
        for i in range(self.__size):
            print("{}{}".format(" "*self.__position[0], "#"*self.__size))
