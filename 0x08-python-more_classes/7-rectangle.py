#!/usr/bin/python3

"""A class description of a rectangle"""


class Rectangle:
    """
    This class defines a rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Gets the width of the rectangle.

        Returns:
            The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The value to set the width to.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle.

        Returns:
            The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The value to set the height to.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            The perimeter of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            A string representation of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            rectangle = []
            for i in range(self.height):
                rectangle.append(str(self.print_symbol) * self.width)
            return "\n".join(rectangle)

    def __repr__(self):
        """
        Returns a string representation of the rectangle that can be used to recreate the object.

        Returns:
            A string representation of the rectangle that can be used to recreate the object.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Deletes an instance of Rectangle and decrements the number_of_instances class attribute.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
