#!/usr/bin/python3
"""This Module defines a Square class"""


class Square:
    """A class representing a square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square class with size specified

        Args:
            size (int): defines the size of a square, default is 0
            position (tuple): defines the position to be considered
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """getter method to get position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method to set position"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
