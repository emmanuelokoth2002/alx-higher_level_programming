#!/usr/bin/python3

""" function that creates an Object from a “JSON file """


import json

def load_from_json_file(filename):
    """Open the file with the specified filename in read mode and UTF-8 encoding"""


    with open(filename, mode='r', encoding='utf-8') as file:
        file_contents = file.read()
        obj = json.loads(file_contents)
        return obj
