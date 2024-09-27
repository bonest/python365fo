'''
365 - prepared python version of a DAG (Diagnostic Acyclic Graph)
'''
from collections import defaultdict, deque

# Class to represent a directed graph using adjacency list representation
class Graph:


    '''
    self.graph property er et dictionary
    Key = node id
    Value = Liste af noder

    I 365 regi skal value være et objekt der indeholder parrent værdier + liste af sub noder
    '''

    def __init__(self):
        self.graph = defaultdict(list)

    # Function to add an edge to the graph
    def add_edge(self, u, v):
        # Append node til liste på parrent index. 
        
        self.graph[u].append(v)

    

    # Function to perform BFS traversal from a given source vertex
    def bfs(self, start):
        visited = set()  # Set to keep track of visited nodes
        queue = deque([start])  # Initialize a queue with the starting node

        while queue:
            vertex = queue.popleft()  # Dequeue a vertex from the queue
            if vertex not in visited:
                print(vertex, end=" ")  # Process the current node
                visited.add(vertex)  # Mark the node as visited

                # Enqueue all adjacent vertices that haven't been visited
                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)

# Example usage
if __name__ == '__main__':
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 6)

    print("Following is Breadth First Traversal (starting from vertex 0):")
    g.bfs(0)  # Starting BFS traversal from vertex 0