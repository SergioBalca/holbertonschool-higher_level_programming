#!/usr/bin/python3
"""Class Square defined"""


class Square:
    """Model of Square class"""

    def __init__(self, size=0):

        """Constructor with size as argument,
        where size is the size of the square.
        """

        """if size is not an integer, the
        TypeError exception is raised.
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")

        """size must be greater than 0,
        otherwise the ValueError is raised.
        """

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Public instance method that returns the area of
        current square.
        """

        return self.__size ** 2
