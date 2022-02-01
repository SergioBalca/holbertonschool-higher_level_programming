#!/usr/bin/python3

""" importing JSON module """
import json

""" module that contains the load_from_json_file function """


def load_from_json_file(filename):

    """ creates an Object from a JSON file
        Args:
            filename: the JSON file
    """

    with open(filename) as read_file:
        return json.load(read_file)
