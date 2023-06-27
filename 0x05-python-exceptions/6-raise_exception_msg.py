#!/usr/bin/python3
def raise_exception_msg(message=""):
    """
    Raises a NameError exception with a custom message.

    Args:
        message (str): The custom message for the exception. Default is an empty string.

    Raises:
        NameError: Always raises a NameError with the provided message.

    """
    raise NameError(message)
