#!/usr/bin/python3

import json

"""module that has the Base class"""


class Base:

    """ Private class attribute """
    __nb_objects = 0

    def __init__(self, id=None):

        """ class constructor
            Args:
                id:     The id of the instance. if None
                        id will take the value of the
                        instance counter (__nb_objects)
        """
        if id is None:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
        else:
            self.id = id

    """ static method that returns the JSON representation of
        list_dictionaries
    """
    @staticmethod
    def to_json_string(list_dictionaries):

        """ static method that returns the JSON string representation
            of list_dictionaries
            Args:
                  list_dictinaries: a list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
