#!/usr/bin/python3
import json
""" A  function that returns the JSON representation of an object (string):"""


def to_json_string(my_obj):
    """
    Return the JSON representation of an object.

    Args:
        my_obj: The object to be serialized to JSON.

    Returns:
        str: The JSON representation of the object.

    """
    return json.dumps(my_obj)
