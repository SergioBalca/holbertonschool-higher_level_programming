#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        for k, v in sorted(list(a_dictionary.items())):
            print("{}: {}".format(k, v))
