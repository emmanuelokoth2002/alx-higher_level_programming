#!/usr/bin/python3

"""Class defination"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Instantiates a new Student object with the given attributes."""


        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of the Student instance."""
        

        if attrs is None:
            return self.__dict__
        
        filtered_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                filtered_dict[attr] = getattr(self, attr)
        return filtered_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance with values from the given dictionary."""


        for key, value in json.items():
            setattr(self, key, value)
