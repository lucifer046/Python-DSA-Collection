"""
================================================================================
CONCEPTS AND THEORY: MST VIA DIJKSTRA'S LOGIC (THE UNIFIED GREEDY APPROACH)
================================================================================

This module demonstrates how Prim's and Kruskal's MST algorithms share a 
foundational DNA with Dijkstra's Shortest Path algorithm. 

1. THE 'DISTANCE' DEFINITION:
   - DIJKSTRA: Distance to a node is the CUMULATIVE cost from the SOURCE.
   - PRIM:     Distance to a node is the LOCAL cost of the cheapest edge 
               connecting it to the GROWING TREE.
   - KRUSKAL:  Distance is simply the weight of the cheapest edge globally 
               that doesn't form a cycle.

2. THE PQ-DRIVEN ENGINE:
   All three algorithms can be driven by a Priority Queue (Min-Heap) that 
   always processes the 'cheapest' next option.

STATUS: BRIDGE MODULE (Shows the structural connection between algorithms)
================================================================================
"""

import heapq

def prim_mst_dijkstra_style(G, start_node=0):
    """
    Prim's Algorithm implemented with the EXACT structure of Dijkstra.
    Logic: At each step, we expand our tree by picking the cheapest edge
    that connects a node inside the tree to one outside the tree.
    """
    n = len(G)
    visited = [False] * n
    
    # 1. Distance Tracker (The Dijkstra Scoreboard)
    # d[v] stores the cost of the single CHEAPEST edge connecting v to our MST.
    # In Dijkstra, this would be the cumulative path cost from the start.
    d = [float('inf')] * n
    d[start_node] = 0
    
    # 2. Priority Queue (The Greedy Engine)
    # Stores tuples of (edge_weight, target_node)
    pq = [(0, start_node)] 
    
    total_cost = 0
    mst_edges = []
    parent = [-1] * n # To reconstruct the actual tree structure

    while pq:
        # Pick the node 'u' that is 'closest' to our existing tree
        cost_u, u = heapq.heappop(pq)
        
        # If we've already included 'u' in our MST, ignore it
        if visited[u]: continue
        
        # 3. Expansion Step
        # Mark as visited and add the edge cost to our total
        visited[u] = True
        total_cost += cost_u
        if parent[u] != -1:
            mst_edges.append((parent[u], u, cost_u))

        # 4. The 'Relaxation' Loop (Dijkstra-Style)
        # Check all neighbors 'v' of the newly added node 'u'
        for v, w in G[u]:
            if not visited[v]:
                # THE LOGIC BRIDGE:
                # - Dijkstra would check: if d[v] > d[u] + w (Cumulative)
                # - Prim checks:        if d[v] > w       (Local Edge Only)
                if d[v] > w:
                    d[v] = w # Update v's best connection to the tree
                    parent[v] = u
                    heapq.heappush(pq, (d[v], v))
                    
    return total_cost, mst_edges

def kruskal_mst_pq_style(G):
    """
    Kruskal's Algorithm using a Priority Queue to drive greedy edge selection.
    Logic: Process every edge in the graph from cheapest to most expensive,
    adding them to the MST as long as they don't create a cycle.
    """
    n = len(G)
    
    # 1. Flatten all undirected edges into a Priority Queue
    # This represents the 'Global Greedy' strategy shared with Dijkstra.
    pq = []
    for u in range(n):
        for v, w in G[u]:
            if u < v: # Only add each edge once (u-v is same as v-u)
                heapq.heappush(pq, (w, u, v))
    
    # 2. Component Tracking (Cycle Detection Logic)
    # Initially, every node is its own separate island (component).
    comp = list(range(n))

    # 3. The Greedy Loop
    total_cost = 0
    mst_edges = []
    
    # We stop when we have enough edges (n-1) to connect everything
    while pq and len(mst_edges) < n - 1:
        # Pop the CHEAPEST edge available globally
        w, u, v = heapq.heappop(pq)
        
        # 4. The 'No-Cycle' Check
        # If u and v are in different components, adding (u, v) is safe!
        if comp[u] != comp[v]:
            total_cost += w
            mst_edges.append((u, v, w))
            
            # 5. Component Merge
            # Update all nodes in v's component to have u's component ID.
            # This 'unites' the two groups.
            old_id, new_id = comp[v], comp[u]
            for i in range(n):
                if comp[i] == old_id:
                    comp[i] = new_id
            
    return total_cost, mst_edges


# --- COMPARISON DEMONSTRATION ---

if __name__ == "__main__":
    # Sample Graph (same as used in individual tutorials)
    # (neighbor, weight)
    graph = [
        [(1, 2), (3, 6)],                    # Node 0
        [(0, 2), (2, 3), (3, 8), (4, 5)],    # Node 1
        [(1, 3), (3, 7)],                    # Node 2
        [(0, 6), (1, 8), (2, 7), (4, 1)],    # Node 3
        [(1, 5), (3, 1)]                     # Node 4
    ]

    print("=== MST Algorithms via Dijkstra Logic ===\n")

    # 1. Test Prim (Dijkstra-Style)
    p_cost, p_edges = prim_mst_dijkstra_style(graph)
    print(f"Prim's MST Cost: {p_cost}")
    print(f"Edges: {p_edges}\n")

    # 2. Test Kruskal (PQ-Style)
    k_cost, k_edges = kruskal_mst_pq_style(graph)
    print(f"Kruskal's MST Cost: {k_cost}")
    print(f"Edges: {k_edges}")

    print("\nObservation: Both algorithms use a Min-Heap to greedily select the")
    print("'cheapest' option next, just like Dijkstra's Shortest Path!")
