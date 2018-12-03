from .linked_list import LinkedList

def test_exists():
    assert LinkedList

def test_create():
    ll = LinkedList()
    assert isinstance(ll, LinkedList)
    # note can't just assert(ll) because
    # it's falsy by default once __len__ added

def test_len():
    ll = LinkedList()
    assert len(ll) == 0

def test_str():
    ll = LinkedList()
    assert str(ll) == 'Linked List with 0 nodes'

def test_repr():
    ll = LinkedList()
    assert repr(ll) == '<LinkedList> size:0'


def test_head_none():
    ll = LinkedList()
    assert ll.head is None

def test_insert_to_empty():
    ll = LinkedList()
    ll.insert('apples')
    assert ll.head.value == 'apples'

def test_insert_to_not_empty():
    ll = LinkedList()
    ll.insert('apples')
    ll.insert('bananas')
    assert ll.head.value == 'bananas'
    ll.head._next.value = 'apples'

def test_insert_to_not_empty_still():
    ll = LinkedList()
    ll.insert('apples')
    ll.insert('bananas')
    ll.insert('cucumbers')
    assert ll.head.value == 'cucumbers'
    assert ll.head._next.value == 'bananas'
    assert ll.head._next._next.value == 'apples'

def test_includes():
    ll = LinkedList()
    ll.insert('apples')
    ll.insert('bananas')
    assert ll.includes('apples')

def test_includes():
    ll = LinkedList()
    ll.insert('apples')
    ll.insert('bananas')
    assert ll.includes('bananas')

def test_includes_when_empty():
    ll = LinkedList()
    assert ll.includes('apples') is False

# def test_size():
#    ll = LinkedList()
#    assert len(ll) == 1
