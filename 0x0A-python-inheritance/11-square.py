#!/usr/bin/python3

""" Module that has the Square class """


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):

    """ Inherited from Rectangle class """

    def __init__(self, size):

        """ constructor for square object """

        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    """ __str__ method to return a square description """

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
