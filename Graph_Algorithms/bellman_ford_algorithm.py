"""
================================================================================
CONCEPTS AND THEORY: BELLMAN-FORD (THE 'NEGATIVE WEIGHT' SPECIALIST)
================================================================================

--- TIME COMPLEXITY ANALYSIS ---
- BEST CASE:    O(E) (If no paths change during the first pass)
- AVERAGE CASE: O(V * E) 
- WORST CASE:   O(V * E) (Must relax all edges exactly V-1 times)
--------------------------------
- SPACE COMPLEXITY: O(V) (To store a distance table for every vertex)

STATUS: INDEPENDENT (Contains both a full and a compact version)
================================================================================

1. WHAT IS BELLMAN-FORD?
   Dijkstra's algorithm is fast, but it gets very confused if an edge 
   has a NEGATIVE weight (like a road that pays you to drive on it!). 
   Bellman-Ford is the slower but SMARTER brother that can handle 
   negative weights easily.

2. THE 'RELAXATION' TRICK ( (n-1) TIMES ):
   - 1. We start by assuming the distance to everyone is Infinity.
   - 2. We check every single edge (u, v) and ask: 
        "Is going from u to v shorter than our current best for v?"
   - 3. We repeat this process exactly (num_vertices - 1) times. 
   - 4. Why n-1? Because the longest possible simple path between any 
        two nodes in a graph with 'n' nodes can only have 'n-1' edges!

3. DETECTING 'INFINITE MONEY' (NEGATIVE CYCLES):
   A major feature of Bellman-Ford is finding **NEGATIVE CYCLES**. 
   If we can *still* find a shorter path after (n-1) tries, it means 
   there is a loop that keeps getting smaller and smaller forever. 
   In this case, a 'shortest' path is impossible to calculate!

4. WHY IS IT USEFUL?
   - **Financial Arbitrage**: Finding a loop of currency exchanges 
     (USD -> EUR -> GBP -> USD) that results in a tiny profit. 
     This is literally a Negative Cycle!
   - **Distance Vector Protocols (RIP)**: How routers on the internet 
     learn about the best paths to send your data.

5. REAL LIFE EXAMPLE:
   Think of a **GAME WITH BONUSES AND PENALTIES**. 
   - Most squares take your 'energy' (Weight 10). 
   - Some 'Bonus' squares give you energy (Weight -5). 
   - If there is a loop of squares that lets you gain INFINITE energy, 
     Bellman-Ford will wave a red flag and say, "Wait, this is an 
     illegal infinite loop!" 

6. THE GOLDEN RULE (NEGATIVES):
   - **Negative Weights?** YES ✅! This algorithm is specifically built 
     to handle edges that subtract cost (unlike Dijkstra's).
   - **Negative Cycles?** NO ❌. If there is a loop that keeps decreasing 
     the total cost forever, a "shortest" path doesn't actually exist 
     (it would be -Infinity). Bellman-Ford will detect this and raise 
     a red flag instead of giving a wrong answer.
================================================================================
"""

def bellman_ford(E, n, s):
    """
    Finds shortest paths from source s in graph with n nodes.
    E: list of edges (u, v, w) where u -> v with weight w
    """
    # 1. d: distance tracker for all n node indices
    # set to Infinity initially as we don't know the shortest paths yet
    d = [float('inf')] * n # d = distance result list
    d[s] = 0 # distance to starting node is always 0
    
    # 2. Outer loop: relax all edges for (n-1) iterations
    # the longest possible gap-free path has n-1 edges
    for i in range(n - 1): # i: iteration counter
        # 3. Inner loop: evaluate every single road (edge) in the graph
        for u, v, w in E: # u: source, v: destination, w: edge weight
            # 4. Check if reaching v via u is a better shortcut
            if d[u] != float('inf') and d[v] > d[u] + w:
                d[v] = d[u] + w # update v's best known distance
    
    # 5. Safety check: one final pass to detect negative cycles (infinite loops)
    for u, v, w in E:
        # if a path can STILL be shortened, we have a negative cycle
        if d[u] != float('inf') and d[v] > d[u] + w:
            print("ERROR: Negative cycle detected! 🚩")
            return None # no stable shortest path exists
    
    # 6. Return the final distances to all nodes
    return d

# ================================================================================
# COMPACT BELLMAN-FORD (MINIMAL CODE)
# ================================================================================

def compact_bf(E, n, s):
    """ E: edges, n: node count, s: start. Minimal implementation. """
    # d: result distances
    d = [float('inf')] * n; d[s] = 0
    # relax n-1 times
    for _ in range(n - 1):
        for u, v, w in E: d[v] = min(d[v], d[u] + w)
    # verify stability (no cycles)
    if any(d[u] + w < d[v] for u, v, w in E if d[u] != float('inf')):
        return "Cycle Found!"
    return d # returning mapping of all distances

# --- START OF PROGRAM ---

# E: sample graph as a list of directed edges (u, v, weight)
E = [
    (0, 1, 4), (0, 2, 2), (1, 2, 1), 
    (1, 3, 5), (2, 3, 8), (2, 4, 10), (3, 4, 2)
]

print("Bellman-Ford Shortest Path Search (Negative Weight Proof)!\n")

# Run calculation
start_node = 0
v_count = 5
distances = bellman_ford(E, v_count, start_node)

if distances:
    print(f"Distances from starting node {start_node}:")
    for idx, dist_val in enumerate(distances):
        print(f"  To {idx}: Distance {dist_val}")

# Run compact version
c_dist = compact_bf(E, v_count, start_node)
print(f"\nCompact code result: {c_dist} ✅")
