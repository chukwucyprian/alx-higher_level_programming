#!/usr/bin/python3
class Square:
    """
    A class representing a square.

    Attributes:
        __size: Private instance attribute for the size of the square.

    """

    def __init__(self, size=0):
        """
        Initializes a square with the given size.

        Args:
            size: The size of the square (optional, default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
