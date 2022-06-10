#!/usr/bin/python3
"""Module that contains weight_average function"""


def weight_average(my_list=[]):
    """Returns the weighted average of all integers tuple"""
    avg = 0
    num = 0
    den = 0

    if len(my_list) == 0:
        return 0

    for tup in my_list:
        score = tup[0]
        weight = tup[1]
        num += score * weight
        den += weight
    avg = num / den
    return avg
