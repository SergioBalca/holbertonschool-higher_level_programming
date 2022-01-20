#!/usr/bin/python3

"""Class Square defined"""


class Square:

    """Model of Square class"""

    def __init__(self, size=0):

        """Constructor with size as argument.
        where size is the size of the square.
        """

        self.__size = size

    """property to retraive size"""

    @property
    def size(self):
        return self.__size

    """setter to set the value of square size"""

    @size.setter
    def size(self, value):
        if type(value) is not int or type(value) is not float:
            raise TypeError("size must be a number")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    """public instance method that returns the area of
    current square.
    """

    def area(self):
        return self.__size ** 2

    """special method to define equality operator"""

    def __eq__(self, other):
        return self.__size == other.__size

    """special method to define inequality operator"""

    def __ne__(self, other):
        return self.__size != other.__size

    """special method to define greater than operator"""

    def __gt__(self, other):
        return self.__size > other.__size

    """spacial method to define less than operator"""

    def __lt__(self, other):
        return self.__size < other.__size

    """special method to define greater that or equal operator"""

    def __ge__(self, other):
        return self.__size >= other.__size

    """spacial method to define less that or equal operartor"""

    def __le__(self, other):
        return self.__size <= other.__size
