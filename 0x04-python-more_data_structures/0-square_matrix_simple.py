#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # new_list = [[j ** 2 for j in i] for i in matrix]

    another = [list(map(lambda x: x ** 2, i)) for i in matrix]

    return another
