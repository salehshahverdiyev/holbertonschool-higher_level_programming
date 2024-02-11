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
        if isinstance(value, int) is False:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
            
