# Graph Report - D:\IITM_Source_codes\python-dsa-handbook  (2026-04-20)

## Corpus Check
- 42 files · ~885,050 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 422 nodes · 507 edges · 36 communities detected
- Extraction: 95% EXTRACTED · 5% INFERRED · 0% AMBIGUOUS · INFERRED: 25 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 19|Community 19]]
- [[_COMMUNITY_Community 20|Community 20]]
- [[_COMMUNITY_Community 21|Community 21]]
- [[_COMMUNITY_Community 22|Community 22]]
- [[_COMMUNITY_Community 23|Community 23]]
- [[_COMMUNITY_Community 24|Community 24]]
- [[_COMMUNITY_Community 25|Community 25]]
- [[_COMMUNITY_Community 26|Community 26]]
- [[_COMMUNITY_Community 27|Community 27]]
- [[_COMMUNITY_Community 28|Community 28]]
- [[_COMMUNITY_Community 29|Community 29]]
- [[_COMMUNITY_Community 30|Community 30]]
- [[_COMMUNITY_Community 31|Community 31]]
- [[_COMMUNITY_Community 32|Community 32]]
- [[_COMMUNITY_Community 33|Community 33]]
- [[_COMMUNITY_Community 34|Community 34]]
- [[_COMMUNITY_Community 35|Community 35]]

## God Nodes (most connected - your core abstractions)
1. `MinHeap` - 15 edges
2. `MaxHeap` - 14 edges
3. `AVLTree` - 12 edges
4. `Queue` - 11 edges
5. `DSACheatsheetPDF` - 10 edges
6. `init()` - 9 edges
7. `Node` - 9 edges
8. `LinkedList` - 7 edges
9. `Stack` - 7 edges
10. `solve()` - 7 edges

## Surprising Connections (you probably didn't know these)
- `solve()` --calls--> `unique_paths_memo()`  [INFERRED]
  D:\IITM_Source_codes\python-dsa-handbook\Divide_and_Conquer\closest_pair.py → D:\IITM_Source_codes\python-dsa-handbook\Dynamic_Programming\grid_paths.py
- `solve()` --calls--> `rob_memo()`  [INFERRED]
  D:\IITM_Source_codes\python-dsa-handbook\Divide_and_Conquer\closest_pair.py → D:\IITM_Source_codes\python-dsa-handbook\Dynamic_Programming\house_robber.py
- `solve()` --calls--> `lcs_memo()`  [INFERRED]
  D:\IITM_Source_codes\python-dsa-handbook\Divide_and_Conquer\closest_pair.py → D:\IITM_Source_codes\python-dsa-handbook\Dynamic_Programming\longest_common_subsequence.py
- `Queue` --calls--> `bfs_list()`  [INFERRED]
  D:\IITM_Source_codes\python-dsa-handbook\Data_Structures\queue_implementation.py → D:\IITM_Source_codes\python-dsa-handbook\Graph_Algorithms\breadth_first_search.py
- `Queue` --calls--> `bfs_matrix()`  [INFERRED]
  D:\IITM_Source_codes\python-dsa-handbook\Data_Structures\queue_implementation.py → D:\IITM_Source_codes\python-dsa-handbook\Graph_Algorithms\breadth_first_search.py

## Communities

### Community 0 - "Community 0"
Cohesion: 0.06
Nodes (25): heap_sort_max(), heap_sort_min(), MaxHeap, MinHeap, ================================================================================, Compares node with children and swaps with the SMALLEST child., Updates a specific index.          If new value is smaller than old, bubble UP., Linear search (O(n)) to find a value, then O(log n) update. (+17 more)

### Community 1 - "Community 1"
Cohesion: 0.06
Nodes (29): bfs_list(), bfs_matrix(), compact_bfs(), get_nbrs(), ================================================================================, Shortest BFS implementation using a simple list as a queue.     G: graph, s: st, Breadth-First Search on an Adjacency List.     G: graph dictionary, s: start no, Helper to find neighbors in matrix M for row 'r'. (+21 more)

### Community 2 - "Community 2"
Cohesion: 0.12
Nodes (27): buildFlatTopics(), closeCmdPalette(), escapeHtml(), getProgress(), handleMarkComplete(), handlePaletteKeydown(), handlePaletteOverlayClick(), highlightMatch() (+19 more)

### Community 3 - "Community 3"
Cohesion: 0.08
Nodes (21): compact_solve(), dist(), find_closest(), ================================================================================, Self-contained lightning-fast version of Closest Pair problem.     pts: list of, Calculate Euclidean distance between two points p1 and p2., Recursively finds the minimum distance between points.     px: points sorted by, Starter function that pre-sorts points and calls the solver.     pts: list of i (+13 more)

### Community 4 - "Community 4"
Cohesion: 0.12
Nodes (12): AVLTree, ================================================================================, Right Rotation: Shifting the tree to fix a Left-Heavy tilt., Inserts a new value x and rebalances the tree., Checks balance factors and performs rotations if needed., Recomputes heights top-down for the whole subtree., Traversal: Left -> Root -> Right (produces sorted list)., Traversal: Root -> Left -> Right (visualizes root hierarchy). (+4 more)

