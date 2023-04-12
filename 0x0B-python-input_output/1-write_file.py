#!/usr/bin/python3
"""function defination"""


def write_file(filename="", text=""):
    """Open the file with the specified filename in write mode and UTF-8 encoding"""


    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(text)
        return len(text)
