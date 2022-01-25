#!/usr/bin/python3

"""This module add 2 integers or floats"""


def add_integer(a, b=98):

    """Return the sum of a + b
    Args: a: integer or float
          b: integer or float"""

    """if a or b are floats they are casted into int"""

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    """if a or b are not int, the TypeError exception is raised"""

    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    if a == a + 1:
        msg = "cannot convert float infinity to integer"
        raise OverflowError("msg")
    if b == b + 1:
        raise OverflowError("msg")

    sum = a + b
    return sum
