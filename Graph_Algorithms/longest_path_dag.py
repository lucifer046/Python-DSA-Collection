"""
================================================================================
CONCEPTS AND THEORY: LONGEST PATH ON DAG (THE 'CRITICAL PATH' METHOD)
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

import queue # Standard Python Queue module

def calculate_longest_path_in_dag(task_adjacency_list):
    """
    Computes the depth (longest path) of every node in a directed acyclic graph.
    """
    # 1. INITIALIZATION: Track dependencies (In-degree) and path lengths
    dependency_tracker = {}
    path_length_tracker = {} # Stores how many steps it takes to reach each node
    
    # Ready Queue for nodes that have no prerequisites
    ready_to_process_queue = queue.Queue()
    
    # At the start, set every task to 0 dependencies and 0 path length
    for node in task_adjacency_list.keys():
        dependency_tracker[node] = 0
        path_length_tracker[node] = 0
    
    # 2. COUNT THE INCOMING ARROWS:
    for parent_node in task_adjacency_list.keys():
        for neighbor_node in task_adjacency_list[parent_node]:
            # Each time an arrow points to a task, increase its prerequisite count
            dependency_tracker[neighbor_node] += 1

    # 3. FIND THE STARTING POINTS: Nodes with 0 prerequisites
    for node_name in task_adjacency_list.keys():
        if dependency_tracker[node_name] == 0:
            ready_to_process_queue.put(node_name)
            
    # 4. THE COMPUTING PROCESS: 
    while not ready_to_process_queue.empty():
        # Remove a 'ready' task from the queue
        current_node = ready_to_process_queue.get()
        # Mark it as 'completed' by subtracting its prerequisites
        dependency_tracker[current_node] -= 1
        
        # 5. EXPLORE NEIGHBORS: Check every task waiting on this current one
        for neighbor_node in task_adjacency_list[current_node]:
            # REDUCE PREREQUISITE:
            dependency_tracker[neighbor_node] -= 1
            
            # CALCULATE PATH: 
            # The neighbor node's distance is now AT LEAST (our distance + 1)
            # We use 'max' to make sure we only keep the LONGEST path found so far.
            path_length_tracker[neighbor_node] = max(
                path_length_tracker[neighbor_node], 
                path_length_tracker[current_node] + 1
            )
            
            # 6. UNLOCK: If the neighbor now has 0 prerequisites left, it's ready!
            if dependency_tracker[neighbor_node] == 0:
                ready_to_process_queue.put(neighbor_node)
                
    # Return the map of every node and its longest path length
    return path_length_tracker

# ================================================================================
# VERSION 2: THE MOST COMPACT & SHORTEST WAY
# ================================================================================

def longest_path_shortest_code(graph):
    """
    Very short Longest Path on DAG.
    1. First, get the topological order.
    2. Then, calculate path lengths node-by-node in that order.
    """
    # Helper to get the dependency order using DFS
    def get_order(node, visited, stack):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                get_order(neighbor, visited, stack)
        stack.append(node)

    visited, order = set(), []
    for node in graph.keys():
        if node not in visited:
            get_order(node, visited, order)
    
    # Process in reverse order (topological)
    ordered_nodes = order[::-1]
    
    # Map every node to distance 0 initially
    dist = {node: 0 for node in graph}
    
    # Update distances in order
    for node in ordered_nodes:
        for neighbor in graph.get(node, []):
            dist[neighbor] = max(dist[neighbor], dist[node] + 1)
            
    return dist

# --- START OF PROGRAM ---

# 1. Sample Graph (DAG) representing the 'Critical Path' of a project
sample_tasks = {0: [2, 3, 4], 1: [2, 7], 2: [5], 3: [5, 7], 4: [7], 5: [6], 6: [7], 7: []}

print("Welcome to the Critical Path (Longest Path) Calculator!")
print("Finding the 'Depth' of every node in the system...\n")

# Run the calculation
results_map = calculate_longest_path_in_dag(sample_tasks)

# Print out the results clearly
print("--- Results (Node: Depth) ---")
for task_id, depth in results_map.items():
    print(f"Task {task_id}: {depth}")

print("\n--- Testing THE SHORTEST LONGEST-PATH CODE ---")
final_dist = longest_path_shortest_code(sample_tasks)
print(f"Final Distances: {final_dist}")
