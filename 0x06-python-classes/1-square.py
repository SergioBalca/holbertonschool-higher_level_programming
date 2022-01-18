#!/usr/bin/python3
"""Class Square definition"""


class Square:
    """Model of class Square"""

    def __init__(self, size):
        """Constructor for Square Method
        size: is the size of the square
        the argument size is made private
        by adding two __ before the instance size
        """
        self.__size = size
