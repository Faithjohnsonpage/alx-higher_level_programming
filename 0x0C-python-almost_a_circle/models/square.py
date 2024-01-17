#!/usr/bin/python3
"""
A model that defines a Square class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """A string representation of Square class"""
        return f"[{type(self).__name__}] ({self.id}) {self.x}/{self.y} - "\
               f"{self.width}"

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, size):
        """Setter for size"""
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update the Square class by adding assigned attributes"""
        attributes = ['id', 'size', 'x', 'y']
        for attr, value in zip(attributes, args):
            setattr(self, attr, value)

        for key, value in kwargs.items():
            setattr(self, key, value)
