#!/usr/bin/python3
""" A function that returns the list of available attributes
    and methods of an object
"""


def lookup(obj):
    """Return a list of available attributes and methods of an object."""
    return [attr for attr in dir(obj) if not callable(getattr(obj, attr))
            or not attr.startswith("__")]
