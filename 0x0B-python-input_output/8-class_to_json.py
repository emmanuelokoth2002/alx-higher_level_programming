#!/usr/bin/python3

"""function that returns the dictionary description with simple data structure"""


def class_to_json(obj):
    """Create an empty dictionary to hold the serialized object"""


    serialized_obj = {}


    for attr in dir(obj):
        if not attr.startswith("__"):
            value = getattr(obj, attr)
            if isinstance(value, (list, dict, str, int, bool)):
                serialized_obj[attr] = value

    return serialized_obj
