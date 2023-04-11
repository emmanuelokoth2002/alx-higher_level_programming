#!/usr/bin/python3
"""Function that adds a new attribute to an object if it’s possible"""


def add_attribute(obj, attr, value):
    """Function implementation"""


    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    obj.__dict__[attr] = value
