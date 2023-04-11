#!/usr/bin/python3
"""
Defines a Rectangle class that inherits from BaseGeometry
"""

class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises an exception with a message"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an integer value

        Args:
            name (str): the name of the value
            value (int): the value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less or equal than 0
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """Initializes a Rectangle instance

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """

        super().__init__()

        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def __str__(self):
        """Returns a string representation of the rectangle"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Computes the area of the rectangle"""

        return self.__width * self.__height
