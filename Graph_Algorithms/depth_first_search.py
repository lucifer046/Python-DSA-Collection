"""
================================================================================
CONCEPTS AND THEORY: DEPTH-FIRST SEARCH (THE 'TRENCH EXPLORER' METHOD)
================================================================================

--- TIME COMPLEXITY ANALYSIS ---
- ADJACENCY LIST (Best/Avg/Worst): O(V + E) (Visit every vertex and every edge)
- ADJACENCY MATRIX (Best/Avg/Worst): O(V^2) (Must scan every column for each node)
--------------------------------
- SPACE COMPLEXITY: O(V) (Requires space for the recursion stack or manual stack)

STATUS: INDEPENDENT (Contains Iterative, Recursive, and Compact versions)
================================================================================

1. WHAT IS DEPTH-FIRST SEARCH (DFS)?
   If BFS was ripples in a pond, DFS is someone exploring a deep cave. 
   Instead of checking every neighbor at the same distance, DFS picks 
   ONE tunnel and keeps going as deep as possible until they hit a wall. 
   Only then do they 'Backtrack' and try a different tunnel.

2. THE 'STACK' STRATEGY:
   DFS is a 'Last-In, First-Out' algorithm. 
   - We use a **STACK** to remember our current path. 
   - When we hit a dead end, we 'Pop' (remove) the last node we added
     to see where we were before.

3. TWO WAYS TO IMPLEMENT:
   - 1. **ITERATIVE**: Uses a manual Stack object to keep track of where to 
        go next.
   - 2. **RECURSIVE**: This is often the most elegant way! Each function 
        call 'remembers' its previous state, so the computer handles the 
        backtracking for us naturally.

4. WHY IS IT USEFUL?
   - **Solving Puzzles/Mazes**: Since it explores paths to the end, it's 
     great for finding a way out of a maze.
   - **Detecting Cycles**: If you are walking deep into a graph and find 
     yourself back where you started, you've found a cycle!
   - **Pathfinding**: It's good at finding *a* path (though not necessarily 
      the shortest one).

5. REAL LIFE EXAMPLE:
   Think of **WALKING THROUGH A MAZE**. 
   - You enter a dark tunnel and keep walking straight as far as you can. 
   - If you hit a wall, you turn around (Backtrack) until you find the 
     last side-door you saw. 
   - You enter that side-door and repeat. You keep going 'deep' until 
     you find the exit or check every inch of the maze!
================================================================================
"""

import queue # q: standard python queue module for LIFO stack

# ================================================================================
# VERSION 1: ITERATIVE DFS (USING A MANUAL STACK)
# ================================================================================

def dfs_iter(G, s):
    """
    Depth-First Search using a manual LIFO stack.
    G: adjacency list, s: start node
    """
    # 1. v: visited tracker dictionary for all nodes in G
    v = {node: False for node in G} # node: vertex identifier
    
    # 2. st: Stack for exploration (Last-In, First-Out)
    st = queue.LifoQueue() # st = stack
    
    # 3. Start by adding the initial node to the stack
    st.put(s) # add s to stack
    
    # 4. Explore until no breadcrumbs are left in the stack
    while not st.empty():
        # 5. curr: take the most recently added node (go deep)
        curr = st.get() # curr = current node
        
        # 6. If we haven't visited this node yet, explore it
        if not v[curr]:
            v[curr] = True # mark as seen
            # 7. Add all neighbors to the stack for future exploration
            for nbr in G[curr]: # nbr = neighbor
                if not v[nbr]:
                    st.put(nbr) # push nbr onto stack
                    
    # 8. Return final visited mapping
    return v

# ================================================================================
# VERSION 2: RECURSIVE DFS (MOST ELEGANT)
# ================================================================================

def start_dfs(G):
    """ Helper to setup trackers for recursive DFS. """
    v = {x: False for x in G} # v: visited mapping
    p = {x: -1 for x in G} # p: parent mapping (-1 = none)
    return v, p

def dfs_rec(G, v, p, curr):
    """
    Recursive DFS explorer.
    G: graph, v: visited dict, p: parent dict, curr: current node
    """
    # 1. Mark node as arrived
    v[curr] = True 
    
    # 2. For each neighbor nbr:
    for nbr in G[curr]:
        if not v[nbr]:
            # 3. Mark current node as parent and recurse deeper
            p[nbr] = curr # set parent relationship
            dfs_rec(G, v, p, nbr) # jump into neighbor node
            
    # 4. Return the traversal state
    return v, p

# ================================================================================
# VERSION 3: THE MOST COMPACT DFS
# ================================================================================

def compact_dfs(G, s, v=None):
    """
    Recursive DFS in minimal code using a set.
    G: graph, s: current node, v: visited set
    """
    if v is None: v = set() # v: set to store visited nodes
    v.add(s) # mark current s as seen
    # Explore neighbors m that haven't been seen
    for m in G[s]: # m: neighbor node
        if m not in v: compact_dfs(G, m, v)
    return v # return set of discovered nodes

# --- START OF PROGRAM ---

# G1: sample graph dictionary (0-4)
G1 = {0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: []}

print("Welcome to the Depth-First Explorer!\n")

# Run iterative version
print("--- Testing Iterative DFS ---")
res1 = dfs_iter(G1, 0)
print(f"Nodes reached: {res1} ✅\n")

# Run recursive version
print("--- Testing Recursive DFS ---")
v_init, p_init = start_dfs(G1)
v_fin, p_fin = dfs_rec(G1, v_init, p_init, 0)
print(f"Nodes visited: {v_fin}")
print(f"Parent Path:   {p_fin} ✅\n")

# Run compact version
print("--- Testing Compact DFS ---")
res3 = compact_dfs(G1, 0)
print(f"All nodes reached: {sorted(list(res3))} ✅")
