#!/usr/bin/python3
"""This Module defines a Square class"""


class Square:
    """A class representing a square"""

    def __init__(self, size=0):
        """
        Initializes a Square class with size specified

        Args:
            size (int): defines the size of a square, default is 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
