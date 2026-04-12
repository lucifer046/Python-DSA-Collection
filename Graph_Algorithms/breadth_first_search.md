<!-- +--------------------------------------------------------------+ -->
<!-- |  BREADTH-FIRST SEARCH (BFS) — LAYER-BY-LAYER EXPLORATION    | -->
<!-- +--------------------------------------------------------------+ -->
# Breadth-First Search (BFS) — Layer-by-Layer Exploration

## Theoretical Definition & Comparisons

**Theoretical Definition:** 
Breadth-First Search (BFS) is a graph traversal algorithm that explores the graph level-by-level (outward from the source node). It uses a Queue (FIFO structure) to process all neighbors of the current node before probing deeper.

**Comparison (Graph Traversals):**
*   **Breadth-First Search (BFS):** Best for finding the **shortest path in unweighted graphs**, discovering levels, or analyzing peer networks. Uses more memory for wide graphs (Queue).
*   **Depth-First Search (DFS):** Explores as deep as possible before backtracking. Best for cycle detection, topological sorting, solving mazes, and exhaustively searching paths. Uses a Stack/Recursion.

---

## What is BFS?

Imagine you **drop a stone in a pond**. Ripples spread outwards in perfect circles — first the closest ring, then the next ring, then the next.

**BFS explores a graph exactly like those ripples!** It visits ALL neighbors at distance 1, then ALL neighbors at distance 2, and so on.

> **Simple Definition:** BFS starts at one point and explores the graph **layer by layer**, visiting all nearby nodes before moving further away.

---

## Visual Representation

![BFS "Ripples in a Pond" Layer-by-Layer Diagram](docs/images/bfs_diagram.png)

> [!NOTE]
> **Teacher's Perspective:** "Imagine you **drop a stone in a calm pond**. Ripples spread outwards in perfect circles—first the circle right next to the stone, then the next circle, and then the next. **BFS** works exactly like those ripples! It visits all the 'Layer 1' neighbors first, then all the 'Layer 2' neighbors, and so on. It never moves to a deeper layer until it has finished exploring the current one. This 'fair' exploration is why BFS is the king of finding the **Shortest Path**!"

---

## Step-by-Step Breakdown (Teacher's Guide)

Let's see how the ripple spreads through a graph starting at Node **0**:

### 1. The Waiting Line (The Queue)
BFS is very organized. It uses a **Queue** (First-In, First-Out)—just like a line at a ticket counter. Whoever gets in line first gets processed first!

### 2. The First Ripple (Layer 1)
- We start at Node 0 and look at its immediate friends (let's say 1 and 2).
- We put 1 and 2 in the Queue.
- **Queue:** `[1, 2]`
- Node 0 is now done!

### 3. Spreading Out (Layer 2)
- Next in line is Node 1. We look at its friends (3 and 4).
- We put 3 and 4 in the Queue. 
- **Queue:** `[2, 3, 4]` (Notice 2 was already there, so it stays at the front!)
- Node 1 is done!

### 4. Finishing the Circle
- We keep taking nodes from the front of the line until the line is empty.
- Eventually, every node is visited in the exact order of their distance from the start!

---

---

## Steps to Perform (Visual Trace)

Let's watch the ripple spread from **Node 0** to its neighbors.

### 1. Start at Node 0
Node 0 is current. It sees 1 and 2.
- **Queue:** `[1, 2]`
```text
  [0]*  <-- Current
  / \
(1) (2)
 |   |
(3) (4)
```

### 2. Enter Layer 1: Process Node 1
Node 1 is taken from the queue. It sees 3 and 4.
- **Added to Queue:** 3, 4
- **Queue:** `[2, 3, 4]` (2 is still at the front!)
```text
  (0)
  / \
[1]* (2)  <-- Current
 |   |
(3) (4)
```

### 3. Enter Layer 1: Process Node 2
Node 2 is taken. No new neighbors found.
- **Queue:** `[3, 4]`
```text
  (0)
  / \
 (1) [2]* <-- Current
  |   |
 (3) (4)
```

### 4. Enter Layer 2: Process Node 3 & 4
Process Node 3, then Node 4. Both are "Layer 2" because they took 2 steps to reach.
```text
  (0)  (Layer 0)
  / \
 (1)-(2) (Layer 1)
  |   |
 [3]-[4] (Layer 2)
```

---

## Why is BFS the "Shortest Path" King?
Because BFS explores layer by layer, the **first time** it sees a node, it *must* have found the shortest way to get there. If it took a longer way, it would have seen that node in a later "ripple"!

---


---

## Two Ways to Store a Graph

### 1. Adjacency List (Dictionary)
```
  {
    0: [1, 2],      < "Node 0 is friends with 1 and 2"
    1: [3, 4],      < "Node 1 is friends with 3 and 4"
    2: [4, 3],
    3: [4],
    4: []
  }
```

### 2. Adjacency Matrix (Grid)
```
       0  1  2  3  4
    0 [0, 1, 1, 0, 0]    < Node 0 connects to 1 and 2
    1 [0, 0, 0, 1, 1]    < Node 1 connects to 3 and 4
    2 [0, 0, 0, 1, 1]
    3 [0, 0, 0, 0, 1]
    4 [0, 0, 0, 0, 0]

  '1' means connected, '0' means not connected
```

---

## Where is BFS Used?

| Use Case | How BFS Helps |
|---|---|
| **Shortest Path (unweighted)** | BFS always finds the shortest path in terms of number of steps |
| **Social Networks** | "Friends of friends" — people 2 connections away from you |
| **GPS (simple maps)** | Finding the fewest number of turns to reach somewhere |
| **Web Crawlers** | Google's crawler visits a webpage, then visits all the links on that page |

---

## Key Takeaways

1. BFS uses a **Queue** (First-In, First-Out)
2. It explores **layer by layer** — all neighbors first, then neighbors of neighbors
3. It guarantees the **shortest path** in unweighted graphs
4. It visits nodes in **increasing order of distance** from the start
5. Works like ripples in a pond — spreading outwards evenly!

