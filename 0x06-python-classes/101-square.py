#!/usr/bin/python3
class Square:
    """
    A class representing a square.

    Attributes:
        __size: Private instance attribute for the size of the square.
        __position: Private instance attribute for the position of the square.

    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square with the given size and position.

        Args:
            size: The size of the square (optional, default is 0).
            position: The position of the square as a tuple of 2 positive integers (optional, default is (0, 0)).

        Raises:
            TypeError: If size is not an integer, or position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0.

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
            The position of the square as a tuple of 2 positive integers.

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

        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            The area of the square.

        """
        return self.size ** 2

    def my_print(self):
        """
        Print the square with the character '#' in the desired format.

        """
        if self.size == 0:
            print()
            return

        for _ in range(self.position[1]):
            print()

        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            The square as a string with the character '#' in the desired format.

        """
        result = ""

        if self.size == 0:
            return result

        for _ in range(self.position[1]):
            result += "\n"

        for _ in range(self.size):
            result += " " * self.position[0] + "#" * self.size + "\n"

        return result.strip()
