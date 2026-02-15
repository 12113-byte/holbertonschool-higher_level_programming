#!/usr/bin/python3
"""Square class that inherits from Rectangle"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square with validated private size"""

    def __init__(self, size, width):
        """initialise square with size"""
        self.integer_validator("size", size)
        self.integer_validator("width", width)
        super().__init__(size, size)
        super().__init__(width, width)
        self.__size = size
        self.__width = width

    def area(self):
        """returns area of square"""
        return self.__size * self.__size

    def __str__(self):
        """returns string representation of the square"""
        return f"[Square] {self.__width}/{self.__height}"
