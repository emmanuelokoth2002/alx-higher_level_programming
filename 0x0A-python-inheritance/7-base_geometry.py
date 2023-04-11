#!/usr/bin/python3
"""Class defination"""


class BaseGeometry:
    """Base class for geometry calculations."""

    
    def area(self):
        """Compute area of geometry."""

        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validate input value as an integer greater than 0."""

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
