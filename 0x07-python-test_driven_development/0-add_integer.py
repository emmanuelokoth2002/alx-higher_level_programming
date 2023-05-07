#!/usr/bin/python3
"""Defines a function of Integer addition"""


def add_integer(a, b=98):
    """Return addition of a and b"""

    """Check if a and b are integers or floats"""

    if not isinstance(a, (int,float)):
        raise TypeError("a must be an integer or b must be an integer")
    if not isinstance(b, (int,float)):
        raise TypeError("a must be an integer or b must be an integer")
    """Cast a and b to integers if they are floats"""

    a = int(a)
    b = int(b)
    return a + b
