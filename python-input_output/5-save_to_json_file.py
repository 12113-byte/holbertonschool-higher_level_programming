#!/usr/bin/python3
"""Function that writes an Object to a txt file, using a JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """Writes object to txt file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.fump(my_obj, f)
