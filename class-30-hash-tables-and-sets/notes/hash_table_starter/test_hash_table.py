import pytest
from .hash_table import HashTable

def test_class_exists():
    assert(HashTable)

def test_instance_exists():
    ht = HashTable()
    assert isinstance(ht, HashTable)

def test_set():
    ht = HashTable()
    ht.set('qb','Russell Wilson')

def test_get():
    ht = HashTable()
    ht.set('qb','Russell Wilson')
    qb = ht.get('qb')
    assert qb == 'Russell Wilson'

def test_get_missing_key():
    ht = HashTable()

    with pytest.raises(KeyError):
        ht.get('qb')