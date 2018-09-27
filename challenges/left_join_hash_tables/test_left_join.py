from left_join import left_join_hash_tables
import pytest

@pytest.fixture
def hash1():
    return {
        'fond': 'enamored',
        'wrath': 'anger',
        'diligent': 'employed',
        'outfit': 'garb',
        'guide': 'usher',
    }

@pytest.fixture
def hash2():
    return {
        'fond': 'averse',
        'wrath': 'delight',
        'diligent': 'idle',
        'guide': 'follow',
        'flow': 'jam',
    }

@pytest.fixture
def expected():
    return [
        ['fond','enamored','averse'],
        ['wrath','anger','delight'],
        ['diligent','employed','idle'],
        ['outfit','garb','none'],
        ['guide','usher','follow'],
    ]


def test_left_join_exists():
    assert left_join_hash_tables


def test_left_join_works(hash1, hash2, expected):
    # import pdb; pdb.set_trace()
    # expected = result
    actual = left_join_hash_tables(hash1, hash2)
    assert expected == actual
