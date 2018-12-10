class QueueNode(object):
    """
    """
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def enqueue(self, val):
        """
        """
        # NOTE: Iterative Solution
        # current = self
        #
        # while current.next:
        #     current = current.next
        #
        # new_node = QueueNode(val)
        # current.next = new_node
        # return self

        # NOTE: Recursive Solution
        if self.next is None:
            self.next = QueueNode(val)
            return

        self.next.enqueue(val)
        return self

    def dequeue(self):
        """
        """
        new_front = self.next
        self.next = None
        return new_front
