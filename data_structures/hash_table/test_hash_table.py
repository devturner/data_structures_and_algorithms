from .hash_table import HashTable
# import pytest


def test_hash_table_exists():
    """ make sure the ht is a thing
    """
    assert HashTable


def test_add_one():
    """Test add from ht"""
    ht = HashTable()
    ht.set('one', 'item')
    assert ht.entries_count ==1


def test_add_mult():
    """Test add from ht"""
    ht = HashTable()
    ht.set('one', 'item')
    ht.set('one', 'items')
    ht.set('two', 'item')
    assert ht.entries_count == 2


def test_get():
    """Test get from ht"""
    ht = HashTable()
    ht.set('one', 'item')
    ht.set('one', 'items')
    ht.set('two', 'ITEM')
    assert ht.get('one') == [['one', 'item', 'items']]


def test_remove():
    """Test remove from ht"""
    ht = HashTable()
    ht.set('one', 'item')
    ht.set('two', 'ITEM')
    assert ht.remove('one') == ['one', 'item']
    assert ht.entries_count == 1


def test_remove_not_found():
    """Test remove from ht"""
    ht = HashTable()
    assert ht.remove('one') == 'Key not found'
