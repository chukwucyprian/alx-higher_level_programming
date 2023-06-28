#!/usr/bin/python3
 """
    A class representing a square.
 """


class Square:
    """
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
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            The size of the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value: The size value to be set.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            The area of the square.

        """
        return self.__size ** 2
