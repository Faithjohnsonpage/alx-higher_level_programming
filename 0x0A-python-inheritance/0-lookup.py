#!/usr/bin/python3
"""
A module that returns list of available attributes and methods of an object
"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object"""
    return list(dir(obj))
