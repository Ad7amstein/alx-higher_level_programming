#!/usr/bin/python3
"""Defines a Node and a singly linked list"""


class Node:
    """Represents a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initializes the node data.

        Args:
            data (int): Node data
            next_node (Node): Next node
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set data value."""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set next node value."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value != None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents the singly linked list."""

    def __init__(self):
        """Initializes the data."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new node 
        into the correct sorted position in the list (increasing order).

        Args:
            value (int): New value to be inserted.
        """
        new_node = Node(value)
        if self.__head == None:
            self.__head = new_node
        elif self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node and current.next_node.data < value:
                current = current.next_node

            if current.next_node:
                new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Returns a string representation of the linked list."""
        nodes = []
        current = self.__head
        while current:
            nodes.append(str(current.data))
            current = current.next_node

        return '\n'.join(nodes)
