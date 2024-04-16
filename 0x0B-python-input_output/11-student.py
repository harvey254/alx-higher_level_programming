#!/usr/bin/python3
"""Defines Student class"""


class Student:
    """ Representation of student"""
    def __init__(self, first_name, last_name, age):
        """ creates instances of student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dictionary with filter."""
        if type(attrs) is list and all([type(x) == str for k in attrs]):
            return {i: u for i, u in self.__dict__.items() if i in attrs}
        else:
            return self.__dict__.copy()

    def reload_from_json(self, json):
        """Loads attributes from json."""
        for key, value in json.items():
            self.__dict__[key] = value
