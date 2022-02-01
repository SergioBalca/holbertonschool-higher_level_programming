#!/usr/bin/python3

""" Module that has the Rectangle class """


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):

    """ Inherited from BaseGeometry class """

    def __init__(self, width, height):

        """ Constructor for Rectangle

            Args:
                widht: width of the rectangle
                height: height of the rectangle
        """

        BaseGeometry.integer_validator(self, "width", width)
        self.__width = width
        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height

    """ method that returns the area of a rectangle """

    def area(self):
        return self.__width * self.__height

    """ __str__ method to print a rectangle description """

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
