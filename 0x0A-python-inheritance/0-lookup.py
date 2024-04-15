#!/usr/bin/python3
"""Defines a function lookup"""


def lookup(obj):
    """
    A function that returns the list of available attributes and methods of an object

    Arguments:
        @obj (class): object

    Returns: list of available attributes and methods of an object
    """
    return (dir(obj))
