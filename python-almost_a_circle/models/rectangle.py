#!/usr/bin/python3
'''
Module Documentation
'''

from models.base import Base


class Rectangle(Base):
    '''
    class Documentation
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Method Documentation
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''
        Method Documentation
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Method Documentation
        '''
        self.__width = value

    @property
    def height(self):
        '''
        Method Documentation
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Method Documentation
        '''
        self.__height = value

    @property
    def x(self):
        '''
        Method Documentation
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
        Method Documentation
        '''
        self.__x = value

    @property
    def y(self):
        '''
        Method Documentation
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
        Method Documentation
        '''
        self.__y = value
