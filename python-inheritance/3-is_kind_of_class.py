#!/usr/bin/python3
"""Function about same class or inherit form"""


def is_kind_of_class(obj, a_class):
    """returns True, if obj is an instance of, or a class inherited from"""
    return isinstance(obj, a_class)
