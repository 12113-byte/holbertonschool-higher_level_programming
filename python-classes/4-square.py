#!/usr/bin/python3
"""Module defining a class called Square."""


class Square:
    """Class defining a Square."""
    def __init__(self, size=0):
        """Initialise the square with a size."""
        self.__size = size

    def area(self):
        """Returns current square area."""
        return self.__size * self.__size

    @property
    def size(self):
        """getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
