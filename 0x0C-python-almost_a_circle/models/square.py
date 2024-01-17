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
