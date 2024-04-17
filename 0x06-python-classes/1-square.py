#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines properties of a square

    Attributes:
    size: size of square

    """
    __size = None
    

    def __init__(self, size=None):
        """
        creates a new instance of square

        Args:
        size:size of square

        """
        self.__size = size
