#!/usr/bin/python3
'''
class Rectangle
'''


class Rectangle:
    '''
    Documentation
    '''

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        '''
        init
        '''
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

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

    def __str__(self):
        i = 0
        a = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        while i < self.__height:
            i += 1
            a += ((self.__width * "#"))
            if i != self.__height:
                a += "\n"
        return a

    def __repr__(self):
        wd = self.__width
        hg = self.__height
        className = __class__.__name__
        return "{}({}, {})".format(className, wd, hg)

    def __del__(self):
        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")
