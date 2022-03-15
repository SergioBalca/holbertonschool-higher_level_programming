#!/usr/bin/python3

import json
import csv


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

    @classmethod
    def save_to_file(cls, list_objs):

        """ class method that writes the JSON string
            representation of list_obj to a file
        """
        list_dictionary = []
        if list_objs is None or len(list_objs) == 0:
            return []

        for obj in list_objs:
            list_dictionary.append(obj.to_dictionary())

        filename = cls.__name__ + ".json"
        with open(filename, mode='w', encoding='utf-8') as file:
            json_string = cls.to_json_string(list_dictionary)
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):

        """ static method that returns the list of the
            JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            empty_list = []
            return empty_list
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):

        """class method to create an instance from a dictionary"""
        if cls.__name__ == "Rectangle":
            dummy = cls(2, 2, 2, 2, 3)
        if cls.__name__ == "Square":
            dummy = cls(2, 2, 2, 3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file_csv(cls, list_objs):

        """ class method that serializes in CSV """

        if list_objs is None or len(list_objs) == 0:
            dict_list = []

        filename = cls.__name__ + ".csv"
        key_list = []
        dict_list = []
        values_list = []

        for obj in list_objs:
            dict_list.append(obj.to_dictionary())

        if cls.__name__ == "Rectangle":
            key_list = ['id', 'width', 'height', 'x', 'y']
        elif cls.__name__ == "Square":
            key_list = ['id', 'size', 'x', 'y']

        with open(filename, mode='w', encoding='utf-8', newline='') as file:
            CSV_writer = csv.writer(file)

            """to write the header row with attributes into CSV file"""
            CSV_writer.writerow(key_list)

            """to write the values of each attribute into CSV file"""
            for idx, obj in enumerate(dict_list):
                values_list = dict_list[idx].values()
                CSV_writer.writerow(values_list, )

        @classmethod
        def load_from_file_csv(cls):

            """class method that desearilizes a CSV file"""

            filename = cls.__name__ + ".csv"
