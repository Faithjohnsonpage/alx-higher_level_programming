#!/usr/bin/python3
"""A module that checks if an object is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if object is an instance of the class
    Returns False otherwise
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
