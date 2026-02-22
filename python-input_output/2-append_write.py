#!/usr/bin/python3
"""Function that adds text to the end of the file"""


def append_write(filename="", text=""):
    """
    Opens the file and adds text to the end of the file
    """
    with open(filename, "a") as f:
        return f.write(text)
