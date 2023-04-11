#!/usr/bin/python3

"""Function to return a list of available attributes and methods of an object."""


def lookup(obj):
    """look up function"""


    return [attr for attr in dir(obj) if not callable(getattr(obj, attr)) or attr.startswith('__')]
