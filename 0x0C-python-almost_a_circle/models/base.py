#!/usr/bin/python3
"""A python module that initialize a base class
"""
import json
import csv


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

        my_dict = json.loads(json_string)

        return my_dict

    @classmethod
    def create(cls, **dictionary):
        '''Returns an instance of a class with all attribute already set'''
        class_name = cls.__name__
        if class_name == 'Rectangle':
            inst = cls(1, 2, id=1)
        elif class_name == 'Square':
            inst = cls(1, id=1)

        inst.update(**dictionary)

        return inst

    @classmethod
    def load_from_file(cls):
        '''Returns a list of instance'''
        filename = cls.__name__ + '.json'

        try:
            with open(filename, 'r') as f:
                class_str = f.read()
            dict_list = cls.from_json_string(class_str)
            class_list = [cls.create(**i) for i in dict_list]

            return class_list
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        if list_objs is None or len(list_objs) == 0:
            return

        filename = cls.__name__ + '.csv'

        with open(filename, 'w', newline='') as csvfile:
            fieldnames = list_objs[0].to_dictionary().keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + '.csv'

        try:
            with open(filename, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                obj_list = []
                for row in reader:
                    for i, j in row.items():
                        row[i] = int(j)
                    obj_list.append(cls.create(**row))

            return obj_list
        except FileNotFoundError:
            return []
