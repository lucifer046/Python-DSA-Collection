"""
================================================================================
CONCEPTS AND THEORY: TOPOLOGICAL SORT (THE 'TASK SCHEDULER' METHOD)
================================================================================

--- TIME COMPLEXITY ANALYSIS ---
- ADJACENCY LIST (Kahn's/DFS): O(V + E) (Visit every vertex and every edge once)
- ADJACENCY MATRIX:            O(V^2) (Must scan all columns for each node)
- BEST/AVG/WORST CASE:        O(V + E) (For the list-based versions)
--------------------------------
- SPACE COMPLEXITY: O(V) (Required for in-degree tracker and the result list)

STATUS: INDEPENDENT (Contains Adjacency List, Matrix, and Compact versions)
================================================================================

1. WHAT IS TOPOLOGICAL SORT?
   Imagine you are building a house. You cannot build the ROOF until 
   the WALLS are up. You cannot build the walls until the FOUNDATION 
   is poured. 
   Topological Sort is an algorithm that finds a 'legal' order to do 
   tasks such that every task happens AFTER its requirements (dependencies).

2. THE 'IN-DEGREE' CONCEPT:
   The key to this algorithm is 'In-degree'. 
   - **IN-DEGREE**: The number of arrows pointing TOWARDS a node. 
   - If a node has an in-degree of 2, it means it has 2 prerequisites 
     that MUST be finished first.
   - If a node has an in-degree of 0, it is **READY TO START**!

3. KAHN'S ALGORITHM (THE LIST VERSION):
   - 1. Count the in-degree for every task.
   - 2. Find all tasks with **0 In-degree** and put them in a 'Ready' Queue.
   - 3. Remove a task from the Queue and 'finish' it.
   - 4. Lower the in-degree of its neighbors (because you finished their prerequisite!).
   - 5. If a neighbor now has 0 in-degree, add them to the 'Ready' Queue.

4. WHY IS IT USEFUL?
   - **University Degrees**: Planning which courses to take in which semester.
   - **Software Build Tools**: Compiling code in the correct order so that 
     a library is built before the app that uses it.
   - **Project Management**: Determining the 'Critical Path' of a project.

5. REAL LIFE EXAMPLE:
   Think of **GETTING DRESSED** in the morning. 
   - You have tasks: Socks, Shoes, Pants, Shirt.
   - Dependency: Socks must be on before Shoes. Pants must be on before Shoes.
   - Topological Sort would suggest: [Socks, Pants, Shirt, Shoes]. 
   - It would NEVER suggest: [Shoes, Socks] because that's impossible!
================================================================================
"""

import queue # q: standard python queue module
import numpy as np # np: numeric library for matrices

# ================================================================================
# VERSION 1: KAHN'S ALGORITHM (ADJACENCY LIST)
# ================================================================================

def topo_list(G):
    """
    Kahn's Algorithm for topological sorting.
    G: adjacency list graph dictionary {task: [deps]}
    """
    # 1. d: dictionary to track in-degree (dependency count) for each task
    d = {node: 0 for node in G} # d = dependency tracker
    
    # 2. pre: final ordered sequence of tasks (result list)
    res = [] # res = result sequence
    
    # 3. Calculate in-degree for each node n in G
    for u in G: # u: parent task
        for v in G[u]: # v: dependent task
            d[v] += 1 # increment in-degree of the child v
            
    # 4. q: Queue for tasks that are "Ready to Start" (In-degree = 0)
    q1 = queue.Queue() # q1 = ready queue
    for task in G:
        if d[task] == 0:
            q1.put(task) # add ready tasks to the queue
            
    # 5. Scheduling Loop
    while not q1.empty():
        # curr: current task being finished
        curr = q1.get()
        res.append(curr) # add to final order
        
        # 6. Unlock neighbors - reduce prerequisite count for children
        for child in G[curr]: # child: task depending on curr
            d[child] -= 1 # one prerequisite fulfilled
            if d[child] == 0:
                q1.put(child) # child is now ready to start
                
    # 7. Return the final sorted sequence
    return res

# ================================================================================
# VERSION 2: MATRIX-BASED SORT
# ================================================================================

def topo_matrix(M):
    """ M: 2D adjacency grid. Returns topological order indices. """
    # 1. n: grid dimension (vertices)
    n = M.shape[0] # n = number of rows
    d = {} # d: in-degree mapping
    res = [] # res: resulting order list
    
    # 2. Calculate column sums (in-degrees)
    for c in range(n): # c: column iterator (target task)
        d[c] = sum(1 for r in range(n) if M[r, c] == 1) # r: row (source)
            
    # 3. Greedy selection Loop
    for _ in range(n):
        # 4. ready: indices with 0 prerequisites
        ready = [i for i in range(n) if d.get(i) == 0]
        if not ready: break # cycle detected or finished
        
        # 5. s: pick first ready task
        s = min(ready) # s = selected task
        res.append(s)
        d[s] = -1 # remove from consideration
        
        # 6. Update neighbor counts in the row of s
        for v in range(n): # v: potential neighbor index
            if M[s, v] == 1: d[v] -= 1
                
    return res

# ================================================================================
# VERSION 3: COMPACT DFS VERSION
# ================================================================================

def compact_topo(G):
    """ G: graph dict. DFS-based topological sort. """
    v, s = set(), [] # v: visited set, s: stack list
    def visit(n):
        if n not in v:
            v.add(n)
            for m in G.get(n, []): visit(m) # visit neighbors first
            s.append(n) # push node after neighbors are done
    for node in G: visit(node) # visit every node
    return s[::-1] # reverse stack for correct order

# --- START OF PROGRAM ---

# G1: sample Directed Acyclic Graph (DAG) for tasks
G1 = {0: [2, 3, 4], 1: [2, 7], 2: [5], 3: [5, 7], 4: [7], 5: [6], 6: [7], 7: []}

print("Topological Sort Simulator (The Task Scheduler)!\n")

print("--- Testing Adjacency List Kahn's Algorithm ---")
res1 = topo_list(G1)
print(f"Correct Sequence: {res1} ✅\n")

# M1: matrix version of G1
M1 = np.zeros(shape=(8, 8))
edges = [(0,2), (0,3), (0,4), (1,2), (1,7), (2,5), (3,5), (3,7), (4,7), (5,6), (6,7)]
for u, v in edges: M1[u, v] = 1 # u -> v edge

print("--- Testing Adjacency Matrix Algorithm ---")
res2 = topo_matrix(M1)
print(f"Correct Sequence Indices: {res2} ✅\n")

# Run compact version
print("--- Testing Compact DFS Version ---")
res3 = compact_topo(G1)
print(f"Compact Order result: {res3} ✅")
