"""
================================================================================
CONCEPTS AND THEORY: BELLMAN-FORD (THE 'NEGATIVE WEIGHT' SPECIALIST)
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
================================================================================
"""

def find_shortest_paths_bellman_ford(edge_list, total_vertices, starting_node):
    """
    Finds the cheapest path to ALL nodes, even with negative edge weights.
    """
    # 1. INITIALIZATION: Everyone starts at Infinity distance
    # 'dist_tracker' stores the best cost to reach each node (Index 0 to total_vertices-1)
    dist_tracker = [float('inf')] * total_vertices
    # Distance to our start is 0
    dist_tracker[starting_node] = 0
    
    # 2. THE REPETITION LOOP: We relax all edges (total_vertices - 1) times
    # Each pass 'unlocks' the shortest route to more distant nodes
    for iteration_count in range(total_vertices - 1):
        # 3. SCAN EVERY EDGE:
        for source_node, neighbor_node, edge_weight in edge_list:
            # CHECK: "Is reaching the neighbor through this source shorter 
            # than their current best path?"
            if dist_tracker[source_node] != float('inf') and \
               dist_tracker[neighbor_node] > dist_tracker[source_node] + edge_weight:
                
                # YES! Update the new shorter distance
                dist_tracker[neighbor_node] = dist_tracker[source_node] + edge_weight
    
    # 3. THE CYCLE CHECK (Final Pass): 
    # If we can STILL find a shorter path, it means we have a Negative Cycle!
    for source_node, neighbor_node, edge_weight in edge_list:
        if dist_tracker[source_node] != float('inf') and \
           dist_tracker[neighbor_node] > dist_tracker[source_node] + edge_weight:
            return ["ERROR: Found a Negative Cycle! Path is undefined."]
    
    # 4. Return the finally calculated BEST distances from our starting point
    return dist_tracker

# ================================================================================
# VERSION 2: THE MOST COMPACT & SHORTEST WAY
# ================================================================================

def bellman_ford_shortest_code(edges, n, start):
    """
    Very short implementation focusing on the logic core.
    """
    dist = [float('inf')] * n
    dist[start] = 0
    
    # Relax (n-1) times
    for _ in range(n - 1):
        for u, v, w in edges:
            dist[v] = min(dist[v], dist[u] + w)
            
    # One more check for cycles
    if any(dist[v] > dist[u] + w for u, v, w in edges):
        return "Cycle Found!"
        
    return dist

# --- START OF PROGRAM ---

# 1. Our graph represented as a LIST of EDGES (u -> v with weight w)
# Node labels: 0, 1, 2, 3, 4
sample_edges = [
    (0, 1, 4),      # Edge from 0 to 1, costs 4
    (0, 2, 2),      # Edge from 0 to 2, costs 2
    (1, 2, 1),      # Edge from 1 to 2, costs 1
    (1, 3, 5),      # Edge from 1 to 3, costs 5
    (2, 3, 8),      # Edge from 2 to 3, costs 8
    (2, 4, 10),     # Edge from 2 to 4, costs 10
    (3, 4, 2),      # Edge from 3 to 4, costs 2
]

print("Welcome to the Bellman-Ford Shortest Path Solver!")

# 2. Run the search
num_nodes = 5
start_point = 0
results = find_shortest_paths_bellman_ford(sample_edges, num_nodes, start_point)

# 3. Print the results
print(f"\nShortest distances from Node {start_point}:")
if isinstance(results, list):
    for node_id, final_dist in enumerate(results):
        print(f"  -> Path to Node {node_id}: Distance {final_dist}")
else:
    print(results)

# --- TEST SHORTEST VERSION ---
print("\nShortest implementation result:")
print(bellman_ford_shortest_code(sample_edges, num_nodes, start_point))
