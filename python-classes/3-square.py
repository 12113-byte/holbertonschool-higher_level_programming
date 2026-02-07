#!/usr/bin/python3
"""Module defining a class called Square."""


class Square:
    """Class defining a Square."""
    def __init__(self, size=0):
        """Initialise the square with a size."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns current square area."""
        return self.__size * self.__size
