#!/usr/bin/python3

"""Function that returns the JSON representation"""


import json

def to_json_string(my_obj):
    """Use the json.dumps() method to convert the object to a JSON string"""


    json_string = json.dumps(my_obj)
    return json_string
