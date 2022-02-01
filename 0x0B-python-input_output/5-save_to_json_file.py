#!/usr/bin/python3
""" importin JSON module"""
import json

""" module that contains the save_to_json_file function """


def save_to_json_file(my_obj, filename):

    """ writes an object to a text file,
        using a JSON representation
    """

    with open(filename, 'w') as json_file:
        return json.dump(my_obj, json_file)
