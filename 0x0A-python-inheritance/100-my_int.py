#!/usr/bin/python3
"""Class defination"""


class MyInt(int):
    def __eq__(self, other):
        """Returns an integer"""


        return int(self) != int(other)
    
    def __ne__(self, other):
        """Returns an integer"""


        return int(self) == int(other)
