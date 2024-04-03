#!/usr/bin/python3
"""Defines a class Square"""
class Square:
     """
    Class that defines properties of square by: (based on 5-square.py).

    Attributes:
        size: size of a square (1 side).
        position: position of square
    """
    __size = None
    __position = None

    def __init__(self, size=0, position=(0, 0)):
        """Creates new instances of square.

        Args:
            __size (int): size of the square (1 side).
            __position (tuple): position of the square.
        """
        self.__size = size
        if type(size) != int:
            raise Exception("size must be an integer")
        if size < 0:
            raise Exception("size must be >= 0")
        if (type(position[0]) != int or type(position[1]) != int):
            raise Exception("position must be a tuple of 2 positive integers")
        if len(position) != 2 or type(position) != tuple:
            raise Exception("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise Exception("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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
            TypeError: size must be an integer.
            ValueError: size must be >= 0.
        """
        if type(value) != int:
            raise Exception("size must be an integer")
        self.__size = value

    def get_size(self):
        """Returns the size of a square
        """
        return self.__size

    size = property(get_size, set_size)

    def set_position(self, value):
        """Property setter for position.

        Args:
            value (tuple): position of the square.

        Raises:
            TypeError: position must be a tuple of 2 positive integers
        """
        if (type(value[0]) != int or type(value[1]) != int):
            raise Exception("position must be a tuple of 2 positive integers")
        if len(value) != 2 or type(value) != tuple:
            raise Exception("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise Exception("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def get_position(self):
        """Returns the position of the square
        """
        return self.__position

    position = property(get_position, set_position)

    def my_print(self):
        """prints in stdout the square with the character #
        """

        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(' ', end='')
                for i in range(self.__size):
                    print('#', end='')
                print()
