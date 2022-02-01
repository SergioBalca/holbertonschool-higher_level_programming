#!/usr/bin/python3

""" functions that returns True if the object is an instance
    of a class that inherited from a specified class
"""


def inherits_from(obj, a_class):
    """ Args:
            obj: is an object
            a_class: the specified class
    """

    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
