#!/usr/bin/python3
"""
Module Documentation
"""


def pascal_triangle(n):
    """
        Method Documentation
    """
    final_list = []
    list_creator = [1]
    temp = []
    for x in range(n):
        final_list.append(list_creator)
        temp.append(1)
        for i in range(1, len(list_creator)):
            temp.append(list_creator[i] + list_creator[i-1])
        temp.append(1)
        list_creator = temp
        temp = []
    return final_list
