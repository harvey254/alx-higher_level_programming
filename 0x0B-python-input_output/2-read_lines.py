#!/usr/bin/python3
"""append_write function"""


def append_write(filename="", text=""):
    """a function that appends a string at the end of a text file (UTF8) and returns the number of characters added"""
    with open(filename, "a", encoding="utf-8") as f:
        file = f.write(text)
        return file
