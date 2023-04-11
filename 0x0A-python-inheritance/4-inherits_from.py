#!/usr/bin/python3
"""function to  returns True if the object is an instance of a class that inherited"""


def inherits_from(obj, a_class):
    """Function defination."""


    return issubclass(type(obj), a_class) and type(obj) is not a_class
