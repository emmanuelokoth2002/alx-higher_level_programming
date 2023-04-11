#!/usr/bin/python3
"""Class defination for MyInt class"""


class MyInt(int):
    def __eq__(self, other):
        """Function to returns an integer"""


        return int(self) != int(other)
    
    def __ne__(self, other):
        """Function to returns an integer"""


        return int(self) == int(other)
