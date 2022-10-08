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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json string representation of
        a list of dictionaries passed as an argument
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a json representation of an array of instances"""
        if list_objs is None or len(list_objs) == 0:
            filename = cls.__name__
            filename += ".json"
            with open(filename, 'w') as fd:
                fd.write("[]")
            return

        filename = list_objs[0].__class__.__name__
        filename += ".json"

        list_dict = [i.to_dictionary() for i in list_objs]
        j_string = cls.to_json_string(list_dict)
        with open(filename, 'w') as fd:
            fd.write(j_string)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []

        with open("jsonfile.txt", 'w') as f:
            f.write(json_string)
        with open("jsonfile.txt", 'r') as f:
            my_dict = json.load(f)

        return my_dict
