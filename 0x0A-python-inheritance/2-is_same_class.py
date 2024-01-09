#!/usr/bin/python3
"""
A module that checks if object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """Function defines an instance of a class
    Args:
        obj: object considered
        a_class: the class to compare against
    Returns:
        True: if the object is exactly an instance of the specified class
        Failse: otherwise
    """
    return type(obj) is a_class
