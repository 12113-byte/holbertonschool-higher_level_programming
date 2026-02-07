#!/usr/bin/python3
"""Module defining a class called Square."""


class Square:
    """Class defining a Square."""
    def __init__(self, size=0):
        """Initialise the square with a size."""
        try:
            self.__size = size
        except type(size) is not int:
            raise TypeError("size must be an integer")
        except size < 0:
            raise ValueError("size must be >= 0")
