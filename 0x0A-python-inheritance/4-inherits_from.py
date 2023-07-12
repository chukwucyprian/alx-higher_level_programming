#!/usr/bin/python3
"""Return True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Check whether the given object is a
    class that inherited (directly or indirectly)

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
    True if the object is an instance given object is a
    class that inherited (directly or indirectly), False otherwise.
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
