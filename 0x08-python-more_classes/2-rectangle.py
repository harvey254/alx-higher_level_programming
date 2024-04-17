#!/usr/bin/python3
""" Defines a class Rectangle """


class Rectangle:
    """
    Class that defines properties of rectangle by: (based on 2-rectangle.py).

    Attributes:
        width (int): width of the rectangle.
        height (int): height of the rectangle.
        area (int): area of rectangle.
        perimeter(int): perimeter of rectangle.
    """
    __width = None
    __height = None
    area = 0
    perimeter = 0

    def __init__(self, width=0, height=0):
       " ""Creates new instances of Rectangle.

        Args:
            width (int, optional): width of rectangle. Defaults to 0.
            height (int, optional): height of rectangle. Defaults to 0.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Width retriver.

        Returns:
            int: the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter for width of rectangle.

        Args:
            value (int): width of the rectangle.

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than 0.
        """

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Height retriver.

        Returns:
            int: the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter for height of recyangle.

                  Args:
                      value (int): height of the rectangle.

                  Raises:
                      TypeError: if height is not an integer.
                      ValueError: if height is less than 0.
                  """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates area of a rectangle.

        Returns:
            int: area.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates perimeter of a rectangle

        Returns:
            int: perimeter.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
