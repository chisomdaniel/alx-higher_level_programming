#!/usr/bin/python3
"""Diving deeper into the usage of python classes"""

class Rectangle:
    """A class that does nothing"""
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
