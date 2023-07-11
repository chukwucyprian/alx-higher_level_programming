#!/usr/bin/python3
""" script that adds all arguments to a Python list,
    and then save them to a file:
"""
import sys
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be serialized and written to the file.
        filename (str): The name of the file to write the JSON
        representation to.

    Returns:
        None

    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)


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


def main():
    filename = 'add_item.json'
    try:
        # Load existing list from file, if available
        existing_list = load_from_json_file(filename)
    except FileNotFoundError:
        # Create a new list if the file doesn't exist
        existing_list = []

    # Add command-line arguments to the list
    existing_list.extend(sys.argv[1:])

    # Save the updated list to the file
    save_to_json_file(existing_list, filename)


if __name__ == '__main__':
    main()
