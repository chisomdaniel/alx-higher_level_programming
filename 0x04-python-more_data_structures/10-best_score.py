#!/usr/bin/python3

def best_score(a_dictionary):

    if a_dictionary == None or not a_dictionary:
        return None

    highest = max(list(a_dictionary.values()))

    for i, j in a_dictionary.items():
        if j == highest:
            return i

    return None
