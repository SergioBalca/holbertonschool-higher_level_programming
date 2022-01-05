#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is not None:
        result = set(my_list)
        return sum(result)
