#!/usr/bin/python3
""" A  function that writes a string to a text file (UTF8) and returns
    the number of characters written: 
"""


def write_file(filename: str = "", text: str = "") -> int:
    """
    Write a string to a text file and return the number of characters written.

    Args:
        filename (str): The name of the file to be written. (Default: "")
        text (str): The string to be written to the file. (Default: "")

    Returns:
        int: The number of characters written to the file.

    """
    with open(filename, 'w', encoding='utf-8') as file:
        num_chars = file.write(text)

    return num_chars
