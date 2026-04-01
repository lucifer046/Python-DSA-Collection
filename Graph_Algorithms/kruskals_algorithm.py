"""
================================================================================
CONCEPTS AND THEORY: KRUSKAL'S ALGORITHM (THE 'DISJOINT-SET' TREE BUILDER)
================================================================================

--- TIME COMPLEXITY ANALYSIS ---
- BEST CASE:    O(E log E) (Sorting all edges takes the most time)
- AVERAGE CASE: O(E log E) or O(E log V)
- WORST CASE:   O(E log E)
--------------------------------
- SPACE COMPLEXITY: O(V + E) (To store the graph edges and the parent array)

STATUS: INDEPENDENT (Contains both a full and a compact implementation)
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

class DSU:
    """ 
    Disjoint Set Union (Union-Find) to detect cycles and merge groups. 
    n: number of elements (nodes)
    """
    def __init__(self, n):
        # p: parent list, r: rank list for balancing
        self.p = list(range(n)) # each node is its own parent initially
        self.r = [0] * n        # rank helps keep tree flat
        
    def find(self, i):
        """ Returns the 'Chief' (root) of node i's group. """
        # i: node index
        if self.p[i] == i: return i
        # path compression optimization
        self.p[i] = self.find(self.p[i])
        return self.p[i]

    def union(self, i, j):
        """ Merges groups containing i and j. Returns True if merged. """
        # 1. find roots of both elements
        ri, rj = self.find(i), self.find(j) # ri: root of i, rj: root of j
        
        # 2. if already in the same group, cannot merge
        if ri == rj: return False
        
        # 3. union by rank strategy
        if self.r[ri] < self.r[rj]:
            self.p[ri] = rj
        elif self.r[ri] > self.r[rj]:
            self.p[rj] = ri
        else:
            self.p[rj] = ri
            self.r[ri] += 1
        return True

def kruskal(E, n):
    """
    Kruskal's MST algorithm.
    E: list of (weight, source, dest) tuples, n: vertices count
    """
    # 1. Sort all edges by weight (cheapest first)
    # e: edge iterator (w, u, v)
    E.sort() # w: weight, u: source, v: destination
    
    # 2. uf: Union-Find manager
    uf = DSU(n) # uf = union-find instance
    
    # 3. Initialize collectors for MST
    mst = [] # mst = minimum spanning tree edges
    tc = 0   # tc = total cost (budget)
    
    # 4. Greedy edge selection
    for w, u, v in E:
        # 5. Only add if it doesn't form a cycle
        if uf.union(u, v):
            mst.append((u, v, w)) # save edge
            tc += w # add cost
            # exit early if we've found n-1 edges (MST complete)
            if len(mst) == n - 1: break
            
    # return total cost and the selected edges
    return tc, mst

# ================================================================================
# COMPACT KRUSKAL
# ================================================================================

def compact_kruskal(n, E):
    """ n: vertices, E: (w,u,v) list. Minimalist MST cost. """
    E.sort(); p = list(range(n)) # p: parent
    def find(i):
        if p[i] == i: return i
        p[i] = find(p[i]); return p[i]
    cost, count = 0, 0
    for w, u, v in E:
        ru, rv = find(u), find(v) # ru: root of u
        if ru != rv:
            p[ru] = rv; cost += w; count += 1
            if count == n - 1: break
    return cost

# --- START OF PROGRAM ---

# E_list: list of possible bridges (weight, u, v)
E_list = [
    (2, 0, 1), (3, 1, 2), (6, 0, 3), 
    (8, 1, 3), (5, 1, 4), (7, 2, 3), (1, 3, 4)
]

print("Kruskal's MST Builder Demo!\n")

# Run calculation
v_count = 5
total_c, mst_edges = kruskal(E_list, v_count)

print(f"MST Total Construction Cost: ${total_c}")
print("Selected Connections:")
for u, v, w in mst_edges:
    print(f"  {u} <--> {v} (Cost: {w})")

# Run compact version
c_cost = compact_kruskal(v_count, E_list)
print(f"\nCompact Result Check (Total Cost): ${c_cost} ✅")
