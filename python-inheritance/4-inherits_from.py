#!/usr/bin/python3
"""Function that checks if obj is an instance of a class that inherited"""


def inherits_from(obj, a_class):
    """Returns True if is a subclass"""
    return issubclass(obj, a_class)
