#!/usr/bin/python3
""" Base module """
import json


class Base:
    """ base class
    Attributes:
        _nb_objects: number of objects created
        id: id of object
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Creates new instances 
        args:
            id: id of object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
     

     def int_validator(self, name, value):
        """ check if value is an integer """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be > 0'.format(name))

     def integer_validator2(self, name, value):
        """ check if value is an integer """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value < 0:
            raise ValueError('{} must be >= 0'.format(name))

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns JSON string
        args:
            list_dictionaries: list of dictionaries
        return:
            return serialized list or empty list
        """
        return json.dumps(list_dictionaries or [])

    @staticmethod
    def from_json_string(json_string):
        """ json to string static method
        """
        if json_string:
            return json.loads(json_string)
        return []

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes JSON string to a file
        """
        if list_objs:
            j = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        else:
            j = '[]'
        with open(cls.__name__ + '.json', 'w') as f:
            f.write(j)

    @classmethod
    def create(cls, **dictionary):
        """ return instance with all attributes 
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances
        """
        try:
            filename = cls.__name__ + '.json'
            with open(filename, mode='r') as f:
                c = cls.from_json_string(f.read())
            return [cls.create(**x) for x in c]
        except FileNotFoundError:
            return []
