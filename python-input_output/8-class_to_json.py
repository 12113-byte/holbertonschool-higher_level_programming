#!/usr/bin/python3
"""Function that returns a dictionary description of an obj"""


def class_to_json(obj):
    """Returns a dictionary representation of an obj"""
    return obj.__dict__
