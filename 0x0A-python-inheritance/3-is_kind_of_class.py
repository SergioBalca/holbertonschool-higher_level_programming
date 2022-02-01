#!/usr/bin/python3

""" functions that returns True if the object
    is an instance of, or if the object is
    an instance of a subclass. Otherwise
    return False
"""


def is_kind_of_class(obj, a_class):

    """ Return True if obj is an instance
        of a_class or if is an instance of
        a subclass
    """

    return isinstance(obj, a_class)
