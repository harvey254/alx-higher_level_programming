#!/usr/bin/python3
"""Defines a class Student"""

class Student:
    """ representation of a student"""
    def __init__(self, first_name, last_name, age):
        """creates new instances the object"""
        self.first_name = firstname
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Public method that retrieves a dictionary representation of a Student instance
        """
        return self.__dict__
