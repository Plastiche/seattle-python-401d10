class Node(object):
    """
    """
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return f'{ self.value }'

    def __repr__(self):
        return f'<NODE: { self.value }>'


class Stack(object):
    """
    """
    def __init__(self):
        self.top = None

    def __repr__(self):
        return f'<STACK Top: { self.top }>'

    def push(self, value):
        """
        """
        # self.top = Node(value, self.top)
        node = Node(value)
        node.next_node = self.top
        self.top = node
        return self

    def pop(self):
        """
        """
        old_top = self.top
        self.top = old_top.next_node

        old_top.next_node = None  # Implicitly handled by the janitor (i.e. Garbage collection)

        return old_top.value

    def peek(self):
        """
        """
        return self.top  # OR self.top.value
