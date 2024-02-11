#!/usr/bin/python3
'''
Module Documentation
'''


def inherits_from(obj, a_class):
    '''
    Method Documentation
    '''
    return not type(obj) is a_class and isinstance(obj, a_class)
