#!/usr/bin/python3
import math


class MagicClass:
    """
    A class that represents a magic circle with radius.

    Attributes:
        __radius (int or float): The radius of the circle.
    """

    def __init__(self, radius):
        """
        Initializes a MagicClass instance with the given radius.

        Args:
            radius (int or float): The radius of the circle.

        Raises:
            TypeError: If the radius is not a number (int or float).
        """
        self.__radius = 0
        if type(radius) not in (int, float):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * self.__radius ** 2

    def circumference(self):
        """
        Calculates and returns the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
