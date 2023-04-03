#!/usr/bin/python3

"""class description for  Rectangle"""


class Rectangle:
    """Representation for class"""


    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width should  be an integer")
        elif value < 0:
            raise ValueError("width should  be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height should  be an integer")
        elif value < 0:
            raise ValueError("height should  be >= 0")
        else:
            self.__height = value