"""
================================================================================
CONCEPTS AND THEORY: BREADTH-FIRST SEARCH (LAYER-BY-LAYER EXPLORATION)
================================================================================

--- TIME COMPLEXITY ANALYSIS ---
- ADJACENCY LIST (Best/Avg/Worst): O(V + E) (Visit every vertex and every edge)
- ADJACENCY MATRIX (Best/Avg/Worst): O(V^2) (Must scan All V columns for each node)
--------------------------------
- SPACE COMPLEXITY: O(V) (Requires space for the 'visited' tracker and Queue)

STATUS: INDEPENDENT (Contains Adjacency List, Matrix, and Compact versions)
================================================================================

1. WHAT IS BREADTH-FIRST SEARCH (BFS)?
   Imagine you drop a stone in a pond. Ripples spread outwards in perfect 
   circles. BFS is exactly like those ripples! 
   It explores a graph by visiting every neighbor at the current distance 
   before moving one step further away.

2. THE 'QUEUE' STRATEGY:
   BFS is a 'First-Come, First-Served' algorithm. 
   - We use a **QUEUE** to remember which nodes to visit next. 
   - When we visit a node, we look at all its neighbors and add them to 
      the BACK of the line.

3. TWO WAYS TO REPRESENT A GRAPH:
   - 1. **ADJACENCY LIST**: A dictionary where each person (Node) has a 
        list of their friends (Neighbors). This is fast and uses less memory.
   - 2. **ADJACENCY MATRIX**: A 2D grid/table. If there's a '1' at Row A 
        and Column B, it means A and B are connected.

4. WHY IS IT USEFUL?
   - **Shortest Path**: BFS is the best way to find the shortest path 
     between two points in a simple network (like a subway map).
   - **Social Networks**: Finding "Friends of Friends" or "People You 
     May Know".

5. REAL LIFE EXAMPLE:
   Think of **SPREADING A RUMOR**. 
   - You tell your 3 best friends a secret (Layer 1). 
   - Then *each* of them tells their 3 best friends (Layer 2). 
   - The news spreads in layers. BFS follows this exact pattern!
================================================================================
"""

import queue # q: standard python queue module
import numpy as np # np: numerical python library

# ================================================================================
# VERSION 1: BFS FOR ADJACENCY LIST (USING DICTIONARY)
# ================================================================================

def bfs_list(G, s):
    """
    Breadth-First Search on an Adjacency List.
    G: graph dictionary, s: start node
    """
    # 1. Initialize 'seen' tracker for every node in the graph
    v = {node: False for node in G} # v: visited tracker dictionary
    
    # 2. q: Queue for the 'Waiting Line' (FIFO)
    q1 = queue.Queue() # q1: nodes queue
    
    # 3. Start: Mark starting node s as seen and enqueue it
    v[s] = True # mark s as visited
    q1.put(s) # add s to queue
    
    # 4. Explore until the queue is empty
    while not q1.empty(): # check if anyone is in line
        # 5. Take the person from the very front of the line
        curr = q1.get() # curr: current node being explored
        
        # 6. Look at all the neighbors (friends) of 'curr'
        for nbr in G[curr]: # nbr: neighbor node
            # 7. If this neighbor hasn't been seen yet:
            if not v[nbr]:
                v[nbr] = True # mark as visited
                q1.put(nbr) # add to the back of the line
                
    # 8. Return the final list of visited nodes
    return v

# ================================================================================
# VERSION 2: BFS FOR ADJACENCY MATRIX (USING GRID)
# ================================================================================

def get_nbrs(M, r):
    """ Helper to find neighbors in matrix M for row 'r'. """
    # M: 2D adjacency matrix, r: node index
    return [c for c in range(M.shape[1]) if M[r, c] == 1] # c: column/neighbor

def bfs_matrix(M, s):
    """
    Breadth-First Search on an Adjacency Matrix.
    M: adjacency grid, s: start node index
    """
    # 1. n: total nodes in the matrix
    n = M.shape[0] # n = number of rows
    
    # 2. v: tracker for visited node indices
    v = {i: False for i in range(n)} # i: index iterator
    
    # 3. q1: waiting line queue
    q1 = queue.Queue() # q1 = queue
    
    # 4. Initialize search at s
    v[s] = True
    q1.put(s)
    
    # 5. Exploration loop
    while not q1.empty():
        curr = q1.get() # curr: current node index
        # 6. Search for neighbors in matrix row for curr
        for nbr in get_nbrs(M, curr): # nbr: neighbor index
            if not v[nbr]:
                v[nbr] = True
                q1.put(nbr)
                
    # 7. Return mapping of visited status
    return v

# ================================================================================
# VERSION 3: THE MOST COMPACT BFS
# ================================================================================

def compact_bfs(G, s):
    """
    Shortest BFS implementation using a simple list as a queue.
    G: graph, s: start node
    """
    # v: visited set, q: queue list
    v, q = {s}, [s] # v=set, q=list
    for n in q: # n: current node in walk
        for m in G[n]: # m: next neighbor
            if m not in v:
                v.add(m); q.append(m) # seen it, add to search
    return q # return discovery order

# --- START OF PROGRAM ---

# G1: sample graph with 5 vertices (0-4)
G1 = {0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: []}

print("--- Testing BFS with Adjacency List ---")
res1 = bfs_list(G1, 0)
print(f"Nodes reached: {res1} ✅\n")

# M1: same graph as a 2D Matrix (Numpy result)
M1 = np.zeros(shape=(5, 5))
edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (2, 3), (3, 4)]
for r, c in edges: M1[r, c] = 1 # r: row, c: col

print("--- Testing BFS with Adjacency Matrix ---")
res2 = bfs_matrix(M1, 0)
print(f"Nodes reached (Matrix): {res2} ✅\n")

# Run compact version
print("--- Testing Compact BFS ---")
res3 = compact_bfs(G1, 0)
print(f"Discovery Order: {res3} ✅")
