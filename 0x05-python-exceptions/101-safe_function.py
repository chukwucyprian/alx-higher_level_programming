#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    """
    Executes a function safely and handles any exceptions.

    Args:
        fct (function): The function to be executed.
        *args: Variable-length argument list to be passed to the function.

    Returns:
        Any: Result of the function if it executes successfully, None otherwise.

    """
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
