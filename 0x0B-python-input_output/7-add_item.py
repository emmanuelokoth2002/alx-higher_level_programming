#!/usr/bin/python3

""" script that adds all arguments to a Python list"""


import sys
from save_to_json_file import 5-save_to_json_file
from load_from_json_file import 6-load_from_json_file

my_list = []

for arg in sys.argv[1:]:
    my_list.append(arg)

save_to_json_file(my_list, "add_item.json")
loaded_list = load_from_json_file("add_item.json")
print(loaded_list)
