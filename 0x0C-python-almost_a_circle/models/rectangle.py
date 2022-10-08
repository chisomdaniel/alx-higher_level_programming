#!/usr/bin/python3
"""A rectangle class

This module creates a class named rectagle
that performs various function

"""
from models.base import Base


class Rectangle(Base):
    """ The rectangle class, this class inherits from
    the Base class in the ``base.py`` file

    Attributes:
        id (int, optional): inherited from the Base class
        width (int): the width of the rectangle
        height (int) : the rectangle height
        x (:obj:`int`, optional): the x position, defaults to 0
        y (:obj:`int`, optional): the y position, defaults to 0
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        the init method

        Args:
            id (int, optional): the method id, defaults to None
            width (int): the width of the rectangle
            height (int) : the rectangle height
            x (:obj:`int`, optional): the x position, defaults to 0
            y (:obj:`int`, optional): the y position, defaults to 0
        """
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """int: getter method for width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter method for width"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """int: getter method for the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter method for height"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """getter method for the x attribute"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter method for x"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """getter method for the y attribute"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter method for y"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Returns the area of the rectangle instance"""
        return self.__height * self.__width

    def display(self):
        """Prints the rectangle instance with the # character"""
        print("{}".format("\n"*self.__y), end="")
        for i in range(self.__height):
            print("{}{}".format(" "*self.__x, "#"*self.__width))

    def __str__(self):
        """the string representation of the class"""
        string = "[Rectangle] ({}) {}/{} - {}/{}"
        return string.format(self.id, self.__x, self.__y,
                             self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Updates the attributes of the class"""
        if len(args) == 0:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except Exception:
            return

    def to_dictionary(self):
        """Creates a dictionary of all the attributes"""
        new_dict = {}
        new_dict["id"] = self.id
        new_dict["width"] = self.width
        new_dict["height"] = self.height
        new_dict["x"] = self.x
        new_dict["y"] = self.y

        return new_dict
