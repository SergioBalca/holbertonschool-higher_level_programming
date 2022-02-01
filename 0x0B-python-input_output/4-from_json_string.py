#!/usr/bin/python3

"""importing the JSON module"""
import json

""" module that contains the from_json_string function """


def from_json_string(my_str):

    """ Returns an object represented by a JSON string
        Args:
            my_str: is a JSON string to deserialize
    """

    return json.loads(my_str)
