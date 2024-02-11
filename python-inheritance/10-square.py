#!/usr/bin/python3
'''
Module Documentation
'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    class Documentation
    '''
    def __init__(self, size):
        super().integer_validator("size", size)

        self.__size = size
        super().__init__(size, size)
