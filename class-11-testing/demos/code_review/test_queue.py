from q import QueueNode
import pytest


# Test single node is both front and back
# Test dequeue of empty queue
# Test front and back are tracking correctly
# Test enqueue on empty & populated queue
# Test length


def test_queue_instance():
    assert QueueNode


def test_create_queue():
    q_front = QueueNode(1)
    assert q_front.val == 1


def test_enqueue():
    q_front = QueueNode(1)
    q_front.enqueue(2)
    assert q_front.next.val == 2


def test_enqueue_lrg_list():
    q_front = QueueNode(1)
    q_front.enqueue(2)
    q_front.enqueue(3)
    q_front.enqueue(4)
    q_front.enqueue(5)
    assert q_front.next.next.next.next.val == 5


def test_dequeue_populated_list():
    q_front = QueueNode(1)
    q_front.enqueue(2)
    q_front.enqueue(3)
    assert q_front.next.next.val == 3
    assert q_front.val == 1
    q_front = q_front.dequeue()
    assert q_front.next.val == 3
    assert q_front.val == 2
