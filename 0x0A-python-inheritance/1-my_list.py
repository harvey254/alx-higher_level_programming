#!/usr/bin/python3
"""Defines a class MyList that inherits from the class list"""


class MyList(list):
    """Class that inherits from list """
    def __init__(self):
        """Initialize the object"""
        super().__init__()
        
    def print_sorted(self):
        """Prints a list in ascending order.
        """
        print(sorted(self))
