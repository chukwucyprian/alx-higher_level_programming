#!/usr/bin/python3
def safe_print_integer_err(value):
    """
    Prints an integer and handles error cases.

    Args:
        value: The value to be printed.

    Returns:
        bool: True if value is an integer and printed successfully, False otherwise.

    """
    try:
        print("{:d}".format(value))
        return True
    except:
        import sys
        print("Exception:", sys.exc_info()[1], file=sys.stderr)
        return False
