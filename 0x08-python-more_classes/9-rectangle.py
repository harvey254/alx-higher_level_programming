#!/usr/bin/python3
""" Defines a class Rectangle """


class Rectangle:
     """
    Class that defines properties of rectangle by: (based on 8-rectangle.py).

    Attributes:
        width (int): width of the rectangle.
        height (int): height of the rectangle.
    """
    __width = None
    __height = None
    area = 0
    perimeter = 0
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Creates new instances of Rectangle.

        Args:
            width (int, optional): width of rectangle. Defaults to 0.
            height (int, optional): height of rectangle. Defaults to 0.
        """

        self.__width = width
        self.__height = height
        self.number_of_instances += 1

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

    def __str__(self):
         """Prints the rectangle with the character # .

        Returns:
            str: the rectangle
        """
        string = ''
        self.print_symbol = str(self.print_symbol)
        if self.__height == 0 or self.width == 0:
            return ''
        for i in range(self.__height):
            for j in range(self.__width):
                string = string + self.print_symbol
            if i < (self.__height - 1):
                string = string + '\n'
        return string

    def __repr__(self):
        """Returns a string representation of the rectangle.

        Returns:
            str: the rectangle representation.
        """
        return ("Rectangle({:d}, {:d})".format(
            eval(str(self.__width)), eval(str(self.__height))))

    def __del__(self):
        """Deletes an instance of a class
        """
        print("Bye rectangle...")
        self.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Computes the area of two rectangles and compares them.

        Args:
            rect_1 (Rectangle): first rectangle.
            rect_2 (Rectangle): second rectangle.

        Returns:
            Rectangle: the rectangle with the biggest area else rect_1 if
            areas are equal
        """
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new rectangle instance with width == height == size.

        Args:
            cls: used to access class attributes.
            size (int, optional): size of rectangle (1 side). Defaults to 0.

        Returns:
            Square: the new rectangle with equal values of height and width .
        """

        return cls(size, size)
