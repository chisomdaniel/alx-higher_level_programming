#!/usr/bin/python3
"""A class that does something"""


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
