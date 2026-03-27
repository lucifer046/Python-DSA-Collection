"""
================================================================================
CONCEPTS AND THEORY: PRIM'S ALGORITHM (THE 'GREEDY TREE' BUILDER)
================================================================================

1. WHAT IS PRIM'S ALGORITHM?
   Imagine you are building a social network. You want a way to connect 
   *everyone* together with the shortest possible length of cable. 
   **Prim's Algorithm** is the perfect tool for creating a 
   **Minimum Spanning Tree (MST)**.

2. THE 'MST' CONCEPT:
   - **MINIMUM**: The cheapest total budget.
   - **SPANNING**: Reaches *every* single node in the graph.
   - **TREE**: No cycles (infinite loops) in the connections.

3. THE 'GROW FROM A SEED' STRATEGY:
   Prim's is 'Greedy' and starts from a single node (like a seed).
   - 1. Pick a starting node.
   - 2. Find the smallest edge that connects a node we already 
        visit to a node we haven't visited yet.
   - 3. Add that new node to our 'Seen' list.
   - 4. Repeat until everyone is connected!

4. WHY IS IT USEFUL?
   - **Electricity Grid Layout**: Connecting every house in a city 
     with the minimum amount of power cable.
   - **Computer Networks**: Designing a layout for routers in a 
     building so everyone is connected with minimum fiber optic cabling.

5. REAL LIFE EXAMPLE:
   Think of **WATER PIPELINES**. 
   If you have a map of 10 towns (Nodes) and the cost to lay pipes 
   between them (Weights), Prim's helps the government find the 
   cheapest way to un-dry every town by starting with one town 
   with water and slowly connecting the 'closest' town next to it 
   until everyone has a pipeline!
================================================================================
"""

def prim_minimum_spanning_tree(adjacency_list):
    """
    Finds the cheapest total cost to connect all nodes into a tree structure.
    """
    # 1. INITIALIZATION: Count nodes and track who is 'Seen'
    num_vertices = len(adjacency_list)
    
    # Trace which nodes are already part of our 'Spanning Tree'
    visited_nodes_tracker = [False] * num_vertices
    # We choose node 0 as our starting 'seed' node
    visited_nodes_tracker[0] = True
    
    # Store the total cost for the whole network
    total_mst_cost = 0
    
    # 2. THE GROWTH PASS: We need to find exactly (n-1) edges to connect n nodes
    # (A tree with n nodes always has n-1 edges)
    for edge_count_to_find in range(num_vertices - 1):
        
        next_cheapest_node = -1
        current_best_edge_weight = float('inf')
        
        # 3. SCAN EVERY 'SEEN' PERSON: 
        # For each node we have already connected...
        for already_connected_node in range(num_vertices):
            # Only look at nodes that are already in our tree
            if visited_nodes_tracker[already_connected_node]:
                # ...Look at every possible road (edge) from this connected person
                for neighbor_node, edge_weight in adjacency_list[already_connected_node]:
                    # 4. FIND NEW FRIENDS:
                    # Is this a road to someone we *haven't* connected yet?
                    if not visited_nodes_tracker[neighbor_node]:
                        # 5. GREEDY CHECK: 
                        # Is this the cheapest road found so far to an unvisited person?
                        if edge_weight < current_best_edge_weight:
                            current_best_edge_weight = edge_weight
                            next_cheapest_node = neighbor_node
        
        # 6. UNLOCK THE NEW NODE: 
        # Add the road cost to our total budget and mark them as 'Seen'
        total_mst_cost += current_best_edge_weight
        visited_nodes_tracker[next_cheapest_node] = True
    
    # 7. Return the final budget (total weight) of our pipe network
    return total_mst_cost

# ================================================================================
# VERSION 2: THE MOST COMPACT & SHORTEST WAY (USING A PRIORITY QUEUE)
# ================================================================================

def prim_shortest_code(graph):
    """
    A short version using a HEAP for much faster speed.
    """
    import heapq
    mst_cost, seen, pq = 0, {0}, [(w, v) for v, w in graph[0]]
    heapq.heapify(pq) # Order by weights

    while pq and len(seen) < len(graph):
        w, u = heapq.heappop(pq)
        if u not in seen:
            seen.add(u)
            mst_cost += w
            for v, next_w in graph[u]:
                if v not in seen:
                    heapq.heappush(pq, (next_w, v))
    return mst_cost

# --- START OF PROGRAM ---

# 1. Our graph represented as an ADJACENCY LIST (neighbor, weight)
# Node labels: 0, 1, 2, 3, 4
# For Undirected graphs, edges are listed twice (e.g., 0-1 and 1-0)
sample_prim_graph = [
    [(1, 2), (3, 6)],                    # Node 0 (Link to 1 with weight 2, 3 with weight 6)
    [(0, 2), (2, 3), (3, 8), (4, 5)],    # Node 1
    [(1, 3), (3, 7)],                    # Node 2
    [(0, 6), (1, 8), (2, 7), (4, 1)],    # Node 3
    [(1, 5), (3, 1)]                     # Node 4
]

print("Welcome to Prim's Minimum Spanning Tree Builder!")

# 2. Run the calculation
final_budget = prim_minimum_spanning_tree(sample_prim_graph)

# 3. Print the results
print(f"\nTotal budget needed to connect everyone: ${final_budget}")
print("Every town is now connected to the water system with the lowest cost pipe network.")

# --- TEST SHORTEST VERSION ---
print("\nShortest implementation result (Budget):")
print(prim_shortest_code(sample_prim_graph))
