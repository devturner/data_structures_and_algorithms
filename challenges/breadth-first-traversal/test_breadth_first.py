from breadth_first import breadth_first_traversal
from bst import BinaryTree
import pytest


@pytest.fixture
def empty_tree():
    return BinaryTree()


@pytest.fixture
def small_tree():
    bt = BinaryTree([10, 8, 4, 12, 14])
    return bt


def test_breadth_first_exists():
    """ make sure the method is a thing
    """
    assert breadth_first_traversal


def test_breadth_first_returns_in_order(small_tree):
    expected = [10, 8, 12, 4, 14]
    actual = breadth_first_traversal(small_tree)
    assert expected == actual






# def test_inorder_traversal():
#     bt = BinaryTree([20, 18, 12, 19, 11, 14, 40, 31, 22, 33])
#     expected = [11, 12, 14, 18, 19, 20, 22, 31, 33, 40]
#     actual = []
    
#     def generate_list(node):
#         actual.append(node.value)

#     bt.in_order(generate_list)
#     assert expected == actual    