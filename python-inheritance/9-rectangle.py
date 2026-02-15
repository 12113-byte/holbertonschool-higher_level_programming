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

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns string representation of the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
