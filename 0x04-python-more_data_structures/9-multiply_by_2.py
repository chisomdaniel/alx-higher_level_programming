#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    new_dic = {i: j * 2 for i, j in a_dictionary.items()}

    return new_dic
