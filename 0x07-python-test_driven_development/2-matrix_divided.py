#!/usr/bin/python3
"""How to use the ``matrix_divided`` function

Argument:
    matrix: the matrixs to be passed
    div: what to divide with

Return:
    the new matrix

"""


def matrix_divided(matrix, div):
    if (not isinstance(matrix, list) or
            not all([type(i) == list for i in matrix])):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    if not all(
            [all(map(lambda x: type(x) in (int, float), i)) for i in matrix]):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    length = len(matrix[0])
    if not all([True if len(i) == length else False for i in matrix]):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_list = [list(map(lambda x: round(x / div, 2), i)) for i in matrix]

    return new_list
