#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    dictionary = sorted(list(a_dictionary))
    for i in dictionary:
        print("{}: {}".format(i, a_dictionary[i]))
