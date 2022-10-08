#!/usr/bin/python3
"""A square class module that inherits from
a rectangle class.

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The sqaure class, inherits from the Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the sqaure class

        Inherits all the same argument and attribute
        from the rectangle class
        """
        Rectangle.__init__(self, size, size, x, y, id)
        self.size = size

    def __str__(self):
        """the string representation of the class"""
        string = "[Square] ({}) {}/{} - {}"
        return string.format(self.id, self.x, self.y,
                             self.width)
    @property
    def size(self):
        """getter method for the size"""
        return self.__width

    @size.setter
    def size(self, num):
        """Setter method for width"""
        if type(num) != int:
            raise TypeError("width must be an integer")
        if num <= 0:
            raise ValueError("width must be > 0")
        self.__width = num
        self.__height = num
