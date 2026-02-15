#!/usr/bin/python3
"""Class called Rectangle inherits from BaseGeometry"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry
class Rectangle(BaseGeometry):
    """Class called Rectangle with private width and height validation"""

    def __init__(self, width, height):
        """initialise Rectangle with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
