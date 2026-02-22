#!/usr/bin/python3
"""Function turning JSON string to object (deserializing)"""

import json


def from_json_string(my_str):
    """Returns converted string from json to object"""
    return json.loads(my_str)
