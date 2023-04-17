#!/usr/bin/python3
"""Module for Base class."""


from json import dumps, loads
import csv

class Base:
    """A representation of the base of our OOP hierarchy."""
    __nb_objects = 0

    """Constructor"""


    def __init__(self, id=None):        
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
