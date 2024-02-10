#!/usr/bin/python3
'''
Module Documentation
'''


def inherits_from(obj, a_class):
    '''
    Method Documentation
    '''
    obj_class = type(obj)

    if issubclass(obj_class, a_class):
        return True
    for base_class in obj_class.__bases__:
        if inherits_from(base_class, a_class):
            return True
    return False
