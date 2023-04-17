#!/usr/bin/python3
""" Module that contains the Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """A representation of a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the Square instance"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter method for the size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for the size attribute"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes of the Square instance"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the Square instance"""
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}

