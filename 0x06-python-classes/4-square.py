#!/usr/bin/python3

"""Class Square defined"""

class Square:

    """Model of Square class"""

    def __init__(self, size=0):

        """Constructor with size as argument.
        where size is the size of the square.
        """

        """if size is not an integer, the exception
        TYpeError is raised.
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")

        """if size is not greater that 0,
        the ValueError exception is raised.
        """

        if size < 0:
            raise ValueError("size must be >= 0")

        self.size = size

    """property to retraive size"""

    @property
    def size(self):
        return self.__size

    """setter to set the value of square size"""

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        
        if value < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = value

    """public instance method that returns the area of
    current square.
    """

    def area(self):
        return self.__size ** 2

