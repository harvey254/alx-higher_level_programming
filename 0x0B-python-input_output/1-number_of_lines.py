#!/usr/bin/python3
"""write_file function"""


def write_file(filename="", text=""):
    """a function that writes a string to a text file (UTF8)
    Argumensts:
           @filename: name of file
           @text: text to be written on file
    Returns:the number of characters written:
    """
    with open(filename, "w", encoding="utf-8") as f:
        file = f.write(text)
        return (file)
