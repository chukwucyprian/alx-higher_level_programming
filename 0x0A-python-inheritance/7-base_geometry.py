#!/usr/bin/python3
"""Base class for geometry-related classes."""


class BaseGeometry:
    """Base class for geometry-related classes.

        Examples:
    >>> import doctest
    >>> doctest.testfile('7-base_geometry.txt')
    """

    def area(self):
        """Compute the area of the geometry.

        Raises:
            Exception: This method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the value as an integer.

        Args:
            name (str): The name of the value.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
