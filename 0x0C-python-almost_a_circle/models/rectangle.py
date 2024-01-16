#!/usr/bin/python3
"""
A module that defines a Rectangle class
"""


from models.base import Base


class Rectangle(Base):
    """A Rectangle class that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        for arg_name, arg_value in zip(['width', 'height', 'x', 'y'],
                                       [width, height, x, y]):
            if not isinstance(arg_value, int):
                raise TypeError("{} must be an integer".format(arg_name))
        for arg_name, arg_value in zip(['width', 'height'], [width, height]):
            if arg_value <= 0:
                raise ValueError("{} must be > 0".format(arg_name))
        for arg_name, arg_value in zip(['x', 'y'], [x, y]):
            if arg_value < 0:
                raise ValueError("{} must be >= 0".format(arg_name))
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter for width"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter for height"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter for x"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter for y"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Returns the area value of the Rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        print('\n' * (self.__y - 1)) if self.__y != 0 else None
        for i in range(self.__height):
            print(' ' * self.__x + "#" * self.__width)

    def __str__(self):
        """A string representation of the Rectangle class"""
        return f"[{type(self).__name__}] ({self.id}) {self.x}/{self.y} - "\
               f"{self.width}/{self.height}"

    def update(self, *args):
        """Assigns an argument to each attribute"""
        attributes = ['id', 'width', 'height', 'x', 'y']
        for attr, value in zip(attributes, args):
            setattr(self, attr, value)
