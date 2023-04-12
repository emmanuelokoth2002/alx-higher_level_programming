#!/usr/bin/python3

"""function that returns an object"""


import json

def from_json_string(my_str):
    """Use the json.loads() method to parse the JSON string into a Python object"""


    obj = json.loads(my_str)
    return obj
