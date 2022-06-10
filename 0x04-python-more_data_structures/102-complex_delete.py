#!/usr/bin/python3
"""Module that contains def complex_delete function"""


def complex_delete(a_dictionary, value):
    """Deletes keys with a specific value in a dictionary"""
    key_list = []
    if value in a_dictionary.values():
        for k, v in a_dictionary.items():
            if v == value:
                key_list.append(k)
        for item in key_list:
            a_dictionary.pop(item)
    return a_dictionary
