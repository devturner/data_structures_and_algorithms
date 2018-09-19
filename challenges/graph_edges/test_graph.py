import pytest
from .graph import Graph
from .get_edge import get_edge


@pytest.fixture()
def graph_empty():
    g = Graph()
    return g


@pytest.fixture()
def graph_filled():
    g = Graph()
    g.graph = {
        'A': {'B': 10},
        'B': {'A': 5, 'D': 15, 'C': 20},
        'C': {},
        'D': {'A': 5},
        'E': {},
        'F': {}
    }
    return g


@pytest.fixture()
def graph_filled_for_traversal():
    g = Graph()
    g.graph = {
        'A': {'B': 10, 'C': 15},
        'B': {'D': 15, 'E': 5, 'C': 2},
        'C': {'F': 50, 'G': 25},
        'D': {},
        'E': {'C': 5},
        'F': {'E': 10},
        'G': {'F': 20}
    }
    return g


def test_class_exists():
    assert Graph


def test_can_instantiate_empty_graph(graph_empty):
    assert isinstance(graph_empty, Graph)


def test_get_edge():
    assert get_edge


def test_get_edge_not_there(graph_filled_for_traversal):
    locations = ['P', 'A', 'B']
    expected = [False, 0]
    actual = get_edge(graph_filled_for_traversal, locations)
    assert expected == actual


def test_get_edge_happy(graph_filled_for_traversal):
    locations = ['A', 'B']
    expected = [True, 10]
    actual = get_edge(graph_filled_for_traversal, locations)
    assert expected == actual


def test_get_edge_with_three(graph_filled_for_traversal):
    locations = ['A', 'B', 'E']
    expected = [True, 15]
    actual = get_edge(graph_filled_for_traversal, locations)
    assert expected == actual


def test_get_edge_not_there_there(graph_filled_for_traversal):
    locations = ['A', 'D']
    expected = [False, 0]
    actual = get_edge(graph_filled_for_traversal, locations)
    assert expected == actual
