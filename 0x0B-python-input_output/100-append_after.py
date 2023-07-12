#!/usr/bin/python3
""" A function that inserts a line of text to a file, after each
    line containing a specific string
"""


def append_after(
    filename: str = "",
    search_string: str = "",
    new_string: str = ""
):
    """
    Insert a line of text to a file after each line containing
    a specific string.

    Args:
        filename (str): The name of the file to modify. (Default: "")
        search_string (str): The string to search for in each line.
        (Default: "")
        new_string (str): The line of text to insert after each
        matching line. (Default: "")

    Returns:
        None

    """
    temp_filename = filename + '.tmp'

    with open(filename, 'r') as file, open(temp_filename, 'w') as temp_file:
        for line in file:
            temp_file.write(line)
            if search_string in line:
                temp_file.write(new_string + '\n')
