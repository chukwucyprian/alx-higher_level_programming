#!/usr/bin/python3
""" A  function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added:
"""


def append_write(filename: str = "", text: str = "") -> int:
    """
    Append a string at the end of a text file and return the number of characters added.

    Args:
        filename (str): The name of the file to be appended. (Default: "")
        text (str): The string to be appended to the file. (Default: "")

    Returns:
        int: The number of characters added to the file.

    """
    with open(filename, 'a', encoding='utf-8') as file:
        num_chars = file.write(text)

    return num_chars
