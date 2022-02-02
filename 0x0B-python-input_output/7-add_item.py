#!/usr/bin/python3
"""importing JSON module and sys module """
import json
import sys

""" This module contains a script that loads a json file into a
    python list and this list is save in a file
"""

""" From 5-save_to_json_file module import save_to_json_file """

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

""" From 6-load _from_json_file module import load_from_json_file """

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

the_file = "add_item.json"

try:
    my_list = load_from_json_file(the_file)
except Exception:
    my_list = []

for argument in sys.argv[1:]:
    my_list.append(argument)
save_to_json_file(my_list, the_file)
