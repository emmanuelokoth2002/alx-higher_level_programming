#!/usr/bin/python3
"""Module containing the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that defines a Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for the Square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the string representation of the Square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates attributes"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
