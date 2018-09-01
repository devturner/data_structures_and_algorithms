from .bst import BinaryTree
import pytest

@pytest.fixture
def empty_tree():
    return BinaryTree()


@pytest.fixture
def small_tree():
    bt = BinaryTree([10, 8, 4, 12, 14])
    return bt


def test_binary_tree_exists():
    """ make sure the ll is a thing
    """
    assert BinaryTree


def test_create_instance_of_binary_tree():
    """ test to make sure the ll is created
    """
    bt = BinaryTree()
    assert isinstance(bt, BinaryTree)


def test_default_property_root(empty_tree):
    """ make sure the head is empty
    """
    assert empty_tree.root is None


def test_insertion_successful(empty_tree):
    """ test the insert to make sure that the element is added (25)
    """
    assert empty_tree.root is None
    empty_tree.insert(25)
    assert empty_tree.root.value == 25


def test_small_tree_insert_placements(small_tree):
    """ test the insert to make sure that the elements added are 
        placed correctly in the tree that is built. 
    """
    assert small_tree.root.value == 10
    assert small_tree.root.left.value == 8
    assert small_tree.root.left.left.value == 4
    assert small_tree.root.right.value == 12
    small_tree.insert(2)
    small_tree.insert(11)
    small_tree.insert(13)
    assert small_tree.root.right.right.left.value == 13
    assert small_tree.root.right.right.value == 14
    assert small_tree.root.right.left.value == 11
    assert small_tree.root.left.left.left.value == 2



