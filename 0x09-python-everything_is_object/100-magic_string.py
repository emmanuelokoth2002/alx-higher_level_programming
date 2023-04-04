#!/usr/bin/python3

"""Defination for function magic_string"""


def magic_string():
    """Representation for the function"""

    if not hasattr(magic_string, "count"):
        magic_string.count = 1
    else:
        magic_string.count += 1
    return ", ".join(["BestSchool"] * magic_string.count)
