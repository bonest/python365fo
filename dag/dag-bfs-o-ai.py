from collections import deque
from typing import Dict, List, Set

class Node:
    def __init__(self, id: str, value: str) -> None:
        self._id: str = id
        self._value: str = value
    
    @property
    def id(self) -> str:
        return self._id
    
    @id.setter
    def id(self, new_id: str) -> None:
        if not isinstance(new_id, str):
            raise ValueError("ID must be a string")
        self._id = new_id
    
    @property
    def value(self) -> str:
        return self._value
    
    @value.setter
    def value(self, new_value: str) -> None:
        self._value = new_value
    
    def __str__(self) -> str:
        return f"Node({self.id}, {self.value})"
    
    def __repr__(self) -> str:
        return self.__str__()

class DAG:
    def __init__(self) -> None:
        # An empty dictionary 
        self._graph: Dict[Node, List[Node]] = {}
    
    @property
    def graph(self) -> Dict[Node, List[Node]]:
        return self._graph
    
    def add_edge(self, u: Node, v: Node) -> None:
        if u not in self._graph:
            self._graph[u] = []
        self._graph[u].append(v)
        
        if v not in self._graph:
            self._graph[v] = []

def bfs_traversal(graph: DAG, start: Node) -> List[Node]:
    queue: deque = deque([start])
    visited: Set[Node] = set([start])
    traversal: List[Node] = []
    
    while queue:
        node: Node = queue.popleft()
        traversal.append(node)
        
        for neighbor in graph.graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return traversal

# Create nodes
node_a: Node = Node('A', 'Start')
node_b: Node = Node('B', 'Process 1')
node_c: Node = Node('C', 'Process 2')
node_d: Node = Node('D', 'Process 3')
node_e: Node = Node('E', 'End')

# Create a DAG
dag: DAG = DAG()

# Add edges to the DAG
dag.add_edge(node_a, node_b)
dag.add_edge(node_a, node_c)
dag.add_edge(node_b, node_d)
dag.add_edge(node_c, node_d)
dag.add_edge(node_c, node_e)
dag.add_edge(node_d, node_e)

# Perform BFS traversal starting from node_a
traversal_result: List[Node] = bfs_traversal(dag, node_a)

# Print the result
print("BFS Traversal:")
for node in traversal_result:
    print(f"{node.id} ({node.value})", end=" -> " if node != traversal_result[-1] else "\n")

# Demonstrate property usage
print("\nDemonstrating property usage:")
try:
    node_a.id = 123  # This will raise a ValueError
except ValueError as e:
    print(f"Caught an error: {e}")

node_a.value = "New Start"
print(f"Updated node_a: {node_a}")