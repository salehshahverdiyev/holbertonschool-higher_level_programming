#!/usr/bin/python3
"""
Module Documentation
"""


def read_file(filename=""):
    """
    Method Documentation
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
    print(read_data, end="")
    f.close()
