#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Safely prints the first x integers from a list.

    Args:
        my_list (list): The list containing elements of any type.
        x (int): The number of elements to access in my_list.

    Returns:
        int: The actual number of integers printed.

    """
    count = 0
    try:
        index = 0
        while count < x:
            try:
                element = my_list[index]
                formatted_value = "{:d}".format(element)
                print(formatted_value, end='')
                count += 1
            except (IndexError, ValueError):
                pass
            index += 1
    except Exception:
        pass

    print()
    return count    
