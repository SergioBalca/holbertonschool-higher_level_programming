#!/usr/bin/python3

"""Class Rectangle definition"""


class Rectangle:

    """Model of a Rectangle"""

    def __init__(self, width=0, height=0):

        """__init__ method for the Rectangle class
        Arguments:
        width: integer that defines the width of rectangle
        height: integer that defines the height of rectangle
        """

        self.width = width
        self.height = height

    """property to retrieve width of the rectangle"""

    @property
    def width(self):
        return self.__width

    """property to set the value of width of the rectangle"""

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    """property to retreive height of the rectangle"""

    @property
    def height(self):
        return self.__height

    """property to set the value of height of rectangle"""

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
