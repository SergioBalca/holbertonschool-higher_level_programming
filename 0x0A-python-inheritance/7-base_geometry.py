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

    """ public instance method that validates value
        assuming name is always a string
    """

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
