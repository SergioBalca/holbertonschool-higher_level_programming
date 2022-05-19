#!/usr/bin/python3
"""Module with find_peak function"""


def find_peak(list_of_integers):
    """ function that finds a peak in a
        list of unsorted integers
    """
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[len(list_of_integers) - 1]
    else:
        return None
