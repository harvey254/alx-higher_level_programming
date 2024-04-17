#!/usr/bin/python3
"""Defines a class Square"""


class Square:
     """
    Class that defines properties of square by: (based on 2-square.py).

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

    def area(self):
         """Calculates the area of square.

        Returns: the current square area.
        """
        return (self.__size * self.__size)
