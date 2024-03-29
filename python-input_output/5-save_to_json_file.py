#!/usr/bin/python3
"""
Module Documentation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Method Documentation
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
    f.close()
