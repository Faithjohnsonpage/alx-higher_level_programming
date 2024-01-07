#!/usr/bin/python3
"""
A module that defines a function that adds numbers
"""


def add_integer(a, b=98):
    """Adds two integers
    Args:
        a: first argument
        b: secong argument(optional)
    Returns:
        the sum of the integers
    Raises:
        TypeError: if either arguments are not integer of float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
