#!/usr/bin/python3
"""function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Open the file with the specified filename in append mode and UTF-8 encoding"""


    with open(filename, mode='a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
