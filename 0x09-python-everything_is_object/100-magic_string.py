#!/usr/bin/bash/python3
def magic_string():
    if not hasattr(magic_string, "count"):
        magic_string.count = 1
    else:
        magic_string.count += 1
    return ", ".join(["BestSchool"] * magic_string.count)