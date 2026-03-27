"""
================================================================================
CONCEPTS AND THEORY: TOPOLOGICAL SORT (THE 'TASK SCHEDULER' METHOD)
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

import queue # Standard Python Queue module
import numpy as np

# ================================================================================
# VERSION 1: TOPOLOGICAL SORT FOR ADJACENCY LIST (KAHN'S ALGORITHM)
# ================================================================================

def topological_sort_list(task_adjacency_list):
    """
    Finds a legal sequence for tasks using a dependency dictionary.
    """
    # 1. INITIALIZATION: Create trackers for our dependencies and the final result
    dependency_tracker = {} # Stores how many prerequisites each task has
    final_ordered_sequence = []
    
    # 2. START CODES: Assume everyone has 0 dependencies initially
    for node in task_adjacency_list.keys():
        dependency_tracker[node] = 0
    
    # 3. COUNT THE ARROWS: For every task, see which neighbors it 'points' to
    for parent_task in task_adjacency_list.keys():
        for neighbor_task in task_adjacency_list[parent_task]:
            # Each time an arrow points to a task, increase its in-degree count
            dependency_tracker[neighbor_task] += 1
    
    # 4. READY QUEUE: Find every task that has NO prerequisites (In-degree 0)
    ready_to_start_queue = queue.Queue()
    for task_name in task_adjacency_list.keys():
        if dependency_tracker[task_name] == 0:
            ready_to_start_queue.put(task_name)
    
    # 5. THE SCHEDULING PROCESS: While there's a task ready to go...
    while not ready_to_start_queue.empty():
        # Remove the task from the ready line
        current_task = ready_to_start_queue.get()       
        
        # Add it to our final finished list
        final_ordered_sequence.append(current_task)
        
        # 'Subtract' this task from the system (No longer a pending prerequisite)
        dependency_tracker[current_task] -= 1
        
        # 6. UNLOCK NEIGHBORS: For each neighbor that was waiting on this task...
        for unlocked_task in task_adjacency_list[current_task]:
            # Reduce their prerequisite count by 1
            dependency_tracker[unlocked_task] -= 1
            # If they now have ZERO prerequisites left, they are READY!
            if dependency_tracker[unlocked_task] == 0:
                ready_to_start_queue.put(unlocked_task)                
    
    return final_ordered_sequence

# ================================================================================
# VERSION 2: TOPOLOGICAL SORT FOR ADJACENCY MATRIX (THE GRID WAY)
# ================================================================================

def topological_sort_matrix(task_dependency_matrix):
    """
    Finds a legal sequence for tasks represented in a 2D grid.
    """
    # 1. INITIALIZATION: Measure the grid
    row_count, column_count = task_dependency_matrix.shape
    dependency_tracker = {}
    final_ordered_sequence = []
    
    # 2. COMPUTE IN-DEGREE: For every column (task), count how many 1s are in its row
    for col_idx in range(column_count):
        dependency_tracker[col_idx] = 0
        for row_idx in range(row_count):
            # If the matrix shows a connection from Row -> Column
            if task_dependency_matrix[row_idx, col_idx] == 1:
                dependency_tracker[col_idx] += 1
    
    # 3. THE REPEATED SELECTION PROCESS
    for _ in range(row_count):
        # 4. PICK THE SMALLEST READY TASK: 
        # Find all tasks that currently have 0 prerequisites
        ready_tasks = [task for task in range(column_count) if dependency_tracker[task] == 0]
        
        # If no task is ready but some are left, we have a cycle (infinite loop)!
        if not ready_tasks:
            break
            
        # Pick the first one available
        chosen_task = min(ready_tasks)
        
        # 5. MARK AS FINISHED: Add to the sequence and 'delete' its dependencies
        final_ordered_sequence.append(chosen_task)
        dependency_tracker[chosen_task] = -1 # Move it out of the search pool
        
        # 6. UPDATE NEIGHBORS: Look at every other task in its row
        for neighbor_idx in range(column_count):
            # If the chosen task was a prerequisite for this neighbor
            if task_dependency_matrix[chosen_task, neighbor_idx] == 1:
                # Reduce neighbor's prerequisite count
                dependency_tracker[neighbor_idx] -= 1
                
    return final_ordered_sequence

# ================================================================================
# VERSION 3: THE MOST COMPACT & SHORTEST WAY (DFS-BASED)
# ================================================================================

def topological_sort_shortest(graph):
    """
    Very compact Topological Sort using DFS.
    The secret: Push a node to the list ONLY AFTER its neighbors are finished.
    Then reverse the list at the end!
    """
    visited, stack = set(), []

    def visit(node):
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                visit(neighbor)
            # Add to stack AFTER visiting neighbors
            stack.append(node)

    # Make sure we visit every node in the graph
    for vertex in graph.keys():
        visit(vertex)

    # Return the reverse of the stack
    return stack[::-1]

# --- START OF PROGRAM ---

# 1. Sample Graph (Directed Acyclic Graph)
# Links: 0->2, 0->3, 0->4, 1->2, 1->7, 2->5, 3->5, 3->7, 4->7, 5->6, 6->7
sample_task_list = {0: [2, 3, 4], 1: [2, 7], 2: [5], 3: [5, 7], 4: [7], 5: [6], 6: [7], 7: []}

print("--- Testing Topological Sort with Adjacency List ---")
list_result = topological_sort_list(sample_task_list)
print(f"Correct Task Order: {list_result}\n")

# 2. Adjacency Matrix
num_vertices = 8
edges = [(0,2), (0,3), (0,4), (1,2), (1,7), (2,5), (3,5), (3,7), (4,7), (5,6), (6,7)]
sample_matrix = np.zeros(shape=(num_vertices, num_vertices))

for start_task, end_task in edges:
    sample_matrix[start_task, end_task] = 1 

print("--- Testing Topological Sort with Adjacency Matrix ---")
matrix_result = topological_sort_matrix(sample_matrix)
print(f"Correct Task Order: {matrix_result}\n")

print("--- Testing THE SHORTEST TOPOLOGICAL SORT ---")
shortest_result = topological_sort_shortest(sample_task_list)
print(f"The Shortest Order: {shortest_result}")
