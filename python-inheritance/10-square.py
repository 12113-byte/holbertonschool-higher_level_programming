#!/usr/bin/python3
"""Square class that inherits from Rectangle"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square with validated private size"""

    def __init__(self, size):
        """initialise square with size"""
        self.integer_validation("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """returns area of square"""
        return self.__size * self.__size
