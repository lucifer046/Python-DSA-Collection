"""
================================================================================
CONCEPTS AND THEORY: FLOYD-WARSHALL (THE 'ALL-TO-ALL' SHORTEST PATH)
================================================================================

--- TIME COMPLEXITY ANALYSIS ---
- BEST CASE:    O(V^3) (Always iterates through three nested loops)
- AVERAGE CASE: O(V^3) 
- WORST CASE:   O(V^3) 
--------------------------------
- SPACE COMPLEXITY: O(V^2) (Requires a 2D matrix to store distances)

STATUS: INDEPENDENT (Contains both a full and a compact implementation)
================================================================================

1. WHAT IS FLOYD-WARSHALL?
   While Dijkstra's finds the shortest path from ONE node to all others, 
   Floyd-Warshall finds the shortest path between EVERY pair of nodes 
   in the entire graph at once! 

2. THE 'TRANSITIVE' LOGIC:
   If we can go from A to B with some cost, and from B to C with some cost, 
   then we can definitely go from A to C by going through B. 
   The algorithm asks: "Is taking the path through B shorter than my 
   current best for A to C?" 

3. HOW IT WORKS:
   - We start with an 'Adjacency Matrix' (a grid of all costs).
   - We pick every possible intermediate node 'k'.
   - For every pair of nodes (i, j), we check if going through 'k' 
     (i -> k -> j) is cheaper than the direct route (i -> j).

4. WHY IS IT USEFUL?
   - **Network Optimization**: Finding the best communication routes 
     between every single computer in a cluster.
   - **Transitive Closure**: Finding out "Who knows whom" in a large 
     social network.
   - **Shortest Path Problems**: When you need a lookup table for all 
     distances and don't want to run Dijkstra's a million times.

5. REAL LIFE EXAMPLE:
   Think of **TRANS-CONTINENTAL FLIGHTS**. 
   You want to find the cheapest way to fly between any two cities in the world. 
   Floyd-Warshall looks at every city (like New York, London, Tokyo) and asks: 
   "Is it cheaper to fly direct from Paris to Sydney, or is it cheaper 
   to fly Paris -> London -> Sydney?" It repeats this for EVERY city until 
   it finds the absolute cheapest ticket for any possible trip!
================================================================================
"""

def floyd_warshall(M):
    """
    Computes all-pairs shortest paths on adjacency matrix M.
    M: a 2D grid where M[i][j] is the edge weight from i to j.
    """
    # 1. n: number of vertices (dimension of the square matrix M)
    n = len(M) # n = total nodes
    
    # 2. D: distance matrix (we copy M to use as a starting point)
    # Using list slicing [:] to create a true deep copy of each row
    D = [row[:] for row in M] # D = distance grid
    
    # 3. Triple Nested Loops (The Core k-i-j logic)
    # Iterates exactly n*n*n times = O(V^3)
    
    # k: our "stopover" or intermediate vertex index
    for k in range(n):
        # i: starting vertex index
        for i in range(n):
            # j: destination vertex index
            for j in range(n):
                # 4. Fundamental Check: Is going (i -> k -> j) a better shortcut?
                # If d(i,k) + d(k,j) is smaller than current best d(i,j)
                if D[i][k] + D[k][j] < D[i][j]:
                    # 5. Update the distance table with the new cheaper shortcut
                    D[i][j] = D[i][k] + D[k][j] # relax the edge
                    
    # 6. Return the final table of shortest all-to-all paths
    return D

# ================================================================================
# COMPACT FLOYD-WARSHALL (MINIMAL CODE)
# ================================================================================

def compact_fw(M):
    """ M: 2D matrix. Returns shortest all-to-all path matrix. """
    n = len(M) # n = vertices
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # direct in-place update using min()
                M[i][j] = min(M[i][j], M[i][k] + M[k][j])
    return M # return modified matrix

# --- START OF PROGRAM ---

# INF: helper for disconnected nodes (no road exists)
INF = float('inf')

# M_init: initial adjacency matrix showing direct road costs
# 4 nodes (0-3)
M_init = [
    [0,   3,   INF, 5],   # Start from node 0
    [2,   0,   INF, 4],   # Start from node 1
    [INF, 1,   0,   INF], # Start from node 2
    [INF, INF, 2,   0]    # Start from node 3
]

print("Floyd-Warshall All-Pairs Path Finder!\n")

# Run calculation
dist_tab = floyd_warshall(M_init)

# Print results
print("Shortest Paths Matrix [From][To]:")
for row_idx, row_vals in enumerate(dist_tab):
    # format output for readability
    print(f"Node {row_idx}: {row_vals}")

# Compact version test
print(f"\nCompact code result (Node 0 row): {compact_fw([r[:] for r in M_init])[0]} ✅")
