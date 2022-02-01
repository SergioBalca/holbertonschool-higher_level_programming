#!/usr/bin/python3

""" Module that has the Square class """


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):

    """ Inherited from Rectangle class """

    def __init__(self, size):

        """ constructor for square object """

        super().integer_validator("size", size)
        super().__init__(size, size)
