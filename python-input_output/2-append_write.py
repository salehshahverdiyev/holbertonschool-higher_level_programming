#!/usr/bin/python3
"""
Module Documentation
"""


def append_write(filename="", text=""):
    """
    Method Documentation
    """
    with open(filename, "a", encoding="utf-8") as f:
        count = f.write(text)
    f.close()
    return count
