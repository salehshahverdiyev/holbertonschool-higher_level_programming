#!/usr/bin/python3
'''
Model Documentation
'''

import json

class Base:
    '''
    class Documentation
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Method Documentation
        '''
        self.__class__.__nb_objects += 1
        if id is not None:
            self.id = id
        else:
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        Method Documentation.
        '''
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
