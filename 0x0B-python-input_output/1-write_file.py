#!/usr/bin/python3

""" module that contains the write_file function
"""


def write_file(filename="", text=""):

    """ Function that writes a string to a text file
        and returns the number of characters written.

        Args:
            filename: name of the file
            text: the text to be writtern into the file
    """

    with open(filename, mode='w', encoding='utf-8') as my_file:
        return my_file.write(text)
