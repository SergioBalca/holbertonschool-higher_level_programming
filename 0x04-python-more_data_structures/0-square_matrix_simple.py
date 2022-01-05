#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        matrix_copy = [list(map(lambda x: x ** 2, row)) for row in matrix]
        return matrix_copy

    return matrix
