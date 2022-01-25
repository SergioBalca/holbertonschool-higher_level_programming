#!/usr/bin/python3

"""This module divides all elements of a matrix"""


def matrix_divided(matrix, div):

    """Return a new matrix with all elements divided by a number div
    (int or float) and rounded to 2 decimal places.

    Arguments: matrix must be a list of lists, containg int or float values
               and with all rows of the same lenght.
               div: a number (int or float) and different from 0
    """

    msg0 = "matrix must be a matrix (list of lists) of integers/floats"
    msg1 = "Each row of the matrix must have the same size"

    """div must be an int or float and must be greater that 0"""

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0 or div == float('-inf'):
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    row_length = 0

    """Each row of the matrix must be a list of int of float values"""

    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(msg0)
    if type(matrix[0]) is list:
        row_length = len(matrix[0])

    for row in range(len(matrix)):
        if type(matrix[row]) is not list:
            raise TypeError(msg0)
        if len(matrix[row]) != row_length:
            raise TypeError(msg1)
        else:
            new_row = []
            for column in range(row_length):
                if type(matrix[row][column]) not in [int, float]:
                    raise TypeError(msg0)
                new_row.append(round(matrix[row][column] / div, 2))

            new_matrix.append(new_row)

    return new_matrix
