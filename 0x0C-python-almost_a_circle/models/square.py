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

    def __str__(self):
        """the string representation of the class"""
        string = "[Square] ({}) {}/{} - {}"
        return string.format(self.id, self.__x, self.__y,
                             self.__width)
