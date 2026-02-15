#!/usr/bin/python3
"""Modules defines a class called MyList"""


class MyList(list):
    """Class that inherits from list and adds method print_sorted"""
    def print_sorted(self):
        """Prints the list in ascending sorted order"""
        print(sorted(self))
