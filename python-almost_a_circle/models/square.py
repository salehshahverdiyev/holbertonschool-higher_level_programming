#!/usr/bin/python3
'''
Module Documentation
'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    class Documentation
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''
        Method Documentation
        '''
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        '''
        Method Documentation
        '''
        return f"[Square] ({self.id}) \
{self.x}/{self.y} - {self.size}"
