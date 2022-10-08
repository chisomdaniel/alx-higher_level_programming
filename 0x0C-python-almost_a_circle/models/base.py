#!/usr/bin/python3
"""A python module that initialize a base class
"""
import json


class Base():
    """The class

    Attributes:
        __nb_objects(class attribute, private, int)
        id (int, public)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns the json string representation of
        a list of dictionaries passed as an argument
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)
