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
        __class__.__nb_objects += 1
        if id is not None:
            self.id = id
        else:
            self.id = __class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        Method Documentation.
        '''
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        Method Documentation
        '''
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(Base.to_json_string(list))

    @staticmethod
    def from_json_string(json_string):
        '''
        Method Documentation
        '''
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)
