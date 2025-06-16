import heapq

def dijkstra(graph, start):
   """
   Find shortest paths from start vertex to all other vertices
   graph: dictionary where graph[node] = [(neighbor, weight), ...]
   start: starting vertex
   Returns: dictionary of shortest distances from start to each vertex
   """
   # Initialize distances - all nodes start with infinite distance except start
   distances = {node: float('inf') for node in graph}
   distances[start] = 0
   
   # Keep track of previous nodes for path reconstruction
   previous = {node: None for node in graph}
   
   # Priority queue to always process the closest unvisited node
   # Format: (distance, node)
   pq = [(0, start)]
   visited = set()
   
   while pq:
       # Get the node with minimum distance
       current_distance, current_node = heapq.heappop(pq)
       
       # Skip if we've already processed this node
       if current_node in visited:
           continue
           
       # Mark current node as visited
       visited.add(current_node)
       
       # Check all neighbors of current node
       for neighbor, weight in graph[current_node]:
           # Skip if neighbor already processed
           if neighbor in visited:
               continue
               
           # Calculate new distance through current node
           new_distance = current_distance + weight
           
           # If we found a shorter path, update it
           if new_distance < distances[neighbor]:
               distances[neighbor] = new_distance
               previous[neighbor] = current_node
               # Add to priority queue with new distance
               heapq.heappush(pq, (new_distance, neighbor))
   
   return distances, previous

def get_shortest_path(previous, start, end):
   """Reconstruct the shortest path from start to end using previous nodes"""
   path = []
   current = end
   
   # Work backwards from end to start
   while current is not None:
       path.append(current)
       current = previous[current]
   
   # Reverse to get path from start to end
   path.reverse()
   
   # Return path only if we can actually reach the end from start
   if path[0] == start:
       return path
   else:
       return []  # No path exists

# Example usage
if __name__ == "__main__":
   # Create a sample graph - adjacency list representation
   # Each node maps to list of (neighbor, weight) tuples
   graph = {
       'A': [('B', 4), ('C', 2)],
       'B': [('C', 1), ('D', 5)],
       'C': [('D', 8), ('E', 10)],
       'D': [('E', 2)],
       'E': []
   }
   
   start_node = 'A'
   print(f"Graph: {graph}")
   print(f"Starting from node: {start_node}")
   
   # Run Dijkstra's algorithm
   distances, previous = dijkstra(graph, start_node)
   
   print(f"\nShortest distances from {start_node}:")
   for node, distance in distances.items():
       if distance == float('inf'):
           print(f"  {start_node} -> {node}: No path")
       else:
           print(f"  {start_node} -> {node}: {distance}")
   
   # Show actual paths
   print(f"\nShortest paths from {start_node}:")
   for node in graph:
       if node != start_node:
           path = get_shortest_path(previous, start_node, node)
           if path:
               path_str = " -> ".join(path)
               print(f"  {start_node} to {node}: {path_str} (distance: {distances[node]})")
           else:
               print(f"  {start_node} to {node}: No path exists")
