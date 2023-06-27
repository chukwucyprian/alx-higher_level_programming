#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element from two lists and returns a new list with the results.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The desired length of the new list.

    Returns:
        list: A new list containing the division results.

    """
    result_list = []

    for i in range(list_length):
        try:
            dividend = my_list_1[i]
            divisor = my_list_2[i]

            try:
                result = dividend / divisor
            except ZeroDivisionError:
                result = 0
                print("division by 0")
            except (TypeError, ValueError):
                result = 0
                print("wrong type")

        except IndexError:
            result = 0
            print("out of range")

        finally:
            result_list.append(result)

    return result_list
