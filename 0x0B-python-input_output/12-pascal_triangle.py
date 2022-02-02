#!/usr/bin/python3

""" this module contains the pascal_triangle function """


def pascal_triangle(n):

    """ Returns a list of lists of intengers representing
        the Pascal's triangle of n.
        Args:
            n: is a positive integer that represents the number
               of the triangle
    """

    pascal_list = []

    if n <= 0:
        return pascal_list

    for i in range(n):
        pascal_list.append([])
        pascal_list[i].append(1)
        for j in range(1, i):
            ap = pascal_list[i - 1][j - 1] + pascal_list[i - 1][j]
            pascal_list[i].append(ap)

        if n != 0:
            pascal_list[i].append(1)
    return pascal_list
