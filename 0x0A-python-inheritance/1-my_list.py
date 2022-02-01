#!/usr/bin/python3

""" Class Mylist defined, that inherits from
    list
"""


class MyList(list):

    """ public instance method that prints the list
        in ascending sort
    """

    def print_sorted(self):
        alist = []
        for item in self:
            alist.append(item)  # to add an element to the list
        alist.sort()    # to sort the list in ascending order
        print(alist)
