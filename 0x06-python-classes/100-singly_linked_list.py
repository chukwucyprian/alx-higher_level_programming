#!/usr/bin/python3
"""
    A class representing a node of a singly linked list.
"""


class Node:
    """
   Attributes:
        __data: Private instance attribute for the data stored in the node.
        __next_node: Private instance attribute for the reference to
        the next node.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a node with the given data and next_node.

        Args:
            data: The data to be stored in the node.
            next_node: The reference to the next node
            (optional, default is None).

        Raises:
            TypeError: If data is not an integer, or next_node is not None
            or a Node object.

        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieve the data stored in the node.

        Returns:
            The data stored in the node.

        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data stored in the node.

        Args:
            value: The data value to be set.

        Raises:
            TypeError: If data is not an integer.

        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieve the reference to the next node.

        Returns:
            The reference to the next node.

        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the reference to the next node.

        Args:
            value: The reference to the next node.

        Raises:
            TypeError: If next_node is not None or a Node object.

        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

"""
    A class representing a singly linked list.
"""

class SinglyLinkedList:
    """
    Attributes:
        head: The first node of the linked list.

    """

    def __init__(self):
        """
        Initializes an empty singly linked list.

        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in
        the list (increasing order).

        Args:
            value: The value to be inserted into the linked list.

        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None
            and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            The linked list as a string with one node number per line.

        """
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()
