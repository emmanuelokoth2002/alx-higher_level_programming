#!/usr/bin/python3
"""inherits from list"""


class MyList(list):
    """Class definition for MyList"""
    pass

    def print_sorted(self):
        print(sorted(list(self)))
