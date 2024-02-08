#!/usr/bin/python3
'''
class Rectangle
'''


class Rectangle:
    '''
    Documentation
    '''
    def __init__(self, width=0, height=0):
        '''
        init
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''
        Documentation for this
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Documentation for this
        '''
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''
        Documentation for this
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Documentation for this
        '''
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width
    
    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (2 * (self.__height + self.__width))