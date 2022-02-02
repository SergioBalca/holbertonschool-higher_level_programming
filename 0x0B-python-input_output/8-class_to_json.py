#!/usr/bin/python3

""" this module contains the class_to_json function """
import json


def class_to_json(obj):

    """ Returns the dictionary description with simple data structure
        for JSON serialization of an objet
    """

    return obj.__dict__
