#!/usr/bin/python3
"""Class defination for MyInt class"""


class MyInt(int):
    """Override the == operator to return the opposite original result"""


    def __eq__(self, other):
        return super().__ne__(other)

    """ Override the != operator to return the opposite original result"""


    def __ne__(self, other):
        return super().__eq__(other)
