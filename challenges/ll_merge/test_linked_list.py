from .linked_list import LinkedList
from .ll_merge import ll_merge
import pytest

@pytest.fixture
def empty_list():
    return LinkedList()


@pytest.fixture
def small_list():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    return ll

@pytest.fixture
def smalls_list():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(6)
    ll.insert(7)
    ll.insert(8)
    return ll    


# def test_linked_list_exists():
#     """ make sure the ll is a thing
#     """
#     assert LinkedLista

def test_ll_merge(small_list, smalls_list):
    assert ll_merge(small_list, smalls_list)._length == 8


def test_ll_merge_placement(small_list, smalls_list):
    merged = ll_merge(small_list, smalls_list)
    assert merged.kth_from_the_end(7) == 1
    assert merged.kth_from_the_end(6) == 5
    assert merged.kth_from_the_end(5) == 2
    assert merged.kth_from_the_end(4) == 6 
    assert merged.kth_from_the_end(3) == 3
    assert merged.kth_from_the_end(2) == 7
    assert merged.kth_from_the_end(1) == 4
    assert merged.kth_from_the_end(0) == 8

# def test_create_instance_of_list():
#     """ test to make sure the ll is created
#     """
#     ll = LinkedList()
#     assert isinstance(ll, LinkedList)


# def test_default_property_head(empty_list):
#     """ make sure the head is empty
#     """
#     assert empty_list.head is None


# def test_default_property_length(empty_list):
#     """ make sure the ll is empty
#     """
#     assert empty_list._length == 0


# def test_insertion_successful(empty_list):
#     """ test the insert to make sure that the element is added (1)
#     """
#     assert empty_list.head is None
#     empty_list.insert(25)
#     assert empty_list.head.val == 25


# def test_length_of_list_increases_on_insertion(empty_list):
#     """ Make sure ll insert changes the len of the ll (+1)
#     """
#     assert len(empty_list) == 0
#     empty_list.insert(25)
#     assert len(empty_list) == 1


# def test_includes_returns_true_if_exists(small_list):
#     """ return true if the element is in the ll
#     """
#     actual = small_list.includes(4)
#     assert actual is True
#     assert small_list.includes(1) is True

# def test_includes_returns_false_if_not_exists(small_list):
#     """ return false if the element is not the ll
#     """
#     assert small_list.includes(100) is False
#     assert small_list.includes(0) is False

# def test_append_adds_node(small_list):
#     """ return true if the element is added to the ll
#     """
#     small_list.append(45)
#     assert small_list.includes(45) is True


# def test_insert_after(small_list):
#     """ return true if the element is added after the val in the ll
#     """
#     small_list.insert_after(2, 77)
#     assert small_list.includes(77) is True


# def test_insert_before(small_list):
#     """  return true if the element is added before the val in the ll
#     """
#     small_list.insert_before(2, 77)
#     assert small_list.includes(77) is True


# def test_kth_locator_each_2(small_list):
#     """ make sure the kth arg is found and has the correct value
#     """
#     assert small_list.kth_from_the_end(2) == 3 


# def test_kth_locator_each_0(small_list):
#     """ make sure the kth arg is found and has the correct value
#     """
#     assert small_list.kth_from_the_end(0) == 1

# def test_kth_locator_each_1(small_list):
#     """ make sure the kth arg is found and has the correct value
#     """
#     assert small_list.kth_from_the_end(1) == 2     

# def test_kth_locator_each_4(small_list):
#     """ make sure the kth arg is found and has the correct value
#     """
#     assert small_list.kth_from_the_end(3) == 4

# def test_kth_for_error_returned(small_list):
#     """ make sure the kth arg is not found and raises an error
#     """
#     with pytest.raises(AttributeError):
#         small_list.kth_from_the_end(9)