#!/usr/bin/python3
"""read_file function"""


def read_file(filename=""):
    """"a function that reads a text file (UTF8) and prints it to stdout:"""
    with open(filename, "r", encoding="utf-8") as f:
        file = f.read()
        print(file, end="")
        close(file)
