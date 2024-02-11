#!/usr/bin/python3
"""
Module Documentation
"""


def write_file(filename="", text=""):
    """
    Method Documentation
    """
    with open(filename, "w", encoding="utf-8") as f:
        count = f.write(text)
    f.close()
    return count
