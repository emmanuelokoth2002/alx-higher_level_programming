#!/usr/bin/python3
"""inherits from list"""


class MyList(list):
    """
    A subclass of list with a method to print the list sorted.
    """

    def print_sorted(self):
        """
        Prints the list sorted in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
