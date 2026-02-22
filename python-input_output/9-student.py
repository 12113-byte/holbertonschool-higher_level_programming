#!/usr/bin/python3
"""Defines a class called Student with a to_json method"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Initialise a new Student instance"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary representation"""

        return self.__dict__
