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

    def area(self):
        """
        Calculates the area of the square

        Return:
            the current square are
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        A getter fucntion to retrieve the size

        Return: the size attribute is returned
        """
        return str(self.__size)

    #size.setter
    def size(self, value):
        """
        A setter function to make changes to the size

        Args:
            value: the value to be assigned to size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
