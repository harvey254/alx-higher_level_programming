#!/usr/bin/python3
""" Rectangle module """
from models.base import Base


class Rectangle(Base):
    """ class Rectangle that inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor Rectangle
            Arguments:
            @width: width of rectangle
            @height: height of rectangle
            @x: x position
            @y: y position
            @id: instances
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Retrieves the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter method """
        self.int_validator('width', value)
        self.__width = value

    @property
    def height(self):
        """ Retrieves the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Height setter method """
        self.int_validator('height', value)
        self.__height = value

    @property
    def x(self):
        """x getter method"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter method"""
        self.int_validator2('x', value)
        self.__x = value

    @property
    def y(self):
        """y getter method"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter method"""
        self.int_validator2('y', value)
        self.__y = value

    def display(self):
        """print into stdout
        return: na
        """
        for row in range(self.y):
            print()
        for row in range(self.height):
            print("{}{}".format(" " * self.x, "#" * self.width))


    def __str__(self):
        """print method"""
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """update attributes"""
        if args:
            my_list = ['id', 'width', 'height', 'x', 'y']
            i = 0
            for arg in args:
                setattr(self, my_list[i], arg)
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ return dict representation of Rectangle """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
