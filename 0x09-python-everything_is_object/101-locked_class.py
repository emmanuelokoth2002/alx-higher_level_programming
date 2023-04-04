#!/usr/bin/python3

"""Defines class called LockedClass"""


class LockedClass:
    __slots__ = ['first_name']

    def __init__(self):
        self.first_name = None
    
    def __setattr__(self, name, value):
        if not hasattr(self, 'first_name') and name != 'first_name':
            raise AttributeError(f"Cannot set attribute '{name}'. 'LockedClass' allows only 'first_name' attribute.")
        object.__setattr__(self, name, value)
