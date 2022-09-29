#!/usr/bin/python3
"""checks if a class is the same as an object"""


def is_same_class(obj, a_class):
    """returns True if the same else False"""
    if type(obj) == a_class:
        return True
    else:
        False
