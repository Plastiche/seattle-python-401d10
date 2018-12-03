from .node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return 0

    def __str__(self):
        return f'Linked List with {self.size} nodes'

    def __repr__(self):
        return f'<LinkedList> size:{self.size}'

    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, value):

        current = self.head

        while current:
            if current.value == value:
                return True
            else:
                current = current._next

        return False
