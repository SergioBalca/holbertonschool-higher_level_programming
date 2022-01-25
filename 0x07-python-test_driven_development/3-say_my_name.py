#!/usr/bin/python3

"""function that prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):

    """Return first_name and last_name
    Arguments:
              first_name: a string
              last_name: a string
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
