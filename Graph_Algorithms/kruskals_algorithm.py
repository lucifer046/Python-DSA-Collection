"""
================================================================================
CONCEPTS AND THEORY: KRUSKAL'S ALGORITHM (THE 'DISJOINT-SET' TREE BUILDER)
================================================================================

1. WHAT IS KRUSKAL'S ALGORITHM?
   Like Prim's, Kruskal's is designed to find the **Minimum Spanning Tree (MST)**. 
   Connecting every node together with the minimum total budget. 

2. THE 'SORT AND CONNECT' STRATEGY:
   Instead of growing from a seed node like Prim's, Kruskal's is much 
   simpler to explain:
   - 1. Sort every single edge (road) in the graph from CHEAPEST to MOST EXPENSIVE.
   - 2. Go through the sorted list one by one.
   - 3. If adding the cheapest road DOESN'T form a loop (cycle), add it!
   - 4. Repeat until everyone is connected.

3. THE 'UNION-FIND' CONCEPT:
   Kruskal's needs a special helper called **UNION-FIND** (Disjoint Set). 
   - Each node starts in its own 'Island'. 
   - When we add an edge, we check: 
     "Are these two nodes already on the same Island?"
   - If NOT, we 'Union' (connect) the islands and add the edge!

4. WHY IS IT USEFUL?
   - **Network Topology Design**: Designing the backbone for a city's 
     fiber-optic internet. 
   - **Clustering**: In data science, finding relationships between 
     points in a scatter plot.

5. REAL LIFE EXAMPLE:
   Think of **ISLAND BRIDGES**. 
   There are many tiny islands in the ocean. You want to build the 
   cheapest possible bridges so everyone can visit everyone else. 
   Kruskal's starts by building the absolute cheapest bridge first. 
   If a bridge would just connect two islands that already have a path 
   between them, we skip it to save money! 
================================================================================
"""

class IslandConnector:
    """
    A simple Union-Find (Disjoint Set) class to manage our islands.
    """
    def __init__(self, node_count):
        # Every node starts as its own parent (its own island)
        self.island_parent = list(range(node_count))
        # 'Rank' helps us keep our tree balanced for speed
        self.island_rank = [0] * node_count

    # The 'Find' function: Tells us which island a node belongs to
    def find_island_id(self, node_id):
        # If the node is not its own parent, it belongs to someone else's island
        if self.island_parent[node_id] != node_id:
            # We recursively find the 'Chief' of the island
            # OPTIMIZATION: We update the parent to the Chief directly ('Path Compression')
            self.island_parent[node_id] = self.find_island_id(self.island_parent[node_id])
        return self.island_parent[node_id]

    # The 'Union' function: Connects two islands together
    def merge_islands(self, node_a, node_b):
        # 1. Find the Chief of each island
        root_a = self.find_island_id(node_a)
        root_b = self.find_island_id(node_b)
        
        # 2. If they are already on the same island, DO NOTHING
        if root_a == root_b:
            return False
            
        # 3. Otherwise, connect the smaller island under the larger one (By Rank)
        if self.island_rank[root_a] < self.island_rank[root_b]:
            self.island_parent[root_a] = root_b
        elif self.island_rank[root_a] > self.island_rank[root_b]:
            self.island_parent[root_b] = root_a
        else:
            # If they are same size, pick one and increase its rank
            self.island_parent[root_b] = root_a
            self.island_rank[root_a] += 1
        return True

def find_minimum_spanning_tree_kruskal(edge_list, total_vertices):
    """
    Finds the cheapest total budget to connect all nodes together using sorted edges.
    """
    # 1. INITIALIZATION: Create our Island Connector (Union-Find)
    connector = IslandConnector(total_vertices)
    
    # 2. SORT EDGES: Sort from Cheapest to Most Expensive (ascending)
    # The 'edge' tuple is (weight, source, destination)
    sorted_edges = sorted(edge_list, key=lambda current_edge: current_edge[0])

    mst_selected_edges = []
    total_budget_needed = 0

    # 3. THE CONNECTING PROCESS:
    for weight, source, destination in sorted_edges:
        # Ask: "Would adding this bridge connect two DIFFERENT islands?"
        if connector.merge_islands(source, destination):
            # YES! Add the cost and remember the edge
            mst_selected_edges.append((source, destination, weight))
            total_budget_needed += weight
            
            # OPTIMIZATION: Once we have n-1 edges, we are DONE!
            if len(mst_selected_edges) == total_vertices - 1:
                break

    return total_budget_needed, mst_selected_edges

# ================================================================================
# VERSION 2: THE MOST COMPACT & SHORTEST WAY
# ================================================================================

def kruskal_shortest_code(n, edges):
    """
    A very short version using simple parent links for union-find.
    """
    # 1. Sort edges (w, u, v)
    edges.sort()
    parent = list(range(n))
    
    # Helper to find the chief of an island
    def find_chief(i):
        if parent[i] == i: return i
        parent[i] = find_chief(parent[i])
        return parent[i]
        
    mst_cost, count = 0, 0
    # 2. Connect if not on same island
    for w, u, v in edges:
        root_u, root_v = find_chief(u), find_chief(v)
        if root_u != root_v:
            parent[root_u] = root_v
            mst_cost += w
            count += 1
            if count == n - 1: break
            
    return mst_cost

# --- START OF PROGRAM ---

# 1. Our graph represented as a LIST of EDGES (weight, source, destination)
# Node labels: 0, 1, 2, 3, 4
sample_edges_list = [
    (2, 0, 1),      # Bridge from 0 to 1 costs 2
    (3, 1, 2),      # Bridge from 1 to 2 costs 3
    (6, 0, 3),      # Bridge from 0 to 3 costs 6
    (8, 1, 3),      # Bridge from 1 to 3 costs 8
    (5, 1, 4),      # Bridge from 1 to 4 costs 5
    (7, 2, 3),      # Bridge from 2 to 3 costs 7
    (1, 3, 4)       # Bridge from 3 to 4 costs 1
]

print("Welcome to Kruskal's Minimum Spanning Tree Builder!")

# 2. Run the calculation
total_nodes_count = 5
final_cost, selected_roads = find_minimum_spanning_tree_kruskal(sample_edges_list, total_nodes_count)

# 3. Print the results
print(f"\nTotal budget needed to connect all islands: ${final_cost}")
print("Selected Bridges (Source -- Cost --> Destination):")
for src, dst, cost in selected_roads:
    print(f"  Island {src} -- ${cost} --> Island {dst}")

# --- TEST SHORTEST VERSION ---
print("\nShortest implementation result (Total Budget):")
print(f"${kruskal_shortest_code(total_nodes_count, sample_edges_list)}")
