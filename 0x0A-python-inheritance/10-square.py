#!/usr/bin/python3
"""This module defines a class Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class defines a square"""

    def __init__(self, size):
        """Initializes an instance of Square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns a string representation of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
