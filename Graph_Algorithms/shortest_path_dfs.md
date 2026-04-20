# Shortest Path using DFS

## Theoretical Definition & Comparisons

**Theoretical Definition:** 
Shortest Path via DFS uses exhaustive depth-first exploration with backtracking to visit every possible path from source to target, tracking the minimum distance (edge count or weight sum) found.

**Comparison (Shortest Path Algorithms):**
*   **DFS (Shortest Path):** Exponential complexity $O(V!)$. Best for small graphs or when backtracking is the focus.
*   **BFS:** Optimal for unweighted graphs in $O(V+E)$.
*   **Dijkstra:** Optimal for weighted graphs with positive edges in $O(E \log V)$.

---


Finding the shortest path between two nodes in a graph is a fundamental problem. While specialized algorithms like BFS (for unweighted) and Dijkstra (for weighted) are typically preferred, Depth First Search (DFS) can also be used through exhaustive path exploration.

## Unweighted Graphs
In an unweighted graph, the shortest path is the one with the fewest number of edges. DFS can find this by exploring every possible path from the start to the end and tracking the one with the minimum length.

### Mechanism
1. Start DFS from the source node.
2. Maintain a `current_path` and `min_distance`.
3. Whenever the target node is reached, compare the length of the `current_path` with the `min_distance`.
4. If it's smaller, update `min_distance` and store the `best_path`.
5. Backtrack to explore other possible paths.

## Weighted Graphs
In a weighted graph, the shortest path is the one with the minimum total sum of edge weights.

### Mechanism & Pruning
1. Start DFS from the source node.
2. Track the `current_weight_sum` as you descend.
3. **Pruning**: If the `current_weight_sum` already exceeds the `min_distance` found so far, stop exploring that branch (Optimization).
4. When the target is reached, update the global minimum and best path if the current weight is lower.
5. Backtrack to continue the search.

## DFS vs. BFS / Dijkstra
| Feature | DFS (Shortest Path) | BFS / Dijkstra |
| :--- | :--- | :--- |
| **Complexity** | $O(V!)$ in worst case (explores all paths) | $O(V+E)$ or $O(E \log V)$ |
| **Optimal?** | Only if exhaustive search completes | Yes, by design |
| **Space** | $O(V)$ (recursion depth) | $O(V)$ (queue/heap) |
| **Use Case** | Small graphs, finding ALL paths | Large graphs, production systems |

## Why use DFS?
DFS is rarely used for shortest paths in production because of its exponential time complexity ($O(V!)$ in a complete graph). However, it is pedagogically useful for understanding **Backtracking** and is helpful when you need to find **all paths** between two nodes, not just the shortest one.
