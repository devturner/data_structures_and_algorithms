from .queue import Queue
import pytest

@pytest.fixture
def empty_queue():
    return Queue()


@pytest.fixture
def small_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    return queue


def test_queue_class_exists():
    assert Queue


def test_can_instantiate_empty_queue(empty_queue):
    assert isinstance(empty_queue, Queue)


def test_enqueue_of_value_increases_len(empty_queue):
    assert len(empty_queue) == 0
    empty_queue.enqueue(100)
    empty_queue.enqueue(-1)
    empty_queue.enqueue('this is that enqueue test')
    assert len(empty_queue) == 3
    assert empty_queue.back.val is 'this is that enqueue test'
    assert empty_queue.front.val is 100


def test_default_value_of_top(empty_queue):
    assert empty_queue.front is None
