"""
================================================================================
CONCEPTS AND THEORY: DIJKSTRA'S ALGORITHM (THE 'SMARTEST PATH' FINDER)
================================================================================

--- TIME COMPLEXITY ANALYSIS ---
- BEST CASE:    O(E + V log V) (Matches the average case efficiency)
- AVERAGE CASE: O(E log V) (Using a Priority Queue/Min-Heap)
- WORST CASE:   O(V^2) (If implemented using a simple list as a queue)
--------------------------------
- SPACE COMPLEXITY: O(V + E) (Requires space for graph and distance tracker)

STATUS: INDEPENDENT (Contains both a full and a compact implementation)
================================================================================

1. WHAT IS IT?
   Dijkstra's algorithm is the gold standard for finding the SHORTEST 
   distance between two points in a graph where every road (edge) has 
   a COST (weight).

2. THE GREEDY STRATEGY:
   Dijkstra is 'Greedy'. It always picks the closest known node and 
   checks if going through it would provide a shorter shortcut to 
   other nodes. 

3. THE 'RELAXATION' MOVE:
   Imagine you thought it took 10 mins to get to City B. But then you 
   find a path through City C that takes only 7 mins. You 'relax' your 
   expectation and update the time to 7. This is what Dijkstra does!

4. LIMITATIONS:
   Dijkstra CANNOT handle negative road costs (negative edge weights). 
   If a road somehow 'gave you back time', Dijkstra would get confused.

5. WHY IS IT USEFUL?
   - **GPS Navigation**: This is exactly how Google Maps or Apple Maps 
     finds the fastest way to your destination!
   - **Network Routing**: Deciding how data should travel through the 
     internet to reach you as fast as possible.

6. REAL LIFE EXAMPLE:
   Think of a **COMMUTER TRAIN MAP**. 
   Every station is a Node, and the time between stations is the Weight. 
   Dijkstra starts at your home station, looks at all the immediate 
   stops, and keeps picking the 'earliest' arrivals until it finds 
   the fastest possible route to your office.
================================================================================
"""

from heapq import heappop, heappush # priority queue tools: min-heap

def dijkstra(G, s, t):
    """
    Finds shortest path from s to t in graph G.
    G: adjacency list [ (nbr, weight), ... ], s: start, t: target
    """
    # 1. n: total number of vertices in G
    n = len(G) # n = vertices count
    
    # 2. p: parent map to trace the final route sequence
    p = {} # p[child] = parent
    
    # 3. d: tracker for current best distance to each node
    # set to Infinity initially as we don't know the routes yet
    d = [float('inf')] * n # d = distances list
    d[s] = 0 # distance to start point is 0
    
    # 4. pq: Priority Queue (Heap) stores tuples of (distance, node)
    pq = [(0, s)] # pq = min-heap priority queue
    
    # 5. Greedy Search Loop
    while pq:
        # popped node 'u' is the closest unvisited node
        # d_curr: current distance from s to u
        d_curr, u = heappop(pq)
        
        # early exit: if we reached the target t, we can stop
        if u == t: return d_curr, p
        
        # 6. Relaxation loop for neighbors 'v' of node 'u'
        for v, w in G[u]: # v: neighbor node index, w: edge weight
            # d_new: potential shorter distance to v via u
            d_new = d_curr + w 
            
            # if d_new is better than previously known best for v
            if d[v] > d_new:
                d[v] = d_new # update best distance
                p[v] = u # mark u as the best 'parent' for v
                heappush(pq, (d_new, v)) # add to queue for exploration
                
    # return infinity if t is unreachable
    return float('inf'), p

def get_path(p, t):
    """ Rebuilds the path sequence from start to target 't'. """
    # p: parent mapping from dijkstra function
    pth = [] # pth = path list
    curr = t # curr = current node being traced back
    
    while curr in p:
        pth.append(curr)
        curr = p[curr] # step back to parent
        
    pth.append(curr) # add the start node
    return pth[::-1] # reverse list to get Start -> End order

# ================================================================================
# COMPACT DIJKSTRA (DISTANCES TO ALL NODES)
# ================================================================================

def compact_dijkstra(G, s):
    """ G: graph, s: source node. Returns all shortest distances. """
    d = {n: float('inf') for n in range(len(G))} # d: distance mapping
    d[s], pq = 0, [(0, s)] # pq: priority queue
    while pq:
        dist_u, u = heappop(pq)
        if dist_u > d[u]: continue # skip stale entries
        for v, w in G[u]: # v: nbr, w: weight
            if d[u] + w < d[v]:
                d[v] = d[u] + w; heappush(pq, (d[v], v))
    return d # mapping of node indices to shortest distance

# --- START OF PROGRAM ---

# G: sample adjacency list graph
# Index -> list of (neighbor_id, cost)
G = [
    [(1, 4), (2, 2)],           # Node 0
    [(0, 4), (2, 1), (3, 5)],   # Node 1
    [(0, 2), (1, 1), (3, 8), (4, 10)], # Node 2
    [(1, 5), (2, 8), (4, 2)],   # Node 3
    [(2, 10), (3, 2)]           # Node 4
]

print("Dijkstra's Shortest Path Simulator!\n")

start_pt, end_pt = 0, 4
cost, parents = dijkstra(G, start_pt, end_pt)
path_res = get_path(parents, end_pt)

print(f"Shortest path from {start_pt} to {end_pt}:")
print(f"Route: {' -> '.join(map(str, path_res))}")
print(f"Total Cost: {cost} 🏁\n")

print("All-Nodes Distances (Compact Version):")
print(compact_dijkstra(G, 0))
