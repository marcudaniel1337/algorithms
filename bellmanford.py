def bellman_ford(graph, start):
    # Step 1: Initialize distances
    distance = {node: float('inf') for node in graph}
    distance[start] = 0
    predecessor = {node: None for node in graph}

    # Step 2: Relax edges repeatedly
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u]:
                if distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
                    predecessor[v] = u

    # Step 3: Check for negative-weight cycles
    for u in graph:
        for v, weight in graph[u]:
            if distance[u] + weight < distance[v]:
                raise ValueError("Graph contains a negative-weight cycle")

    return distance, predecessor

# Example graph as an adjacency list
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', -3), ('D', 2)],
    'C': [('D', 3)],
    'D': []
}

# Run Bellman-Ford from 'A'
try:
    dist, prev = bellman_ford(graph, 'A')
    print("Shortest distances:", dist)

    # Optional: reconstruct path to D
    def reconstruct_path(predecessor, end):
        path = []
        while end is not None:
            path.append(end)
            end = predecessor[end]
        return path[::-1]

    print("Path to D:", reconstruct_path(prev, 'D'))

except ValueError as e:
    print("Error:", e)
