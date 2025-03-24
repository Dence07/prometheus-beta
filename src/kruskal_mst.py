class DisjointSet:
    """
    A data structure to perform Union-Find operations efficiently.
    Used as a key component in Kruskal's Minimum Spanning Tree algorithm.
    """
    def __init__(self, vertices):
        """
        Initialize the Disjoint Set data structure.
        
        :param vertices: Number of vertices in the graph
        """
        self.parent = list(range(vertices))
        self.rank = [0] * vertices

    def find(self, item):
        """
        Find the root/representative of a set with path compression.
        
        :param item: Vertex to find the root for
        :return: Root of the set containing the vertex
        """
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x, y):
        """
        Union two sets by rank to keep the tree balanced.
        
        :param x: First vertex
        :param y: Second vertex
        :return: True if union was successful (different sets), False otherwise
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

        return True

def kruskal_mst(graph):
    """
    Find the Minimum Spanning Tree using Kruskal's Algorithm.
    
    :param graph: A list of edges where each edge is (weight, u, v)
    :return: A list of edges in the Minimum Spanning Tree
    
    Time Complexity: O(E log E), where E is the number of edges
    Space Complexity: O(V), where V is the number of vertices
    """
    # Input validation
    if not graph:
        return []

    # Sort edges by weight
    graph.sort()

    # Find the maximum vertex to determine the number of vertices
    max_vertex = max(max(u, v) for _, u, v in graph)
    vertices = max_vertex + 1

    # Initialize Disjoint Set
    disjoint_set = DisjointSet(vertices)
    minimum_spanning_tree = []

    # Number of edges in MST should be vertices - 1
    target_edges = vertices - 1

    # Process each edge
    for weight, u, v in graph:
        # If including this edge doesn't create a cycle, add it to MST
        if disjoint_set.union(u, v):
            minimum_spanning_tree.append((weight, u, v))
            
            # Stop when we have V-1 edges (or when all vertices are connected)
            if len(minimum_spanning_tree) == target_edges:
                break

    return minimum_spanning_tree