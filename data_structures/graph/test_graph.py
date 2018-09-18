import pytest
from .graph import Graph


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


def test_full_graph(graph_filled_for_traversal):
    assert len(graph_filled_for_traversal) == 7


def test_add_vert_to_graph(graph_empty):
    assert len(graph_empty) == 0
    graph_empty.add_vert('t')
    assert len(graph_empty) == 1


def test_add_vert_to_graph_already_in(graph_empty):
    graph_empty.add_vert('t')
    assert len(graph_empty) == 1
    graph_empty.add_vert('t')
    assert len(graph_empty) == 1


def test_add_vert_to_graph_not_there(graph_empty):
    with pytest.raises(Exception):
        graph_empty.add_vert()


def test_add_edge_to_graph(graph_filled_for_traversal):
    graph_filled_for_traversal.add_edge('D', 'A', 30)
    assert graph_filled_for_traversal.graph['D'] == {'A': 30}


def test_add_edge_to_graph_not_there(graph_filled_for_traversal):    
    graph_filled_for_traversal.add_edge('S', 'A', 30) == 'That key is not in the graph'
    

def test_get_neighbors(graph_filled_for_traversal):
    assert graph_filled_for_traversal.get_neighbors('E') == ['C'] 
    assert graph_filled_for_traversal.get_neighbors('B') == ['D', 'E', 'C']


def test_bft_happy(graph_filled_for_traversal):
    actual = graph_filled_for_traversal.bft('A')
    expected = ['A', 'B', 'D', 'E', 'C', 'F', 'G']
    assert actual == expected
    

def test_bft_happy_other_start(graph_filled_for_traversal):
    actual = graph_filled_for_traversal.bft('F')
    expected = ['F', 'E', 'C', 'G']
    assert actual == expected


def test_bft_happy_other_starts(graph_filled_for_traversal):
    actual = graph_filled_for_traversal.bft('D')
    expected = ['D']
    assert actual == expected