#!/usr/bin/python3
"""function that reads a text file"""


def read_file(filename=""):
    """Open the file with the specified filename in read mode and UTF-8 encoding"""

    with open(filename, mode='r', encoding='utf-8') as file:
        """Read the contents of the file into a string variable"""

        contents = file.read()
        """Print the contents of the file to stdout (the console)"""

        print(contents)
