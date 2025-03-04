'''
Graph (Adjacency List)
A graph is a collection of nodes (vertices) connected by edges. It can be:

Directed or Undirected: Edges have direction or are bidirectional.
Weighted or Unweighted: Edges have weights or are uniform.
'''

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        """Add a vertex to the graph."""
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """Add an edge between two vertices."""
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)  # For undirected graphs

    def display(self):
        """Display the graph as an adjacency list."""
        for vertex, edges in self.adjacency_list.items():
            print(f"{vertex}: {edges}")


# Using the Graph class
graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "C")

graph.display()
# Output:
# A: ['B', 'C']
# B: ['A', 'C']
# C: ['A', 'B']
