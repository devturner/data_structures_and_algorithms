from hash_table import HashTable
from left_join import left_join_hash_tables
import pytest

@pytest.fixture
def hash1():
    ht = HashTable()
    ht.set('fond', 'enamored')
    ht.set('wrath', 'anger')
    ht.set('diligent', 'employed')
    ht.set('outfit', 'garb')
    ht.set('guide', 'usher')
    return ht


@pytest.fixture
def hash2():
    ht = HashTable()
    ht.set('fond', 'averse')
    ht.set('wrath', 'delight')
    ht.set('diligent', 'idle')
    ht.set('guide', 'follow')
    ht.set('flow', 'jam')
    return ht


@pytest.fixture
def expected():
    return [['fond', 'enamored', 'averse'],
    ['guide', 'usher', 'follow'],
    ['wrath', 'anger', 'delight'],
    ['diligent', 'employed', 'idle'],
    ['outfit', 'garb', 'none']]


def test_left_join_exists():
    assert left_join_hash_tables


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

def test_left_join_works(hash1, hash2, expected):
    # import pdb; pdb.set_trace()
    # expected = result
    actual = left_join_hash_tables(hash1, hash2)
    assert expected == actual
