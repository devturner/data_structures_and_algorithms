from .array_binary_search import find_binary_index
import pytest

def test_element_gets_indexed_even():
    expected = 2
    actual = find_binary_index([0,1,3,4], 3)
    assert expected == actual

def test_element_gets_indexed_odd():
    expected = 2
    actual = find_binary_index([0,1,3], 3)
    assert expected == actual

def test_element_gets_indexed_not_in_list():
    expected = -1
    actual = find_binary_index([0,1,3], 33)
    assert expected == actual      

def test_element_gets_indexed_wrong():
    with pytest.raises(Exception):
        find_binary_index([0,1,3], 'goop')

def test_element_gets_indexed_empty():
    expected = -1
    actual = find_binary_index([], 3)
    assert expected == actual    