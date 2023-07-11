#!/usr/bin/python3
""" A flie that Read the contents of a text file and print it to stdout. """


def read_file(filename: str = "") -> None:
    """
    Read the contents of a text file and print it to stdout.

    Args:
        filename (str): The name of the file to be read. (Default: "")

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified file is not found.

    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
