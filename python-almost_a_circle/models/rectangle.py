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
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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
        if isinstance(value, int) is False:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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
        if isinstance(value, int) is False:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''
        Method Documentation
        '''
        return self.__height * self.__width

    def display(self):
        '''
        Method Documentation
        '''
        x = "#" * self.__width
        for _ in range(self.__y):
            print()
        x_cordnt = " " * self.__x
        for _ in range(self.__height):
            print(x_cordnt, x, sep='')

    def __str__(self):
        '''
        Method Documentation
        '''
        return f"[Rectangle] ({self.id}) \
{self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        '''
        Method Documenta
        '''
        if args:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
