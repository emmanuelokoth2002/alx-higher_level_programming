#!/usr/bin/python3
"""Module with Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize Square instance with size"""
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return string representation of Square instance"""
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """Return the area of the Square instance"""
        return self.__size ** 2
