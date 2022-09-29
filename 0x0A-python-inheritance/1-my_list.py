#!/usr/bin/python3
"""This list inherits from the list object and expands its function"""


class MyList(list):
    """The sub-class"""
    def print_sorted(self):
        """prints a sorted arrangement of the list"""
        new_list = sorted(self)

        print(new_list)
