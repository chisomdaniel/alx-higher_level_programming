#!/usr/bin/python3
"""returns the available attribute and methods of an object"""


def lookup(obj):
    """returns a list of attribute and methods"""
    lst = dir(obj)

    return lst
