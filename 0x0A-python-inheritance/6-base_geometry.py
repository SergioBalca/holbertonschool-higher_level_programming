#!/usr/bin/python3

""" Module with the BaseGeometry class """


class BaseGeometry:

    """ BaseGeometry is an empty class"""

    def ___init___(self):
        pass

    """ public instance method that raises
        an exception
    """

    def area(self):
        raise Exception("area() is not implemented")
