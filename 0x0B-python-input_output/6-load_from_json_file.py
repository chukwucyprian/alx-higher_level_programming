#!/usr/bin/python3
import json
""" A function that creates an Object from a “JSON file”: """


def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        object: The Python object created from the JSON file.

    """
    with open(filename, 'r') as file:
        obj = json.load(file)

    return obj
