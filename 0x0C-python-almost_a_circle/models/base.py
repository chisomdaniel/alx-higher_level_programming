#!/usr/bin/python3
"""A python module that initialize a base class
"""


class Base():
    """The class

    Attributes:
        __nb_objects(class attribute, private, int)
        id (int, public)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

