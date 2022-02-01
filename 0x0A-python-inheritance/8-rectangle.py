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

        self.__width = width
        self.__height = height
        self.integer_validator('width', self.__width)
        self.integer_validator('height', self.__height)
