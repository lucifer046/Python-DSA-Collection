"""
================================================================================
CONCEPTS AND THEORY: DIJKSTRA'S ALGORITHM (THE 'SMARTEST PATH' FINDER)
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

from heapq import heappop, heappush # Special tools for our Priority Queue (Min-Heap)

def find_shortest_path_dijkstra(adjacency_list, source_node, destination_node):
    """
    Finds the absolute cheapest way to get from source to destination.
    """
    # 1. INITIALIZATION: Count nodes and set initial 'best' distances to Infinity
    total_nodes = len(adjacency_list)
    
    # 'parent_map' stores which node led us to the current one (for rebuilding the path)
    parent_map = {}

    # 'dist_tracker' stores the best cost to reach each node found so far
    # Initially, we know nothing, so we set it to math Infinity
    dist_tracker = [float('inf')] * total_nodes
    
    # Distance to the starting point is obviously 0!
    dist_tracker[source_node] = 0

    # 2. CREATE THE MIN-HEAP: Stores (cost_to_reach, node_id)
    # The heap always keeps the SMALLEST cost at the top (top of the pyramid)
    min_priority_queue = [(0, source_node)]

    # 3. THE WORKER LOOP: 
    while min_priority_queue:
        # Grab the node that is currently the CHEAPEST to reach
        current_cost, current_node = heappop(min_priority_queue)

        # OPTIMIZATION: If we reached our actual target, we can stop early!
        if current_node == destination_node:
            return current_cost, parent_map

        # 4. EXPLORE NEIGHBORS (The 'Relaxation' part):
        # Look at every neighbor we can reach from this current_node
        for neighbor_node, edge_weight in adjacency_list[current_node]:
            # Calculate: "Is reaching the neighbor THROUGH me cheaper than their current best?"
            newly_proposed_cost = current_cost + edge_weight
            
            if dist_tracker[neighbor_node] > newly_proposed_cost:
                # YES! Update their best cost
                dist_tracker[neighbor_node] = newly_proposed_cost
                # Remember that *we* were the one who led them to this cheaper path
                parent_map[neighbor_node] = current_node
                # Add this improved path to the heap so we can explore it later
                heappush(min_priority_queue, (newly_proposed_cost, neighbor_node))
                
    return float('inf'), parent_map

def rebuild_path_sequence(parent_map, target_node):
    """
    Helper function: Walks backwards from the target using parent links 
    to show the full path.
    """
    final_path = []
    # Loop backwards as long as we have a parent link
    while target_node in parent_map:
        final_path.append(target_node)
        target_node = parent_map[target_node]

    # Add the starting node (which has no parent)
    final_path.append(target_node)
    
    # Reverse it because we walked BACKWARDS!
    return final_path[::-1]

def find_path_via_middle_point(adjacency_list, start, end, via_point):
    """
    A special version: Finds the best path from Start to End that MUST pass through Via.
    Example: Going home to work, but stopping at the Bakery on the way.
    """
    # 1. Find shortest path to the 'Via' point
    cost_1, parents_1 = find_shortest_path_dijkstra(adjacency_list, start, via_point)
    # 2. Find shortest path from 'Via' to the final 'End'
    cost_2, parents_2 = find_shortest_path_dijkstra(adjacency_list, via_point, end)

    # 3. Combine the paths carefully
    part_1 = rebuild_path_sequence(parents_1, via_point)
    part_2 = rebuild_path_sequence(parents_2, end)[1:] # Skip the first node to avoid duplicate 'via_point'
    
    return (cost_1 + cost_2, part_1 + part_2)

# ================================================================================
# VERSION 2: THE MOST COMPACT & SHORTEST WAY
# ================================================================================

def dijkstra_shortest_code(graph, source):
    """
    A very short version that gives the distances to ALL nodes in the graph.
    """
    import heapq
    dist = {n: float('inf') for n in range(len(graph))}
    dist[source], pq = 0, [(0, source)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue # Already found a better way
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist

# --- START OF PROGRAM ---

# 1. Create a sample graph (Adjacency List)
# Each list contains (neighbor, weight)
# Node 0 connects to: 1 (cost 4), 2 (cost 2)
sample_graph = [
    [(1, 4), (2, 2)],           # Node 0
    [(0, 4), (2, 1), (3, 5)],   # Node 1
    [(0, 2), (1, 1), (3, 8), (4, 10)],  # Node 2
    [(1, 5), (2, 8), (4, 2)],   # Node 3
    [(2, 10), (3, 2)]           # Node 4
]

print("Welcome to Dijkstra's Path Finder!")

# --- TEST 1 ---
start, target = 0, 4
total_cost, p_map = find_shortest_path_dijkstra(sample_graph, start, target)
full_path = rebuild_path_sequence(p_map, target)

print(f"\n--- Best Path from {start} to {target} ---")
print(f"Total Cost: {total_cost}")
print(f"Path: {' -> '.join(map(str, full_path))}")

# --- TEST 2 ---
via = 1
via_cost, via_path = find_path_via_middle_point(sample_graph, start, target, via)
print(f"\n--- Path from {start} to {target} (VIA Node {via}) ---")
print(f"Total Cost: {via_cost}")
print(f"Path: {' -> '.join(map(str, via_path))}")

# --- TEST 3 ---
print("\n--- All Distances (Shortest Version) ---")
print(dijkstra_shortest_code(sample_graph, 0))
