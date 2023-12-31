#!/usr/bin/python3
"""My square module"""


class Square:
    """A class that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Create a Square
        Args:
            size: length of a side of Square
            position: where the square is (coordinates)
        """
        self.size = size
        self.position = position

    def __str__(self):
        return self.pos_print()

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size
        Args:
            value: size to set (must be an integer >= 0)
        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position
        Args:
            value: position to set (must be a tuple of 2 positive integers)
        Raises:
            TypeError: If position is not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or \
           len(value) != 2 or not all(isinstance(i, int) for i in value) or \
           any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculate and return the area of the square"""
        return self.__size ** 2

    def pos_print(self):
        """Returns the position in spaces"""
        pos = ""
        if self.__size == 0:
            return "\n"
        for _ in range(self.__position[1]):
            pos += "\n"
        for _ in range(self.__size):
            for _ in range(self.__position[0]):
                pos += " "
            for _ in range(self.__size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """Print the square using '#' character
        The position attribute is used to determine indentation.
        """
        print(self.pos_print(), end='')
