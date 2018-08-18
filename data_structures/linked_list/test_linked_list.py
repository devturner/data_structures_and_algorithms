from .linked_list import LinkedList, Node
import pytest


@pytest.fixture
def empty_list():
    return LinkedList()


@pytest.fixture
def small_list():
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    linked_list.insert(4)
    # import pdb; pdb.set_trace()
    return linked_list


def test_linked_list_exists():
    assert LinkedList


def test_create_instance_of_list():
    ll = LinkedList()
    assert isinstance(ll, LinkedList)


def test_default_property_head(empty_list):
    assert empty_list.head is None


def test_default_property_length(empty_list):
    assert empty_list._length == 0


def test_insertion_successful(empty_list):
    assert empty_list.head is None
    empty_list.insert(25)
    assert empty_list.head.val == 25


def test_length_of_list_increases_on_insertion(empty_list):
    assert len(empty_list) == 0
    empty_list.insert(25)
    assert len(empty_list) == 1


def test_includes_returns_true_if_exists(small_list):
    # actual = small_list.find_node(4)
    assert small_list.find_node(4) is True
    # assert actual is True
    # assert small_list.includes(1) is True


def test_includes_returns_false_if_not_exists(small_list):
    assert small_list.find_node(100) is False
# #     assert small_list.includes(0) is False
