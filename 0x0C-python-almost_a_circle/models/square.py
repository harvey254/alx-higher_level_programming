#!/usr/bin/pythoni3
"""Square Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
      """Square class that inherits from Rectangle"""

      def __init__(self, size, x=0, y=0, id=None):
          """initialize method """
          super().__init__(size, size, x, y, id)

      def __str__(self):
          """print method
        return:
            formatted list
          """
          return ("[{}] ({}) {}/{} - {}".format(self.__class__.__name__, self.id, self.x, self.y, self.width))
      
      @property
      def size(self):
          """width getter method
          return:
            size of width and height
          """
          return self.width

      @size.setter
      def size(self, value):
          """width and height setter method"""
          self.width = value
          self.height = value

      def update(self, *args, **kwargs):
          """update square method"""
          if args:
              i = 0
              listme = ['id', 'size', 'x', 'y']
          for arg in args:
              setattr(self, listme[i], arg)
              i += 1
              return
          else:
              for key, value in kwargs.items():
                  setattr(self, key, value)

      def to_dictionary(self):
          """returns a dictionary of Square attributes"""
          return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