### Community 5 - "Community 5"
Cohesion: 0.11
Nodes (10): applyXRay(), initDSACanvas(), ================================================================================, Implements a Stack (LIFO) using TWO Queues.     In this version, we make 'Push', Adds item x to the stack. (Costly O(n) operation), Removes the top item. (Fast O(1) operation), Implements a Stack (LIFO) using only ONE Queue.     We rotate the queue to make, Adds item x to the stack. (O(n) rotation) (+2 more)

### Community 6 - "Community 6"
Cohesion: 0.2
Nodes (8): FPDF, DSACheatsheetPDF, generate(), Replaces non-ASCII characters that cause FPDF errors., Recursively sanitizes all strings in a JSON object (list or dict)., Renders text with bold segments (**text**) and superscripts (n^2)., sanitize_payload(), sanitize_text()

### Community 7 - "Community 7"
Cohesion: 0.17
Nodes (8): Node, ================================================================================, Removes the first occurrence of target value 't'., Prints the entire list structure., A single link in the chain. knows its value and the next person in line., Checks if the node is empty., Appends a new value x to the end of the chain (Recursive)., Inserts a new value x at the current front position.

### Community 8 - "Community 8"
Cohesion: 0.16
Nodes (8): LinkedList, Node, ================================================================================, Displays all nodes in the list., Holds a value and a link to the next node., Manages the collection of Nodes as a single List., Checks if the list has any nodes., Removes the first node containing target value 't'.

### Community 9 - "Community 9"
Cohesion: 0.17
Nodes (7): ================================================================================, Simulates a Last-In, First-Out (LIFO) stack., Checks if the stack is currently empty., Adds item x to the top of the stack., Removes and returns the top item from the stack., Displays the stack's current state., Stack

### Community 10 - "Community 10"
Cohesion: 0.21
Nodes (9): compact_kruskal(), DSU, kruskal(), ================================================================================, n: vertices, E: (w,u,v) list. Minimalist MST cost., Disjoint Set Union (Union-Find) to detect cycles and merge groups.      n: numb, Returns the 'Chief' (root) of node i's group., Merges groups containing i and j. Returns True if merged. (+1 more)

### Community 11 - "Community 11"
Cohesion: 0.2
Nodes (6): ================================================================================, Keeps track of non-overlapping sets (teams)., Initializes each element in x_list as its own set., Returns the official leader of the set containing x., Merges the sets containing elements 'a' and 'b'., UnionFind

### Community 12 - "Community 12"
Cohesion: 0.24
Nodes (9): fast_select(), get_pivot(), partition(), quick_select(), ================================================================================, Compact version using list comprehensions.     L: list, k: index, Returns the first element as the pivot.     L: list of elements, Moves elements smaller than 'pvt' to the left.     L: list, low: start index, h (+1 more)

### Community 13 - "Community 13"
Cohesion: 0.2
Nodes (9): fib_memoization(), fib_optimized(), fib_recursive(), fib_tabulation(), ================================================================================, Standard recursion: extremely slow for large n., Uses a dictionary to remember previous results., Builds a table from 0 upwards. (+1 more)

### Community 14 - "Community 14"
Cohesion: 0.2
Nodes (9): compact_dfs(), dfs_iter(), dfs_rec(), ================================================================================, Recursive DFS in minimal code using a set.     G: graph, s: current node, v: vi, Depth-First Search using a manual LIFO stack.     G: adjacency list, s: start n, Helper to setup trackers for recursive DFS., Recursive DFS explorer.     G: graph, v: visited dict, p: parent dict, curr: cu (+1 more)

### Community 15 - "Community 15"
Cohesion: 0.24
Nodes (7): huffman_heap(), huffman_simple(), Node, ================================================================================, Uses a Min-Heap (heapq) for O(n log n) efficiency., A single spot in the Huffman Tree., Builds codes by repeatedly sorting leaf nodes.

### Community 16 - "Community 16"
Cohesion: 0.29
Nodes (7): count_inversions(), fast_count(), merge_and_count(), ================================================================================, Compact recursive inversion counter.     A: array list, Combines two sorted lists and counts 'Split Inversions'.     L: left sorted lis, Recursively counts inversions in list A.     A: input list

### Community 17 - "Community 17"
Cohesion: 0.32
Nodes (7): fast_select(), moms(), partition(), ================================================================================, Finds the median of medians for a stable pivot.     L: list of elements, Standard Partition around a specific value 'v'.     L: list, low: start index,, Fast Select (QuickSelect) with MoM pivot.     L: list, low/high: search range,

