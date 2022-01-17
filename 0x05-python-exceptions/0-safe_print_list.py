#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    count = 0
    new_list = []

    try:
        for index in range(0, x):
            new_list.append(my_list[index])

        for element in new_list:
            count += 1
            print("{}".format(element), end="")

    except IndexError:
        for element in my_list:
            count += 1
            print("{}".format(element), end="")

    print()
    return count
