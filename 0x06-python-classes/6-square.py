#!/usr/bin/python3

"""
    A class representing a square.
"""


class Square:
    """
    Attributes:
        __size: Private instance attribute for the size of the square.
        __position: Private instance attribute for the position of the square.

    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square with the given size and position.

        Args:
            size: The size of the square (optional, default is 0).
            position: The position of the square (optional, default is (0, 0)).

        Raises:
            TypeError: If size is not an integer, or position is not
            a tuple of 2 positive integers.
            ValueError: If size is less than 0, or position contains
            negative values.

        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieve the position of the square.

        Returns:
            The position of the square.

        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value: The position value to be set.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
            ValueError: If position contains negative values.

        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(num, int) for num in value) or \
                not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            The area of the square.

        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#' to stdout.

        If size is equal to 0, prints an empty line.
        Adjusts the position by printing spaces before
        each row if position[1] > 0.

        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
