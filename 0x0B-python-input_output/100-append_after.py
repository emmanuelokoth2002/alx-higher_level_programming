#!/usr/bin/python3

"""funcyion defination"""


def append_after(filename="", search_string="", new_string=""):
    """Open the file for reading and writing using the 'with' statement"""


    with open(filename, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string + '\n')
        f.truncate()
