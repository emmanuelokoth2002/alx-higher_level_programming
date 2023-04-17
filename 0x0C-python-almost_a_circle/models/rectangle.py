#!/usr/bin/python3
"""Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor method for Rectangle class"""

        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter method for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for width attribute"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter method for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for height attribute"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """getter method for x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter method for x attribute"""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """getter method for y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter method for y attribute"""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height
    
    def display(self):
    """Prints in stdout the Rectangle instance with the character #"""
    for i in range(self.y):
        print()
    for i in range(self.height):
        print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """Return information on rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)
