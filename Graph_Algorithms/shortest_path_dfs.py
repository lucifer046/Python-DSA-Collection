"""
Shortest Path using Depth First Search (DFS)
===========================================
This module implements shortest path discovery using exhaustive DFS exploration.
Note: While BFS is optimal for unweighted graphs and Dijkstra/Bellman-Ford for weighted graphs,
DFS can be used to find shortest paths by exploring all possible paths (exhaustive search).

1. Unweighted DFS: Finds the path with minimum number of edges.
2. Weighted DFS: Finds the path with minimum total edge weights.
"""

def shortest_path_unweighted_dfs(graph, start, end):
    """
    Finds the shortest path in an unweighted graph using exhaustive DFS.
    Returns: (distance, path)
    """
    min_dist = float('inf')
    best_path = []

    def dfs(u, target, current_path, visited):
        nonlocal min_dist, best_path
        
        # Base case: target reached
        if u == target:
            if len(current_path) - 1 < min_dist:
                min_dist = len(current_path) - 1
                best_path = list(current_path)
            return

        # Exploration
        for v in graph.get(u, []):
            if v not in visited:
                visited.add(v)
                current_path.append(v)
                dfs(v, target, current_path, visited)
                # Backtrack
                current_path.pop()
                visited.remove(v)

    dfs(start, end, [start], {start})
    return (min_dist, best_path) if best_path else (None, [])

def shortest_path_weighted_dfs(graph, start, end):
    """
    Finds the shortest path in a weighted graph using exhaustive DFS with pruning.
    graph: {u: {v: weight, ...}, ...}
    Returns: (distance, path)
    """
    min_dist = float('inf')
    best_path = []

    def dfs(u, target, current_dist, current_path, visited):
        nonlocal min_dist, best_path
        
        # Pruning: stop if current path is already worse than best found
        if current_dist >= min_dist:
            return

        # Base case: target reached
        if u == target:
            min_dist = current_dist
            best_path = list(current_path)
            return

        # Exploration
        if u in graph:
            for v, weight in graph[u].items():
                if v not in visited:
                    visited.add(v)
                    current_path.append(v)
                    dfs(v, target, current_dist + weight, current_path, visited)
                    # Backtrack
                    current_path.pop()
                    visited.remove(v)

    dfs(start, end, 0, [start], {start})
    return (min_dist, best_path) if best_path else (None, [])

if __name__ == "__main__":
    # --- Unweighted Test ---
    # Graph: A-B, B-C, A-C, C-D
    unweighted_graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B', 'D'],
        'D': ['C']
    }
    
    print("--- Unweighted Graph (DFS Shortest Path) ---")
    dist, path = shortest_path_unweighted_dfs(unweighted_graph, 'A', 'D')
    print(f"Shortest Distance: {dist}")
    print(f"Shortest Path: {' -> '.join(path)}")

    # --- Weighted Test ---
    # A --1--> B --2--> D
    # A --5--> C --1--> D
    # B --1--> C
    weighted_graph = {
        'A': {'B': 1, 'C': 5},
        'B': {'C': 1, 'D': 2},
        'C': {'D': 1},
        'D': {}
    }
    
    print("\n--- Weighted Graph (DFS Shortest Path) ---")
    w_dist, w_path = shortest_path_weighted_dfs(weighted_graph, 'A', 'D')
    print(f"Shortest Distance: {w_dist}")
    print(f"Shortest Path: {' -> '.join(w_path)}")
