#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Safely prints the first x elements of a list.

    Args:
        my_list (list): The list containing elements of any type.
        x (int): The number of elements to print.

    Returns:
        int: The actual number of elements printed.

    """
    try:
        count = 0
        for index in range(x):
            try:
                print(my_list[index], end='')
                count += 1
            except IndexError:
                break
    except:
        pass

    print()
    return count

