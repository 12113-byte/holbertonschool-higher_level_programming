#!/usr/bin/python3
"""Function that writes a text into a file"""


def write_file(filename="", text=""):
    """
    Opens the file and puts in desired text
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
