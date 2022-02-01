#!/usr/bin/python3

""" importing JSON module """
import json

""" module that contains the to_json_string function """


def to_json_string(my_obj):

    """ Returns the JSON representation of an object,
        in this case a string.
        Args:
            my_obj: is a python object
    """
    return json.dumps(my_obj)
