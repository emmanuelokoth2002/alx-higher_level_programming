#!/usr/bin/python3
""" function that writes an Object to a text file, using a JSON representation"""


import json

def save_to_json_file(my_obj, filename):
    """Convert the object to a JSON string"""


    json_string = json.dumps(my_obj)
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(json_string)
