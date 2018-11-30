from .node import Node


class LinkedList(object):
    """
    """
    def __init__(self, iterable=None):
        self.head = None
        self._size = 0

        if iterable is None:
            iterable = []

        if type(iterable) is not list:
            raise TypeError('iterable must be of type list')

        for val in iterable:
            self.insert(val)

    def __str__(self):
        output = f'Linked List: Head val - { self.head }'
        return output

    def __repr__(self):
        output = f'<LinkedList: head - { self.head } size - { self._size }>'
        return output

    def __len__(self):
        return self._size

    def insert(self, value):
        """
        """
        node = Node(value)
        node._next = self.head
        self.head = node
        # self.head = Node(value, self.head)
        self._size += 1

    def includes(self):
        """TODO:
        """