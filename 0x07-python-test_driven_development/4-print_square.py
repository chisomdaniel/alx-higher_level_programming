#!/usr/bin/python3
"""Prints square with # if size (the arguments passed)

Arguments:
    size (int): the size of the circl

"""


def print_square(size):
    """size is the are of the square

    raises:
        TypeError
    """
    if type(size) != int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("{}".format("#"*size))
