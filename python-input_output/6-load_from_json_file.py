#!/usr/bin/python3
"""
Module Documentation
"""


import json


def load_from_json_file(filename):
    """
    Method Documentation
    """
    with open(filename, "r", encoding="utf-8") as f:
        read_data = f.read()
    f.close()
    return json.loads(read_data)
