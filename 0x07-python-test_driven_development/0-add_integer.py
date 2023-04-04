#!/usr/bin/python3
"""Defines a function of Integer addition"""


def add_integer(a, b=98):
    """Return addition of a and b"""

    """Check if a and b are integers or floats"""

    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer or b must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("a must be an integer or b must be an integer")
    """Cast a and b to integers if they are floats"""

    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b
    return a + b
