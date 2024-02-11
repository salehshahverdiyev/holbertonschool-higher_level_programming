#!/usr/bin/python3
"""
Module Documentation
"""


class Student:
    """
    Class Student
    """
    def __init__(self, first_name, last_name, age):
        """
        Method Documentation
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Method Documentation
        """
        return self.__dict__
