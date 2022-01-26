#!/usr/bin/python3

"""Module to define a class LockedClass"""


class LockedClass:

    """prevents the creation of new instances
    other than first_name"""

    __slots__ = ['first_name']
