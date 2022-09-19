#!/usr/bin/python3
"""Diving deeper into the usage of python classes"""


class Rectangle:
    """A class that creates a rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """returns the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter property for the width, must be an int and >= 0"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter property for the height, height must be an int and >= 0"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returns the area of the perimeter

        if ``width`` of ``height`` is equal to 0,
        perimeter is equal to 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__width + self.__height)

    def __str__(self):
        char = ""
        if self.width == 0 or self.height == 0:
            return char
        for i in range(self.__height):
            char += "{}".format("#"*self.__width)
            if i != self.__height - 1:
                char += "\n"
        return char

    def __repr__(self):
        """returns a string representation of the rectangle 
        to be able to recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
