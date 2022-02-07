#!/usr/bin/python3

""" module that has the rectagle class """

from cmath import rect
from models.base import Base

"""Rectangle class inherits from Base class"""

class Rectangle(Base):

    """ Rectangle class that inherits from Base class.
        Args:
            width:  width of the rectangle
            height: height of the rectangle
            x:
     """
    def __init__(self, width, height, x=0, y=0, id=None):

        """contructor for Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    "property for retrieve width instance"
    @property
    def width(self):
        return self.__width

    """setter to set the width value"""
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    """property to retrieve height instance"""
    @property
    def height(self):
        return self.__height

    """setter to set the height valule"""
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    """property to retrieve x value"""
    @property
    def x(self):
        return self.__x

    """setter to retrieve x value"""
    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    """property to retrieve y value"""
    @property
    def y(self):
        return self.__y

    """setter to set the y value"""
    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.__width * self.__height

    """public method that prints in stdout
        the Rectangle instance with #
    """

    def display(self):
        rect = "\n" * self.__y
        for y in range(self.__height):
            posx = " " * self.__x
            rect += posx + "#" * self.__width + "\n"
        print(rect, end="")
        return rect

    """__str__ method is used to print a rectangle instance"""

    def __str__(self):
        return "[{}] ({}) {}/{} - {}/{}".format(
            __class__.__name__, self.id, self.__x,
            self.__y, self.__width, self.__height
        )
