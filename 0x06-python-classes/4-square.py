#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines properties of square by: (based on 3-square.py).

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

    def set_size(self, value):
         """Property setter for size.

        Args:
            value (int): size of a square (1 side).

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if type(value) != int:
            raise Exception("size must be an integer")
        self.__size = value

    def get_size(self):
        """Returns the size of a square
        """
        return self.__size

    size = property(get_size, set_size)
