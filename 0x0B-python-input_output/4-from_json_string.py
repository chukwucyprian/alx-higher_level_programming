#!/usr/bin/python3
""" A function that returns an object (Python data structure)
    represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    Return the object represented by a JSON string.

    Args:
        my_str (str): The JSON string representing an object.

    Returns:
        object: The Python data structure represented by the JSON string.

    """
    return json.loads(my_str)
