#!/usr/bin/python3
'''
Module Documentation
'''


class BaseGeometry:
    '''
    class BaseGeometry
    '''
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    '''
    class Documentation
    '''
    def __init__(self, width, height):
        super().__init__()

        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)
