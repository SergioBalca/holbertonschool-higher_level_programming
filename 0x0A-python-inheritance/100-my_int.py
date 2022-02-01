#!/usr/bin/python3

""" Module with MyInt class defined """


class MyInt(int):
    

    """ method to define the reverse equality operator"""

    def __eq__(self, other):
        return int(self) != other

    """ method to define the reverse enequality operator """

    def __ne__(self, other):
        return int(self) == other
