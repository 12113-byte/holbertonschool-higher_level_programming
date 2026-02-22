#!/usr/bin/python3
"""Defines a class called Student with a to_json method"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Initialise a new Student instance"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary representation of the instance.
        If attrs is a list of str, returns only those attributes.
        Otherwise, returns all attributes"""

        if isinstance(attrs, list):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
