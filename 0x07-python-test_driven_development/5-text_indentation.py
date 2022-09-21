#!/usr/bin/python3
"""A module that parses and print a string

Function: text_indentation

"""
def text_indentation(text):
    """The function to print the string

    Arguments:
        text (str): the string to parse
    """

    if type(text) != str:
        raise TypeError("text must be a string")

    split = False
    for i in text:
        if i in (".", ":", "?"):
            print(i)
            print("")
            split = True
            continue
        if split and i in (" ", "\t"):
            continue
        else:
            split = False
        print(i, end="")
