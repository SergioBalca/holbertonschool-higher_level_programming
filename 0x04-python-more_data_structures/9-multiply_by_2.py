#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    k, v = a_dictionary.keys(), a_dictionary.values()
    new_dictionary = dict(map(lambda k, v: (k, v * 2), k, v))
    return new_dictionary
