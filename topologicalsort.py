from typing import Dict, List, Set
from collections import defaultdict


class CycleError(Exception):
    """Raised when a cycle is detected in the graph."""
    pass


class DirectedGraph:
    def __init__(self):
        self._adjacency: Dict[str, List[str]] = defaultdict(list)

    def add_edge(self, src: str, dest: str) -> None:
        """Adds a directed edge from src to dest."""
        self._adjacency[src].append(dest)
        if dest not in self._adjacency:
            self._adjacency[dest] = []

    def topological_sort(self) -> List[str]:
        """Performs topological sort on the graph.

        Returns:
            A list of node names in topologically sorted order.

        Raises:
            CycleError: If the graph contains a cycle.
        """
        visited: Set[str] = set()
        visiting: Set[str] = set()
        result: List[str] = []

        def dfs(node: str) -> None:
            if node in visiting:
                raise CycleError(f"Cycle detected at node '{node}'")
            if node in visited:
                return

            visiting.add(node)
            for neighbor in self._adjacency[node]:
                dfs(neighbor)
            visiting.remove(node)
            visited.add(node)
            result.append(node)

        for node in self._adjacency:
            if node not in visited:
                dfs(node)

        return result[::-1]

    def __str__(self):
        return '\n'.join(f"{k} → {v}" for k, v in self._adjacency.items())


# Example usage
if __name__ == "__main__":
    graph = DirectedGraph()
    graph.add_edge("A", "C")
    graph.add_edge("B", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "E")
    graph.add_edge("D", "F")
    graph.add_edge("E", "F")
    graph.add_edge("E", "H")
    graph.add_edge("F", "G")

    print("Graph Structure:\n")
    print(graph)

    try:
        order = graph.topological_sort()
        print("\nTopological Sort Order:\n")
        print(" → ".join(order))
    except CycleError as e:
        print(f"\nERROR: {e}")
