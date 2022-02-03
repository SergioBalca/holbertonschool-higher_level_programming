#!/usr/bin/python3

""" module that contains the append_after function """


def append_after(filename="", search_string="", new_string=""):

    """ inserts a line of text, after each line containing
        a specific string
    """

    with open(filename, mode='r', encoding='utf-8') as _file:
        file_lines = _file.readlines()

    with open(filename, mode='w', encoding='utf-8') as _file:
        for i in range(len(lines)):
            if search_string in file_lines[i]:
                file_lines[i] += new_string
        _file.writelines(file_lines)
