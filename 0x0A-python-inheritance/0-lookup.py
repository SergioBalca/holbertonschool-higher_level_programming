#!/usr/bin/python3

""" function that returns the list of available
    attributes and methods of an object
"""


def lookup(obj):
    
    """ Returns a list of attributes.
        Args:
            obj: is an object
    """
    return dir(obj)
