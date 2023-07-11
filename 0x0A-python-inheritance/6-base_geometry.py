#!/usr/bin/python3
"""Base class for geometry-related classes."""


class BaseGeometry:
    """Base class for geometry-related classes."""

    def area(self):
        """Compute the area of the geometry.

        Raises:
            Exception: This method is not implemented.
        """
        raise Exception("area() is not implemented")
