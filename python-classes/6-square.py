#!/usr/bin/python3
"""Module defining a class called Square."""


class Square:
    """Class defining a Square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialise the square with size and position."""
        self.size = size
        self.position = position

    def area(self):
        """Returns current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with the character #"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)

    @property
    def size(self):
        """getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Returns the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position"""
        if type(value) is not tuple or len(value) != 2 or type(value[0]) \
            is not int or type(value[1]) is not int or value[0] < 0 \
                or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
