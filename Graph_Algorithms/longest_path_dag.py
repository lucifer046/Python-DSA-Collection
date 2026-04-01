"""
================================================================================
CONCEPTS AND THEORY: LONGEST PATH ON DAG (THE 'CRITICAL PATH' METHOD)
================================================================================

--- TIME COMPLEXITY ANALYSIS ---
- BEST CASE:    O(V + E) (Requires one full pass of the graph)
- AVERAGE CASE: O(V + E) 
- WORST CASE:   O(V + E) 
--------------------------------
- SPACE COMPLEXITY: O(V) (Requires space for in-degrees and the path length tracker)

STATUS: INDEPENDENT (Contains both a full and a compact implementation)
================================================================================

1. WHAT IS THE LONGEST PATH ON A DAG?
   A Directed Acyclic Graph (DAG) is like a "One-Way Street" system with 
   no loops. Finding the **Longest Path** tells us the furthest distance 
   we can travel from a starting point without ever turning back.

2. THE 'KAHN+DP' STRATEGY:
   This algorithm is a brilliant combination of two ideas:
   - 1. **Topological Sort (Kahn's)**: To ensure we finish every 
        prerequisite before calculating a task's path.
   - 2. **Dynamic Programming**: To 'remember' the longest path we 
        found to a node so far and update it if we find a longer one.

3. HOW IT WORKS:
   - Count the 'In-degree' (incoming arrows) of every node.
   - Start at the nodes with 0 arrows (The 'Beginning' tasks).
   - For every neighbor of a task:
     - Their longest path is: `MAX(their current path, your path + 1)`.
     - This means "To reach me, you must follow at least the longest 
       path that leads to any of my prerequisites."

4. WHY IS IT USEFUL?
   - **Critical Path Method (CPM)**: In construction, the "Longest Path" 
     of tasks determines the minimum time needed to finish the project. 
     If a task on the longest path is delayed, THE WHOLE HOUSE is delayed!
   - **Game Development**: Calculating the depth of a 'Technology Tree'.

5. REAL LIFE EXAMPLE:
   Think of **BUILDING A SPACESHIP**. 
   - You have many tasks: Engine (3 days), Cabin (5 days), Electronics (2 days).
   - Some can happen at the same time, but many have to wait for others. 
   - The "Longest Path" through this dependency map tells NASA exactly 
     when the rocket will be TRULY ready for launch.
================================================================================
"""

import queue # q: standard python queue module

def longest_path(G):
    """
    Kahn's Algorithm + Dynamic Programming for longest path in DAG G.
    G: adjacency list {task: [deps]}
    """
    # 1. d: dependency tracker (in-degree) for all vertices
    d = {node: 0 for node in G} # d = dictionary
    
    # 2. L: longest path tracker stores length to reach each node
    L = {node: 0 for node in G} # L = longest path map
    
    # 3. Calculate in-degrees for each node n in G
    for u in G: # u: source parent task
        for v in G[u]: # v: target dependent task
            d[v] += 1 # increment v's prerequisite count
            
    # 4. q: Queue for nodes that are "Ready to Process" (In-degree = 0)
    q1 = queue.Queue() # q1 = ready queue
    for task in G:
        if d[task] == 0:
            q1.put(task) # add starting tasks to queue
            
    # 5. The Computing Loop
    while not q1.empty():
        # curr: current task being processed
        curr = q1.get()
        # logically skip prerequisite counts for children of curr
        d[curr] -= 1 
        
        # 6. Relax neighbors using Dynamic Programming (max search)
        for child in G[curr]: # child: node depending on curr
            # 7. Decrease child's dependency count
            d[child] -= 1
            
            # 8. Path calculation: compare current path to new path via 'curr'
            # path to child is at least (path to curr + 1) index jump
            L[child] = max(L[child], L[curr] + 1) # keep the longest distance
            
            # 9. If child has no pending prerequisites, add to ready queue
            if d[child] == 0:
                q1.put(child) # child is now ready for path calculation
                
    # 10. Return the final length of the longest path to each node
    return L

# ================================================================================
# COMPACT LONGEST PATH (TOPOLOGICAL BASED)
# ================================================================================

def compact_lp(G):
    """ G: DAG. Returns longest path lengths to every node. """
    v, s = set(), [] # v: visited, s: stack
    def visit(n):
        if n not in v:
            v.add(n)
            for m in G.get(n, []): visit(m)
            s.append(n) # topological sort order
    for node in G: visit(node) # get traversal order
    order = s[::-1] # reverse stack
    dist = {n: 0 for n in G} # dist: distance mapping
    for n in order: # n: current node in sorted order
        for m in G.get(n, []): # m: direct neighbor
            dist[m] = max(dist[m], dist[n] + 1) # relax path
    return dist # return final distances

# --- START OF PROGRAM ---

# G1: sample Directed Acyclic Graph (DAG) for tasks
G1 = {0: [2, 3, 4], 1: [2, 7], 2: [5], 3: [5, 7], 4: [7], 5: [6], 6: [7], 7: []}

print("Longest Path (Critical Path) Calculator for DAGs!\n")

# Run calculation
len_res = longest_path(G1)

print("--- Results (Task Index: Max Depth) ---")
for tid, depth in len_res.items():
    print(f"Task {tid}: {depth} steps from start")

# Run compact version
c_dist = compact_lp(G1)
print(f"\nCompact code result: {c_dist} ✅")
