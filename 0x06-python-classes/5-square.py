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

    @property
    def size(self):
        """
        A getter fucntion to retrieve the size

        Return: the size attribute is returned
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        A setter function to make changes to the size

        Args:
            value: the value to be assigned to size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square

        Return:
            the current square are
        """
        return (self.__size ** 2)

    def my_print(self):
        """Prints in stdout the square with the character #"""

        if self.__size == 0:
            print()
        for i in range(1, self.__size + 1):
            for j in range(1, self.__size + 1):
                print("#", end="\n" if j == self.__size else "")
            print()


