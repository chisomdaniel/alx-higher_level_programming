#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    length = len(my_list)
    new_list = []

    if idx < 0 or idx >= length:
        return my_list

    for i in my_list:
        new_list.append(i)

    new_list[idx] = element

    return new_list
