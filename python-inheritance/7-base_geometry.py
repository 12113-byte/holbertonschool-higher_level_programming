#!/usr/bin/python3
"""Method with a class BaseGeometry"""


class BaseGeometry:
    """class with area and integer_validator methods"""

    def area(self):
        """raises exception with a message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value is an integer > 0"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
