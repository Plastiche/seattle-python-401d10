from .node import Node

class LinkedList:
    def __init__(self):
        self.head = None

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