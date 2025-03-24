import pytest
from src.kruskal_mst import kruskal_mst, DisjointSet

def test_disjoint_set():
    """Test the Disjoint Set data structure."""
    ds = DisjointSet(5)
    
    # Initial state: each element in its own set
    assert ds.find(0) != ds.find(1)
    assert ds.find(2) != ds.find(3)
    
    # Union two sets
    ds.union(0, 1)
    assert ds.find(0) == ds.find(1)
    
    # Ensure other sets remain separate
    assert ds.find(0) != ds.find(2)
    
    # Multiple unions
    ds.union(2, 3)
    ds.union(1, 3)
    
    # All these vertices should now be in the same set
    assert ds.find(0) == ds.find(1)
    assert ds.find(0) == ds.find(2)
    assert ds.find(0) == ds.find(3)

def test_kruskal_mst_simple_graph():
    """Test Kruskal's algorithm on a simple graph."""
    # Graph: [(weight, vertex1, vertex2), ...]
    graph = [
        (1, 0, 1),
        (2, 1, 2),
        (3, 0, 2)
    ]
    
    mst = kruskal_mst(graph)
    
    # Expected MST
    expected_mst = [(1, 0, 1), (2, 1, 2)]
    
    # Sort to ensure order doesn't matter
    assert sorted(mst) == sorted(expected_mst)

def test_kruskal_mst_complex_graph():
    """Test Kruskal's algorithm on a more complex graph."""
    graph = [
        (4, 0, 1),
        (8, 0, 7),
        (11, 1, 7),
        (8, 1, 2),
        (7, 7, 8),
        (1, 7, 6),
        (2, 8, 6),
        (6, 2, 8),
        (4, 2, 3),
        (2, 2, 5),
        (7, 3, 5),
        (14, 3, 4),
        (9, 5, 4),
        (10, 6, 5)
    ]
    
    mst = kruskal_mst(graph)
    
    # Create a DisjointSet to check connectivity
    max_vertex = max(max(u, v) for _, u, v in graph)
    ds = DisjointSet(max_vertex + 1)
    
    # Add edges and check connectivity
    connected_vertices = set()
    for weight, u, v in mst:
        # Add the edge, marking its vertices as connected
        ds.union(u, v)
        connected_vertices.update([u, v])
    
    # Verify MST properties
    assert len(mst) == 7  # V-1 edges for a graph with 9 vertices (0-8)
    assert all(ds.find(u) == ds.find(v) for _, u, v in mst)  # All vertices connected
    assert len(connected_vertices) == 9  # All 9 vertices connected

def test_kruskal_mst_empty_graph():
    """Test Kruskal's algorithm with an empty graph."""
    graph = []
    mst = kruskal_mst(graph)
    assert mst == []

def test_kruskal_mst_single_edge():
    """Test Kruskal's algorithm with a single edge."""
    graph = [(5, 0, 1)]
    mst = kruskal_mst(graph)
    assert mst == [(5, 0, 1)]

def test_kruskal_mst_multiple_minimum_edges():
    """Test case with multiple edges of the same minimum weight."""
    graph = [
        (1, 0, 1),
        (1, 1, 2),
        (2, 0, 2)
    ]
    
    mst = kruskal_mst(graph)
    
    # Either of the minimum weight edges could be in the MST
    assert len(mst) == 2
    assert all(edge[0] == 1 for edge in mst)