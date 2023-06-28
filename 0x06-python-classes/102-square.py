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
            TypeError: If size is not a number (float or integer).
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
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.

        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            The area of the square.

        """
        return self.size ** 2

    def __eq__(self, other):
        """
        Check if two squares have equal areas.

        Args:
            other: The other square to compare.

        Returns:
            True if the areas are equal, False otherwise.

        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Check if two squares have unequal areas.

        Args:
            other: The other square to compare.

        Returns:
            True if the areas are unequal, False otherwise.

        """
        return not self.__eq__(other)

    def __gt__(self, other):
        """
        Check if the area of the square is greater than the
        area of the other square.

        Args:
            other: The other square to compare.

        Returns:
            True if the area is greater, False otherwise.

        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """
        Check if the area of the square is greater than or equal to the
        area of the other square.

        Args:
            other: The other square to compare.

        Returns:
            True if the area is greater than or equal, False otherwise.

        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False

    def __lt__(self, other):
        """
        Check if the area of the square is less than the
        area of the other square.

        Args:
            other: The other square to compare.

        Returns:
            True if the area is less, False otherwise.

        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """
        Check if the area of the square is less than or equal to the
        area of the other square.

        Args:
            other: The other square to compare.

        Returns:
            True if the area is less than or equal, False otherwise.

        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False
