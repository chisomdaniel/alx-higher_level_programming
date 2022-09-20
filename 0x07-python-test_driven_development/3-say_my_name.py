#!/usr/bin/python3
"""This function prints the first name and last name of a user

Argument:
    first_name (str): the first name
    last_name (str): the last name

"""


def say_my_name(first_name, last_name=""):
    """Print the first and last name of a user

    raise:
        TypeError: name must not be a string

    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
