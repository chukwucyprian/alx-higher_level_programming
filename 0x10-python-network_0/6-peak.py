#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_int):
    if not list_of_int:
        return None

    left, right = 0, len(list_of_int) - 1

    while left < right:
        mid = (left + right) // 2

        # Compare the midpoint with its neighbors
        if list_of_int[mid] > list_of_int[mid + 1] and\
                list_of_int[mid] > list_of_int[mid - 1]:
            return list_of_int[mid]
        elif list_of_int[mid] < list_of_int[mid + 1]:
            left = mid + 1
        else:
            right = mid - 1

    # The peak is found when left and right converge
    return list_of_int[left]
