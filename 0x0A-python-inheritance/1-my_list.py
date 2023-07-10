#!/usr/bin/python3
"""Print the list in sorted order (ascending sort)."""


class MyList(list):
    def print_sorted(self):
        """Print the list in sorted order (ascending sort)."""
        sorted_list = sorted(self)
        print(sorted_list)
