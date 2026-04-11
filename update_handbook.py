import os
import glob

# Definitions to insert
data = {
    "dijkstras_algorithm.md": """## Theoretical Definition & Comparisons

**Theoretical Definition:** 
Dijkstra's algorithm is a greedy algorithm that finds the shortest path from a single source vertex to all other vertices in a weighted graph with strictly non-negative edge weights.

**Comparison (Shortest Path Algorithms):**
*   **Dijkstra's:** Best for standard graphs. Fastest for single-source shortest path, but **fails** completely if there are **negative weights**.
*   **Bellman-Ford:** Slower than Dijkstra, but handles **negative weights** and detects negative weight cycles.
*   **Floyd-Warshall:** A Dynamic Programming approach that computes shortest paths for **all pairs** of vertices at once, instead of just a single source.
""",
    "bellman_ford_algorithm.md": """## Theoretical Definition & Comparisons

**Theoretical Definition:** 
The Bellman-Ford algorithm is a dynamic programming-like algorithm that finds the shortest path from a single source vertex to all other vertices. It systematically relaxes all edges $V-1$ times, making it robust enough to handle negative edge weights and detect negative cost cycles.

**Comparison (Shortest Path Algorithms):**
*   **Bellman-Ford:** Slower, but inherently safe for **negative weights** and cycle detection.
*   **Dijkstra's:** Faster and more efficient (using a Priority Queue), but **fails** with negative edge weights.
*   **Floyd-Warshall:** Finds shortest paths between **all pairs** of vertices, rather than from just a single starting vertex.
""",
    "floyd_warshall_algorithm.md": """## Theoretical Definition & Comparisons

**Theoretical Definition:** 
Floyd-Warshall is an All-Pairs Shortest Path (APSP) algorithm. Using dynamic programming, it systematically checks if a path between any two nodes `i` and `j` can be made shorter by passing through an intermediate node `k`.

**Comparison (Shortest Path Algorithms):**
*   **Floyd-Warshall:** Computes the shortest path between **every pair of nodes simultaneously** in $O(V^3)$. It handles negative weights.
*   **Dijkstra's:** Only finds paths from a **single source** vertex. Cannot handle negative weights.
*   **Bellman-Ford:** Only finds paths from a **single source**. Handles negative weights and detects cycles.
""",
    "kruskals_algorithm.md": """## Theoretical Definition & Comparisons

**Theoretical Definition:** 
Kruskal's Algorithm is a greedy approach to finding the Minimum Spanning Tree (MST) of a connected, undirected graph. It does this by sorting all edges by weight and iteratively adding the cheapest edge that does not form a cycle (checked via Union-Find).

**Comparison (Minimum Spanning Tree Algorithms):**
*   **Kruskal's:** Builds the MST by focusing on the **edges globally**. It sorts all edges and combines fragmented sub-trees. It typically performs better on **sparse graphs** (few edges).
*   **Prim's:** Builds the MST by focusing on **one growing tree**. It starts from a single node and expands by picking the cheapest connected edge. It performs better on **dense graphs** (many edges).
""",
    "prims_algorithm.md": """## Theoretical Definition & Comparisons

**Theoretical Definition:** 
Prim's Algorithm is a greedy algorithm that finds the Minimum Spanning Tree (MST) for a connected, undirected graph. It grows a single tree from a starting vertex by repeatedly adding the cheapest edge extending from the currently visited vertices to an unvisited vertex.

**Comparison (Minimum Spanning Tree Algorithms):**
*   **Prim's:** Grows the MST continuously from a **single origin node**. It uses a Priority Queue to pick the next closest node. Better suited for **dense graphs**.
*   **Kruskal's:** Selects minimum edges from the **entire graph globally**, regardless of where they are, and merges them using Union-Find. Better suited for **sparse graphs**.
""",
    "breadth_first_search.md": """## Theoretical Definition & Comparisons

**Theoretical Definition:** 
Breadth-First Search (BFS) is a graph traversal algorithm that explores the graph level-by-level (outward from the source node). It uses a Queue (FIFO structure) to process all neighbors of the current node before probing deeper.

**Comparison (Graph Traversals):**
*   **Breadth-First Search (BFS):** Best for finding the **shortest path in unweighted graphs**, discovering levels, or analyzing peer networks. Uses more memory for wide graphs (Queue).
*   **Depth-First Search (DFS):** Explores as deep as possible before backtracking. Best for cycle detection, topological sorting, solving mazes, and exhaustively searching paths. Uses a Stack/Recursion.
""",
    "depth_first_search.md": """## Theoretical Definition & Comparisons

**Theoretical Definition:** 
Depth-First Search (DFS) is a graph traversal algorithm that explores as deep as possible along a single branch before backtracking. It relies on a Stack (LIFO structure), usually implemented via system recursion.

**Comparison (Graph Traversals):**
*   **Depth-First Search (DFS):** Best for cycle detection, compiling topological sorts, solving puzzles (like mazes), and exploring all possibilities in decision trees.
*   **Breadth-First Search (BFS):** Explores layer-by-layer rather than deep-diving. Best for finding the absolute **shortest path** on unweighted graphs and analyzing level depths.
""",
    "topological_sort.md": """## Theoretical Definition & Comparisons

**Theoretical Definition:** 
Topological Sort produces a linear ordering of vertices in a Directed Acyclic Graph (DAG) such that for every directed edge `$u \\rightarrow v$`, vertex `u` comes before vertex `v`. It can be implemented using DFS (Push to stack on finish) or Kahn's Algorithm (In-degree queueing).

**Context & Comparison (DAG Algorithms):**
*   **Topological Sort:** Purely responsible for establishing the **dependency order** (e.g., determining which task must run before another).
*   **Longest / Shortest Path in a DAG:** Once a Topological Sort is established, calculating path lengths becomes a simple linear pass $O(V+E)$ without needing expensive algorithms like Dijkstra or Bellman-Ford.
""",
    "longest_path_dag.md": """## Theoretical Definition & Comparisons

**Theoretical Definition:** 
The Longest Path / Shortest Path in a DAG algorithm utilizes the acyclic nature of the graph to find optimal paths in strictly linear time $O(V+E)$. It first sorts the graph topologically, then processes each node forward, passing its distances to neighbors.

**Context & Comparison:**
*   **Longest Path (DAG):** Highly efficient because it evaluates nodes perfectly in dependency order. Solves the scheduling critical-path problem.
*   **Dijkstra / Bellman-Ford:** Standard shortest-path algorithms are completely unnecessary in a DAG. Bellman-Ford is $O(VE)$ and Dijkstra is $O(E \\log V)$, whereas DAG traversal achieves $O(V+E)$ linearly and handles negative edge weights naturally without infinite looping.
"""
}

# Apply definitions
directory = "Graph_Algorithms"
for filename, text in data.items():
    path = os.path.join(directory, filename)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        # Check if already inserted
        if "## Theoretical Definition & Comparisons" in content:
            print(f"Skipping {filename} (already updated)")
            continue

        # Insert after the main heading line (finding the first ## What is...)
        if "## What is" in content:
            new_content = content.replace("## What is", f"{text}\n---\n\n## What is", 1)
        elif "## Introduction" in content:
            new_content = content.replace("## Introduction", f"{text}\n---\n\n## Introduction", 1)
        else:
            # Fallback: Just put it under the main title (# ...)
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if line.startswith('# '):
                    lines.insert(i+1, f"\n{text}\n---\n")
                    break
            new_content = '\n'.join(lines)

        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"File {path} not found.")
