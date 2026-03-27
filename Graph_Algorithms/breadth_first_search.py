"""
================================================================================
CONCEPTS AND THEORY: BREADTH-FIRST SEARCH (LAYER-BY-LAYER EXPLORATION)
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

import queue  # We import the standard Python 'queue' module for efficiency
import numpy as np

# ================================================================================
# VERSION 1: BFS FOR ADJACENCY LIST (THE DICTIONARY WAY)
# ================================================================================

def bfs_using_adjacency_list(graph_adjacency_list, start_node):
    """
    Explores the graph using a dictionary representing nodes and neighbors.
    """
    # 1. INITIALIZATION: Create a tracker to remember who we have already 'seen'
    # Initially, every node is marked as False (Not visited)
    visited_nodes_tracker = {}
    for node_name in graph_adjacency_list.keys():
        visited_nodes_tracker[node_name] = False    
    
    # 2. CREATE THE QUEUE: Use the standard 'queue.Queue()' from Python
    # This acts as our 'Waiting Line' for nodes to be processed
    nodes_waiting_line = queue.Queue()
    
    # 3. START: Mark the first node as visited and put it in the waiting line
    visited_nodes_tracker[start_node] = True
    nodes_waiting_line.put(start_node) # 'put' is like 'enqueue'
    
    # 4. THE LOOP: Keep going as long as there is someone left in the line
    while not nodes_waiting_line.empty():
        
        # Pull the person at the VERY FRONT of the line
        current_node = nodes_waiting_line.get() # 'get' is like 'dequeue'
        
        # 5. SCAN NEIGHBORS: Look at all the friends (neighbors) of the current node
        for neighbor_node in graph_adjacency_list[current_node]:
            # If we HAVEN'T visited this neighbor yet:
            if not visited_nodes_tracker[neighbor_node]:
                # Mark them as visited (Found them!)
                visited_nodes_tracker[neighbor_node] = True
                # Add them to the back of the waiting line to check their friends later
                nodes_waiting_line.put(neighbor_node)
                
    # Return the final tracker showing who was reached
    return visited_nodes_tracker

# ================================================================================
# VERSION 2: BFS FOR ADJACENCY MATRIX (THE GRID WAY)
# ================================================================================

def find_neighbor_nodes_in_matrix(graph_matrix, node_index):
    """
    A helper function to look at a row in the grid and find all neighbors (marked as 1).
    """
    neighbor_list = []
    # Find how many columns (potential neighbors) exist in the grid
    row_count, column_count = graph_matrix.shape
    
    # Look at every 'seat' in the current node's row
    for target_column in range(column_count):
        # If there's a '1' in that column, they are connected!
        if graph_matrix[node_index, target_column] == 1:
            neighbor_list.append(target_column)
            
    return neighbor_list

def bfs_using_adjacency_matrix(graph_matrix, start_node_index):
    """
    Explores a graph represented by a 2D grid/matrix.
    """
    # 1. INITIALIZATION: How many nodes are there in total?
    row_count, column_count = graph_matrix.shape
    
    # Create the tracker (Everyone starts as 'Not Visited')
    visited_nodes_tracker = {}
    for node_index in range(row_count):
        visited_nodes_tracker[node_index] = False    
    
    # 2. CREATE THE QUEUE
    nodes_waiting_line = queue.Queue()
    
    # 3. START: Mark start node as visited and put in line
    visited_nodes_tracker[start_node_index] = True
    nodes_waiting_line.put(start_node_index)
    
    # 4. THE LOOP: Process the line one by one
    while not nodes_waiting_line.empty():
        # Remove the front node
        current_node_index = nodes_waiting_line.get()
        
        # 5. FIND FRIENDS: Use our helper to find every neighbor in the grid
        for neighbor_index in find_neighbor_nodes_in_matrix(graph_matrix, current_node_index):
            # If neighbor is new to us:
            if not visited_nodes_tracker[neighbor_index]:
                # Mark as seen
                visited_nodes_tracker[neighbor_index] = True
                # Add to the back of the line
                nodes_waiting_line.put(neighbor_index)
                
    return visited_nodes_tracker

# ================================================================================
# VERSION 3: THE MOST COMPACT & SHORTEST WAY
# ================================================================================

def bfs_shortest_code(graph, start):
    """
    A short, 6-line version of BFS using a list as a queue and a set to 'remember'.
    """
    # 1. 'visited' is a set (much faster than a dictionary!)
    # 2. 'queue' is just a simple list
    visited, line = {start}, [start]
    
    # 3. Keep going until the line is empty
    for node in line:
        # 4. For every unvisited friend, add them to the seen set and the line
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                line.append(neighbor)
                
    # Return the list of nodes in the order they were discovered
    return line

# --- START OF PROGRAM ---

# 1. Define a sample graph with 5 vertices (0 to 4)
# Links: 0-1, 0-2, 1-3, 1-4, 2-4, 2-3, 3-4
sample_adj_list = {0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: []}

print("--- Testing BFS with Adjacency List ---")
list_result = bfs_using_adjacency_list(sample_adj_list, 0)
print(f"Nodes reached (Dict): {list_result}\n")

# 2. Define the SAME graph as a Matrix (Grid)
# We use numpy to create a grid of zeros and fill in the connections
vertices = [0, 1, 2, 3, 4]
edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (2, 3), (3, 4)]
grid_size = len(vertices)
sample_matrix = np.zeros(shape=(grid_size, grid_size))

for row, col in edges:
    sample_matrix[row, col] = 1 # Mark the connection

print("--- Testing BFS with Adjacency Matrix ---")
matrix_result = bfs_using_adjacency_matrix(sample_matrix, 0)
print(f"Nodes reached (Matrix): {matrix_result}\n")

print("--- Testing THE SHORTEST BFS VERSION ---")
simple_list = bfs_shortest_code(sample_adj_list, 0)
print(f"Order discovered: {simple_list}")
