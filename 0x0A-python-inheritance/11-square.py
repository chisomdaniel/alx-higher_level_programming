#!/usr/bin/python3
"""Inheriting a class from another class"""


class BaseGeometry(object):
    """Raises an exception"""
    def area(self):
        """a method to raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the type of the arguments passed"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Creats a rectangle class"""
    def __init__(self, width, height):
        """initialize the attributes"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Create a string representatio for the class"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

class Square(Rectangle):
    """Creates a square"""
    def __init__(self, size):
        """Validate the argument passed"""
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def area(self):
        """Find the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """the string representation of the class"""
        return "[Square] {}/{}".format(self.__size, self.__size)
