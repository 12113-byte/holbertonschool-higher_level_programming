#!/usr/bin/python3
"""Function that reads a text file"""


def read_file(filename=""):
    """
    Read the whole file and return it as a string.
    Args:
    filename(str): The name or path of the file to read.
    Returns:
    str: The content of the file.
    """
    with open(filename) as f:
        print(f.read(), end="")
