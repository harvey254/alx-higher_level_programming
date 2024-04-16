#!/usr/bin/python3
"""save_to_json_file function"""

import json

def save_to_json_file(my_obj, filename):
    """a function that creates an Object from a “JSON file”"""
    with open(filename, 'r', encoding='utf-8') as file:
        create_object = json.load(file)
        return create_object

