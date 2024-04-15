#!/usr/bin/python3
"""Defines a class MyList that inherits from the class list"""


class MyList(list):
    """Class that inherits from list.

    Args:
        list: an array to sort in ascending order.
    """
    def print_sorted(self):
        """Prints a list in ascending order.
        """
        self.sort()
        print(self)
