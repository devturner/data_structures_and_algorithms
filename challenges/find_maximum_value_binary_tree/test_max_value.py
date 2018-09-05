from .binary_max_value import find_max_value
from .bst import BinaryTree
import pytest


@pytest.fixture
def empty_tree():
    return BinaryTree()


@pytest.fixture
def small_tree():
    bt = BinaryTree([10, 8, 4, 12, 14])
    return bt


def test_find_max_value_exists():
    """ make sure the method is a thing
    """
    assert find_max_value


def test_find_max(small_tree):
    """ make sure this find the max
    """
    expected = 14
    actual = find_max_value(small_tree)
    assert expected == actual


def test_find_max_empty(empty_tree):
    """ make sure nothing is returned
        when the tree is empty
    """
    expected = None
    actual = find_max_value(empty_tree)
    assert expected == actual


def test_find_max_all_negative():
    """ find the largest number in all 
        negative tree
    """
    bt = BinaryTree([-10, -8, -4, -12, -14, -123, -1])
    expected = -1
    actual = find_max_value(bt)
    assert expected == actual
