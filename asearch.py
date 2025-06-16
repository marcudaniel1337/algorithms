import heapq

class Node:
    def __init__(self, name, parent=None, g=0, h=0):
        self.name = name      # Name of the node (could be coordinates or label)
        self.parent = parent  # Parent node in the path
        self.g = g            # Cost from start to this node
        self.h = h            # Heuristic cost to goal

    def f(self):
        return self.g + self.h

    def __lt__(self, other):
        return self.f() < other.f()  # This lets heapq sort nodes by f()

def a_star(start, goal, neighbors_fn, heuristic_fn):
    open_set = []
    heapq.heappush(open_set, Node(start, g=0, h=heuristic_fn(start, goal)))

    visited = {}

    while open_set:
        current = heapq.heappop(open_set)

        if current.name == goal:
            return reconstruct_path(current)

        visited[current.name] = current.g

        for neighbor, cost in neighbors_fn(current.name):
            g = current.g + cost
            if neighbor in visited and visited[neighbor] <= g:
                continue

            h = heuristic_fn(neighbor, goal)
            neighbor_node = Node(neighbor, parent=current, g=g, h=h)
            heapq.heappush(open_set, neighbor_node)

    return None  # No path found

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.name)
        node = node.parent
    return path[::-1]  # Reverse to get path from start to goal

# Example usage:

# Define a simple graph as adjacency list
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 3)],
    'D': [('B', 2)],
    'E': [('B', 5), ('F', 1)],
    'F': [('C', 3), ('E', 1)]
}

def neighbors_fn(node):
    return graph.get(node, [])

def heuristic_fn(node, goal):
    # Simple heuristic: pretend each step is 1 (can replace with actual heuristic like Euclidean)
    return 0  # For Dijkstra-like behavior; replace with real heuristic if available

# Find path from 'A' to 'F'
path = a_star('A', 'F', neighbors_fn, heuristic_fn)
print("Path found:", path)
