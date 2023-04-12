#!/usr/bin/python3

"""Class defination"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student instance with all or specified attributes.

        Args:
            attrs (list): List of attribute names to include in the dictionary. If None, include all attributes.

        Returns:
            dict: Dictionary representation of the Student instance.
        """

        if attrs is None:
            return self.__dict__
        else:
            json_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    json_dict[attr] = getattr(self, attr)
            return json_dict
