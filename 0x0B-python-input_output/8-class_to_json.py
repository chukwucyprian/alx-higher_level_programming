#!/usr/bin/python3
""" A function that Convert an object to a dictionary
    representation suitable for JSON serialization.
"""


def class_to_json(obj):
    """
    Convert an object to a dictionary representation suitable
    for JSON serialization.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: The dictionary representation of the object.

    """
    if hasattr(obj, '__dict__'):
        json_dict = {}
        for key, value in obj.__dict__.items():
            if value is None:
                continue
            if isinstance(value, (str, int, bool)):
                json_dict[key] = value
            elif isinstance(value, (list, dict)):
                json_dict[key] = value
            else:
                json_dict[key] = class_to_json(value)
        return json_dict
    else:
        return obj
