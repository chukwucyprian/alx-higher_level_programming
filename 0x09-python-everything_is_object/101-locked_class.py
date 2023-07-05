#!/usr/bin/python3
"""Class that restricts dynamically creating new instance attributes,
    except for 'first_name'.
"""


class LockedClass:
    """Class that restricts dynamically creating new instance attributes,
    except for 'first_name'."""

    __slots__ = ['first_name']

    def __setattr__(self, attr, value):
        """
        Override the __setattr__ method to restrict dynamically creating
        new instance attributes.

        Args:
            attr (str): The name of the attribute being set.
            value: The value to assign to the attribute.

        Raises:
            AttributeError: If the attribute being set is not 'first_name'.
        """
        if attr not in self.__slots__:
            raise AttributeError("'LockedClass' object has no attribute 'last_name'")
        super().__setattr__(attr, value)
