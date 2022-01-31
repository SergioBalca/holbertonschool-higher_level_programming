#!/usr/bin/python3

""" function that returns True if if
    the object is exactly an instance
    of the specified class
"""


def is_same_class(obj, a_class):

    """ Return True if the object
        is an instance of the class
        Args:
            obj: the object
            a_class: a class
    """

    if type(obj) is a_class:
        return True
    else:
        return False
