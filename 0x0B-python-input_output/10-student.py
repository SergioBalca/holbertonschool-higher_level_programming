#!/usr/bin/python3

""" this module contains the definition of class Student """


class Student:

    """ Student class """

    def __init__(self, first_name, last_name, age):

        """ constructor to initialize public instances:
            first_name
            last_name
            age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """ public method that retrives a dictionary representation
        of a student instance
    """

    def to_json(self, attrs=None):
        attributes = {}
        if type(attrs) is list:
            for i in attrs:
                if i in self.__dict__:
                    attributes[i] = self.__dict__[i]
            return attributes
        return self.__dict__
