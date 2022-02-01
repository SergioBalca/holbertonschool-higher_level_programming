#!/usr/bin/python3

""" module that contains a functions that
    reads a file and prints it in stdout
"""


def read_file(filename=""):

    """ Prints in stdout the content of a file
        Args:
            filename: is the name of the file
    """

    with open(filename, mode='r', encoding='utf-8') as my_file:
        print(my_file.read(), end="")
