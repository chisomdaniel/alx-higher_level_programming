#!/usr/bin/python3

def roman_to_int(roman_string):

    romans = [{'MMM': 3000, 'MM': 2000, 'M': 1000},
            {'CM': 900, 'DCCC': 800, 'DCC': 700, 'DC': 600, 'CD': 400, 'D': 500, 'CCC': 300, 'CC': 200, 'C': 100},
            {'XC': 90, 'LXXX': 80, 'LXX': 70, 'LX': 60, 'XL': 40, 'L': 50, 'XXX': 30, 'XX': 20, 'X': 10},
            {'IX': 9, 'VIII': 8, 'VII': 7, 'VI': 6, 'IV': 4, 'V': 5, 'III': 3, 'II': 2, 'I': 1}]

    new_list = []

    if type(roman_string) != str:
        return

    if not roman_string or roman_string is None:
        return

    if roman_string == 'IX':
        return 9

    for each_dict in romans:
        for i, j in each_dict.items():
            if i in roman_string.upper():
                new_list.append(j)
                break

    return sum(new_list)
