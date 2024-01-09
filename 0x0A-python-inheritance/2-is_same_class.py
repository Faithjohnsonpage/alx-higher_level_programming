#!/usr/bin/python3
"""
A module that checks if object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """Function defines an instance of a class
    Args:
        obj: object considered
        a_class: the class considered
    Returns:
        True: if the object is exactly an instance of the specified class
        Failse: otherwise
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
