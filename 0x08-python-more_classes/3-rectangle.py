#!/usr/bin/python3
"""A module that defines a Rectangle class"""


class Rectangle:
    """A Rectangle class"""

    def __init__(self, width=0, height=0):
        """Creates a Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """A Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """A Setter for width
        Args:
            value: width to set (must be an integer)
        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """A Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """A Setter for height
        Args:
            value: height to set (must be an integer)
        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates and returns the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle"""
        result = ""
        for i in range(self.__height):
            if i != self.__height - 1:
                result += "#" * self.__width + "\n"
            else:
                result += "#" * self.__width
        return result
