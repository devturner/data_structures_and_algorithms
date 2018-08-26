from .stack import Stack
import pytest


@pytest.fixture
def empty_stack():
    return Stack()


@pytest.fixture
def small_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    return stack


def test_stack_class_exists():
    assert Stack


def test_can_instantiate_empty_stack(empty_stack):
    assert isinstance(empty_stack, Stack)


def test_insertion_of_value_increases_len(empty_stack):
    assert len(empty_stack) == 0
    empty_stack.push(100)
    assert len(empty_stack) == 1


def test_default_value_of_top(empty_stack):
    assert empty_stack.top is None


def test_value_of_top_with_peek(small_stack):
    assert small_stack.peek().val != 3000
    assert small_stack.peek().val == 4


def test_length_of_small(small_stack):
    assert small_stack._length == 4


def test_push_empty():
    with pytest.raises(Exception):
        small_stack.push()


def test_pop_the_top(small_stack):
    small_stack.pop()
    assert small_stack._length == 3


def test_pop_returns_tops_value(small_stack):
    assert small_stack.pop() == 4


def test_pop_on_empty(empty_stack):
    with pytest.raises(AttributeError):
        empty_stack.pop()
