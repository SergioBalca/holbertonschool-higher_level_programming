#!/usr/bin/python3

""" module that has the rectagle class """

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

    @property
    def width(self):

        "property for retrieve width instance"
        return self.__width

    @width.setter
    def width(self, value):

        """setter to set the width value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """property to retrieve height instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter to set the height valule"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """property to retrieve x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter to retrieve x value"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """property to retrieve y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter to set the y value"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """public method that returns a Rectangle area"""
        return self.__width * self.__height

    def display(self):
        """public method that prints in stdout
        the Rectangle instance with #
        """
        rect = "\n" * self.__y
        for y in range(self.__height):
            posx = " " * self.__x
            rect += posx + "#" * self.__width + "\n"
        print(rect, end="")
        return rect

    def __str__(self):
        """__str__ method is used to print a rectangle instance"""
        return "[{}] ({}) {}/{} - {}/{}".format(
            __class__.__name__, self.id, self.__x,
            self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """public method that assigns an argument to each attribute"""

        if len(args) != 0:
            attr_list = ["id", "width", "height", "x", "y"]
            for key, value in zip(attr_list, args):
                setattr(self, key, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):

        """ public method that returns the dictionary
            representation of a Rectangle
        """
        key_list = ['id', 'width', 'height', 'x', 'y']
        value_list = []
        for key in key_list:
            value_list.append(getattr(self, key))
        return dict(zip(key_list, value_list))
