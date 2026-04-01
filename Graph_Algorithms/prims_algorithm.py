"""
================================================================================
CONCEPTS AND THEORY: PRIM'S ALGORITHM (THE 'GREEDY TREE' BUILDER)
================================================================================

--- TIME COMPLEXITY ANALYSIS ---
- BEST CASE:    O(E log V) (Using a Binary Heap/Priority Queue)
- AVERAGE CASE: O(E log V) 
- WORST CASE:   O(V^2) (In this simple implementation using basic loops)
--------------------------------
- SPACE COMPLEXITY: O(V + E) (Requires space for graph and visited tracker)

STATUS: INDEPENDENT (Contains both a full and a compact implementation)
================================================================================

1. WHAT IS PRIM'S ALGORITHM?
   Imagine you are building a social network. You want a way to connect 
   *everyone* together with the shortest possible length of cable. 
   **Prim's Algorithm** is the perfect tool for creating a 
   **Minimum Spanning Tree (MST)**.

2. THE 'MST' CONCEPT:
   - **MINIMUM**: The cheapest total budget.
   - **SPANNING**: Reaches *every* single node in the graph.
   - **TREE**: No cycles (infinite loops) in the connections.

3. THE 'GROW FROM A SEED' STRATEGY:
   Prim's is 'Greedy' and starts from a single node (like a seed).
   - 1. Pick a starting node.
   - 2. Find the smallest edge that connects a node we already 
        visit to a node we haven't visited yet.
   - 3. Add that new node to our 'Seen' list.
   - 4. Repeat until everyone is connected!

4. WHY IS IT USEFUL?
   - **Electricity Grid Layout**: Connecting every house in a city 
     with the minimum amount of power cable.
   - **Computer Networks**: Designing a layout for routers in a 
     building so everyone is connected with minimum fiber optic cabling.

5. REAL LIFE EXAMPLE:
   Think of **WATER PIPELINES**. 
   If you have a map of 10 towns (Nodes) and the cost to lay pipes 
   between them (Weights), Prim's helps the government find the 
   cheapest way to un-dry every town by starting with one town 
   with water and slowly connecting the 'closest' town next to it 
   until everyone has a pipeline!
================================================================================
"""

def prim_mst(G):
    """
    Prim's algorithm to find Minimum Spanning Tree cost.
    G: adjacency list [ (nbr, weight), ... ]
    """
    # 1. n: total number of vertices (nodes) in the graph G
    n = len(G) # n = nodes count
    
    # 2. v: tracker for nodes already included in our MST
    v = [False] * n # v = visited list
    v[0] = True # start with node 0 as our "seed"
    
    # 3. tc: total cost budget for all connections in MST
    tc = 0 # tc = total cost
    
    # 4. Growth loop: we need exactly n-1 edges to connect n nodes
    # i: edge counter iterator
    for i in range(n - 1):
        # 5. min_w: smallest edge weight found connecting a seen node to an unseen node
        min_w = float('inf') # start with infinity
        nxt = -1 # nxt: index of the next node to add
        
        # 6. Outer loop: scan every node 'u' that is already in our tree
        for u in range(n):
            if v[u]: # if u is part of our growing tree
                # 7. Inner loop: check every neighbor 'nbr' of 'u'
                for nbr, w in G[u]: # w: edge weight from u to nbr
                    # 8. Greedy Selection: check if nbr is new and edge is cheapest
                    if not v[nbr] and w < min_w:
                        min_w = w # update the smallest cost
                        nxt = nbr # mark nbr as the candidate to join
        
        # 9. Add the cheapest neighbor found to our tree
        if nxt != -1:
            tc += min_w # add edge weight to total budget
            v[nxt] = True # mark nxt as part of the family
            
    # return the final MST construction cost
    return tc

# ================================================================================
# COMPACT PRIM (USING PRIORITY QUEUE)
# ================================================================================

def compact_prim(G):
    """ G: adjacency list. Returns MST cost using a heap. """
    import heapq
    # tc: total cost, s: seen set, pq: priority queue (weight, node)
    tc, s, pq = 0, {0}, [(w, nbr) for nbr, w in G[0]]
    heapq.heapify(pq) # order by weights
    while pq and len(s) < len(G):
        w, u = heapq.heappop(pq)
        if u not in s:
            s.add(u); tc += w
            for v, next_w in G[u]:
                if v not in s: heapq.heappush(pq, (next_w, v))
    return tc # final budget calculation

# --- START OF PROGRAM ---

# G: sample graph (0-4 towns connected by pipes)
# (neighbor_id, cost)
G = [
    [(1, 2), (3, 6)],                    # Node 0
    [(0, 2), (2, 3), (3, 8), (4, 5)],    # Node 1
    [(1, 3), (3, 7)],                    # Node 2
    [(0, 6), (1, 8), (2, 7), (4, 1)],    # Node 3
    [(1, 5), (3, 1)]                     # Node 4
]

print("Prim's MST Budget Calculator!\n")

# Run calculation
total_budget = prim_mst(G)
print(f"Minimum budget to connect all towns: ${total_budget} 💰")

# Run compact version
c_budget = compact_prim(G)
print(f"Compact result check: ${c_budget} ✅")
