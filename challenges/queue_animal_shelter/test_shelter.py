from .animal_shelter import Animal_Shelter
import pytest


@pytest.fixture
def empty_shelter():
    return Animal_Shelter()


@pytest.fixture
def small_shelter():
    small_shelter = Animal_Shelter()
    small_shelter.enqueue('cat')
    small_shelter.enqueue('dog')
    small_shelter.enqueue('cat')
    small_shelter.enqueue('dog')
    return small_shelter


def test_shelter_class_exists():
    assert Animal_Shelter


def test_can_instantiate_empty_shelter(empty_shelter):
    assert isinstance(empty_shelter, Animal_Shelter)


def test_enqueue_of_value_increases_len(empty_shelter):
    assert len(empty_shelter) == 0
    empty_shelter.enqueue('cat')
    empty_shelter.enqueue('dog')
    empty_shelter.enqueue('cat')
    empty_shelter.enqueue('dog')
    empty_shelter.enqueue('dog')
    assert len(empty_shelter) == 5
    assert empty_shelter.front.type is 'cat'
    assert empty_shelter.front._next.type == 'dog'
    assert empty_shelter.back.type is 'dog'


def test_enqueue_error(empty_shelter):
    with pytest.raises(TypeError):
        empty_shelter.enqueue()


# def test_default_value_of_top(empty_shelter):
#     assert empty_shelter.front is None


def test_dequeue_returns(small_shelter):
    assert small_shelter.dequeue() == 'cat'


def test_dequeue_head(small_shelter):
    small_shelter.dequeue()
    assert small_shelter.front.type == 'dog'


def test_dequeue_type_is_front(small_shelter):
    assert small_shelter.dequeue('cat') is 'cat'


# def test_dequeue_type_not_front(small_shelter):
#     small_shelter.dequeue('dog')
