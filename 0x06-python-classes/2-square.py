#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines properties of square by

    Attributes:
    size: size of a square (1 side).
              """
    __size = None

    def __init__(self, size=0):
         """Creates new instances of square.

        Args:
            size: size of the square (1 side).
        """
        self.__size = size
        
        if type(size) != int:
            raise Exception("size must be an integer")
        if size < 0:
            raise Exception("size must be >= 0")
