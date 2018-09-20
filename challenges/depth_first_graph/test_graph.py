import pytest
from .graph import Graph
from .depth_first_graph import depth_first_graph
from collections import OrderedDict


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


def test_get_depth():
    assert depth_first_graph


def test_depth_not_there(graph_filled_for_traversal):
    expected = "That is not a valid starting point"
    actual = depth_first_graph(graph_filled_for_traversal, "P")
    assert expected == actual


def test_depth_first(graph_filled_for_traversal):
    expected = ['A', 'B', 'D', 'E', 'C', 'F', 'G']
    actual = depth_first_graph(graph_filled_for_traversal, 'A')
    assert expected == actual
