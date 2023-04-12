#!/usr/bin/python3

"""Class defination"""


class Student:
    """Defines a student with a first name, last name, and age"""

    def __init__(self, first_name, last_name, age):
        """Instantiates a new Student object with a first name, last name, and age"""


        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary representation of a Student instance for JSON serialization"""


        serialized_student = {}


        for attr in dir(self):
            if not attr.startswith("__"):
                value = getattr(self, attr)
                if isinstance(value, (list, dict, str, int, bool)):
                    serialized_student[attr] = value

        return serialized_student
