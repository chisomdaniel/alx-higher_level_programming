#!/usr/bin/python3

def search_replace(my_list, search, replace):

    length = len(my_list)

    if search >= length:
        return my_list

    new_list = my_list.copy()
    new_list[search - 1] = replace

    return new_list