### Community 18 - "Community 18"
Cohesion: 0.25
Nodes (7): compact_dijkstra(), dijkstra(), get_path(), ================================================================================, Rebuilds the path sequence from start to target 't'., G: graph, s: source node. Returns all shortest distances., Finds shortest path from s to t in graph G.     G: adjacency list [ (nbr, weigh

### Community 19 - "Community 19"
Cohesion: 0.43
Nodes (6): extract_takeaways(), main(), Replaces non-ASCII characters that cause FPDF errors., Finds the 'Key Takeaways' section and extracts bullet points., sanitize_text(), slugify()

### Community 20 - "Community 20"
Cohesion: 0.47
Nodes (5): load_file_content(), main(), Converts 'Selection Sort' to 'selection_sort, Loads content of a file if it exists, otherwise returns empty string., slugify()

### Community 21 - "Community 21"
Cohesion: 0.33
Nodes (5): compact_mul(), fast_mul(), ================================================================================, Karatsuba multiplication: Reduces 4 multiplications to 3.     x, y: large integ, Extremely short Karatsuba. x,y: numbers

### Community 22 - "Community 22"
Cohesion: 0.33
Nodes (5): bellman_ford(), compact_bf(), ================================================================================, Finds shortest paths from source s in graph with n nodes.     E: list of edges, E: edges, n: node count, s: start. Minimal implementation.

### Community 23 - "Community 23"
Cohesion: 0.33
Nodes (5): compact_fw(), floyd_warshall(), ================================================================================, Computes all-pairs shortest paths on adjacency matrix M.     M: a 2D grid where, M: 2D matrix. Returns shortest all-to-all path matrix.

### Community 24 - "Community 24"
Cohesion: 0.33
Nodes (5): compact_prim(), prim_mst(), ================================================================================, Prim's algorithm to find Minimum Spanning Tree cost.     G: adjacency list [ (n, G: adjacency list. Returns MST cost using a heap.

### Community 25 - "Community 25"
Cohesion: 0.33
Nodes (5): Shortest Path using Depth First Search (DFS) ===================================, Finds the shortest path in an unweighted graph using exhaustive DFS.     Returns, Finds the shortest path in a weighted graph using exhaustive DFS with pruning., shortest_path_unweighted_dfs(), shortest_path_weighted_dfs()

### Community 26 - "Community 26"
Cohesion: 0.33
Nodes (5): ================================================================================, Finds target 't' in sorted list 'L' using a loop.     L: sorted list, t: target, Finds target 't' in sorted list 'L' using recursion.     L: sorted list, t: tar, search_iterative(), search_recursive()

### Community 27 - "Community 27"
Cohesion: 0.4
Nodes (5): merge(), merge_sort(), ================================================================================, Zips two sorted lists into one unified sorted list., Recursively splits the list and merges it back in sorted order.

### Community 28 - "Community 28"
Cohesion: 0.4
Nodes (5): partition(), quick_sort(), ================================================================================, Rearranges the list around a pivot element.     Returns the final position of t, Recursively sorts the list using partitioning.

### Community 29 - "Community 29"
Cohesion: 0.4
Nodes (3): lcs_substring_optimized(), ================================================================================, To calculate the current row, we only need information from      the PREVIOUS ro

### Community 30 - "Community 30"
Cohesion: 0.5
Nodes (3): ================================================================================, Selects the maximum number of non-overlapping intervals.     intervals: list of, schedule()

### Community 31 - "Community 31"
Cohesion: 0.5
Nodes (3): ================================================================================, Minimizes max lateness by sorting jobs by deadline.     jobs: list of (id, dura, schedule()

### Community 32 - "Community 32"
Cohesion: 0.5
Nodes (3): insertion_sort(), ================================================================================, Sorts a list by picking items and sliding them into their correct slots.     L:

### Community 33 - "Community 33"
Cohesion: 0.5
Nodes (3): ================================================================================, Sorts a list by picking the smallest item and putting it at the front.     L: i, selection_sort()

### Community 34 - "Community 34"
Cohesion: 1.0
Nodes (0): 

### Community 35 - "Community 35"
Cohesion: 1.0
Nodes (0): 

## Knowledge Gaps
- **171 isolated node(s):** `Renders text with bold segments (**text**) and superscripts (n^2).`, `Replaces non-ASCII characters that cause FPDF errors.`, `Recursively sanitizes all strings in a JSON object (list or dict).`, `Converts 'Selection Sort' to 'selection_sort`, `Loads content of a file if it exists, otherwise returns empty string.` (+166 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 34`** (1 nodes): `dsa_book_data.js`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 35`** (1 nodes): `update_handbook.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `StackOneQueue` connect `Community 5` to `Community 0`?**
  _High betweenness centrality (0.110) - this node is a cross-community bridge._
- **Why does `compact_bfs()` connect `Community 1` to `Community 2`?**
  _High betweenness centrality (0.067) - this node is a cross-community bridge._
- **Why does `initDSACanvas()` connect `Community 5` to `Community 2`?**
  _High betweenness centrality (0.051) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `Queue` (e.g. with `bfs_list()` and `bfs_matrix()`) actually correct?**
  _`Queue` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Renders text with bold segments (**text**) and superscripts (n^2).`, `Replaces non-ASCII characters that cause FPDF errors.`, `Recursively sanitizes all strings in a JSON object (list or dict).` to the rest of the system?**
  _171 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.06 - nodes in this community are weakly interconnected._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.06 - nodes in this community are weakly interconnected._