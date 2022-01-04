#!/usr/bin/env python3
def no_c(my_string):
    no_c_string = ''.join([my_string[i] for i in range(len(my_string)) if my_string[i] != 'c' and my_string[i] != 'C'])
    return no_c_string
