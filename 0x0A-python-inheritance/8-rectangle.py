#!/usr/bin/python3
"""Base class for geometry-related classes."""


class BaseGeometry:
    """Basic class named BaseGeometry
    """

    def area(self):
        """
        Public instance method: raises exception
        No implementation yet
        Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        public instance method: validate value
        Args :
            name and value
        Raises :
            if value is not an integer: TypeError exception,
            with the message <name> must be an integer
            if value is less or equal to 0: raise a ValueError
            exception with the message <name> must be greater than 0
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
