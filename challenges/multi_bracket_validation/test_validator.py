from .bracket_validation import multi_braket_validation
import pytest


def test_multi_braket_validation_returns_true_happy_path():
    assert multi_braket_validation('this ( is ) good') == True

# def test_multi_braket_validation_returns_false_happy_path():
#     assert multi_braket_validation('this ( is bad') == False

# def test_insertion_of_value_increases_len(empty_stack):
#     assert len(empty_stack) == 0
#     empty_stack.push(100)
#     assert len(empty_stack) == 1


# def test_default_value_of_top(empty_stack):
#     assert empty_stack.top is None


# def test_value_of_top_with_peek(small_stack):
#     assert small_stack.peek().val != 3000
#     assert small_stack.peek().val == 4


# def test_length_of_small(small_stack):
#     assert small_stack._length == 4


# def test_push_empty():
#     with pytest.raises(Exception):
#         small_stack.push()


# def test_pop_the_top(small_stack):
#     small_stack.pop()
#     assert small_stack._length == 3


# def test_pop_returns_tops_value(small_stack):
#     assert small_stack.pop() == 4


# def test_pop_on_empty(empty_stack):
#     with pytest.raises(AttributeError):
#         empty_stack.pop()
