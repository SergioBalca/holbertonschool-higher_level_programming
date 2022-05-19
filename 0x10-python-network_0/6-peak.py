#!/usr/bin/python3
"""Module with find_peak function"""

def find_peak(list_of_integers):
    """ function that finds a peak in a
        list of unsorted integers
    """
    if list_of_integers:
        return max(list_of_integers)
    else:
        return None

