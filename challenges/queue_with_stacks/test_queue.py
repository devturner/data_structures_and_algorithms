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
    empty_queue.enqueue(4)
    empty_queue.enqueue(45)
    assert len(empty_queue) == 4
    

def test_dequeue_returns(small_queue):
    assert small_queue.dequeue() == 1


def test_dequeue_head(small_queue):
    small_queue.dequeue()
    assert small_queue._length == 3


def test_dequeue_error(empty_queue):
    empty_queue.dequeue()
