#!/usr/bin/python3
"""Module that contains roman_to_int function"""

romans = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }


def roman_to_int(roman_string):
    """function that converts Roman numerals to integer values"""
    int_value = 0

    if type(roman_string) is not str or roman_string == None:
        return 0

    for count, roman in enumerate(roman_string):
        n1 = romans[roman_string[count]]
        if count + 1 < len(roman_string):
            n2 = romans[roman_string[count + 1]]
            if n1 >= n2:
                int_value += n1
            else:
                int_value -= n1
        else:
            int_value += n1
    return int_value
