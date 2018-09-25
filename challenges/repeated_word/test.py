import pytest
from .repeated_word import repeated_word


def test_repeated_word():
    str = 'This is the first test, it is a good test'
    expected = 'is'
    actual = repeated_word(str)
    assert actual == expected

