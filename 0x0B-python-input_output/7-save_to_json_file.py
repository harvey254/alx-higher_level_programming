#!/usr/bin/python3
"""a script that adds all arguments to a Python list, and then save them to a file"""

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = 'add_item.json'
my_list = []
try:
    my_list = load_from_json_file(filename)
except Exception:
    save_to_json_file(my_list, filename)

arg_length = len(argv)

if arg_length > 1:
    for i in range(1, arg_length):
        my_list.append(argv[i])

    save_to_json_file(my_list, filename)
