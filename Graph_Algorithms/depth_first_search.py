"""
================================================================================
CONCEPTS AND THEORY: DEPTH-FIRST SEARCH (THE 'TRENCH EXPLORER' METHOD)
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

import queue  # We will use queue.LifoQueue for our iterative stack

# ================================================================================
# VERSION 1: ITERATIVE DFS (USING A MANUAL STACK)
# ================================================================================

def dfs_iterative(graph_adjacency_list, start_node):
    """
    Explores the graph by pushing paths onto a manual Stack.
    """
    # 1. INITIALIZATION: Track every node as 'Not Visited'
    visited_nodes_tracker = {}
    for node_name in graph_adjacency_list.keys():
        visited_nodes_tracker[node_name] = False    
    
    # 2. CREATE THE STACK: Use the standard 'LifoQueue' (Last-In, First-Out)
    # This acts as our 'Breadcrumb Trail' for exploration
    path_stack = queue.LifoQueue()
    
    # 3. START: Put the first node into the stack
    path_stack.put(start_node)
    
    # 4. THE LOOP: Keep going until we have no more breadcrumbs
    while not path_stack.empty():
        # Pop the VERY LAST node we added (the deepest one)
        current_node = path_stack.get()
        
        # 5. CHECK: Have we visited this node before?
        if not visited_nodes_tracker[current_node]:
            # Mark as visited (exploring its tunnel)
            visited_nodes_tracker[current_node] = True
            
            # 6. SCAN NEIGHBORS: Look at all the neighbors of the current node
            for neighbor_node in graph_adjacency_list[current_node]:
                # If we haven't been there yet, push it onto the stack to explore later
                if not visited_nodes_tracker[neighbor_node]:
                    path_stack.put(neighbor_node)
                    
    # Return the final results
    return visited_nodes_tracker

# ================================================================================
# VERSION 2: RECURSIVE DFS (THE ELEGANT WAY)
# ================================================================================

def initialize_dfs_trackers(graph_adjacency_list):
    """
    A helper function to set up our 'visited' and 'parent' dictionaries.
    'parent' helps us trace the 'family tree' of how we got there.
    """
    visited_nodes_tracker = {}
    parent_node_tracker = {}
    
    for vertex in graph_adjacency_list.keys():
        visited_nodes_tracker[vertex] = False
        parent_node_tracker[vertex] = -1 # -1 means 'No parent yet'
        
    return visited_nodes_tracker, parent_node_tracker

def dfs_recursive(graph_adjacency_list, visited, parent, current_node):
    """
    Explores the graph by asking the function to call itself on its neighbors.
    """
    # 1. Mark the current node as 'Visited' as soon as we arrive
    visited[current_node] = True
    
    # 2. SCAN NEIGHBORS: For every person (neighbor) connected to us:
    for neighbor_node in graph_adjacency_list[current_node]:
        # If we haven't visited them yet:
        if not visited[neighbor_node]:
            # 3. SET PARENT: Mark the current node as their 'Father'
            parent[neighbor_node] = current_node
            
            # 4. GO DEEPER: Ask the function to go explore that neighbor! (Recursion)
            (visited, parent) = dfs_recursive(graph_adjacency_list, visited, parent, neighbor_node)
            
    # Return the results back to whoever called us
    return visited, parent

# ================================================================================
# VERSION 3: THE MOST COMPACT & SHORTEST WAY
# ================================================================================

def dfs_shortest_code(graph, start, seen=None):
    """
    Extremely short, recursive DFS using a set to remember visited nodes.
    """
    if seen is None: 
        seen = set() # Create a single set for the whole search
    
    seen.add(start) # Mark current node as visited
    
    # For every neighbor, go deep IF we haven't been there yet
    for neighbor in graph[start]:
        if neighbor not in seen:
            dfs_shortest_code(graph, neighbor, seen)
            
    return seen

# --- START OF PROGRAM ---

# 1. Define our sample graph (same as the BFS example)
sample_graph = {0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: []}

print("Welcome to the Depth-First Explorer!")

# --- TEST 1 ---
print("\n--- Testing Iterative DFS ---")
iterative_result = dfs_iterative(sample_graph, 0)
print(f"Nodes reached: {iterative_result}")

# --- TEST 2 ---
print("\n--- Testing Recursive DFS ---")
vis, par = initialize_dfs_trackers(sample_graph)
final_visits, final_family = dfs_recursive(sample_graph, vis, par, 0)
print(f"Nodes reached (Visited): {final_visits}")
print(f"Path taken (Parents):    {final_family}")

# --- TEST 3 ---
print("\n--- Testing SHORTEST DFS VERSION ---")
all_found = dfs_shortest_code(sample_graph, 0)
print(f"All nodes reached (Set): {sorted(all_found)}")
