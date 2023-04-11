#!/usr/bin/python3
"""
This module contains the Rectangle class that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A Rectangle class inheriting from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initializes an object of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        super().__init__()
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def area(self):
        """
        Calculates the area of the Rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the string representation of the Rectangle.

        Returns:
            str: A string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
