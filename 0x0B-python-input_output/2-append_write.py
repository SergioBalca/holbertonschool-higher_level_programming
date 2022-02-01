#!/usr/bin/python3

""" module that containts the append_write functions"""


def append_write(filename="", text=""):

    """ functions that appends a string at the end of a text file and
        returns the number of characters added

        Args:
            filenname: name of the file
            text: the text to be appended at the end of the file
    """

    with open(filename, mode='a', encoding='utf-8') as my_file:
        return my_file.write(text)
