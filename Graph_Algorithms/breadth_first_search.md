<!-- ╔══════════════════════════════════════════════════════════════╗ -->
<!-- ║  BREADTH-FIRST SEARCH (BFS) — LAYER-BY-LAYER EXPLORATION    ║ -->
<!-- ╚══════════════════════════════════════════════════════════════╝ -->
# Breadth-First Search (BFS) — Layer-by-Layer Exploration

## What is BFS?

Imagine you **drop a stone in a pond**. Ripples spread outwards in perfect circles — first the closest ring, then the next ring, then the next.

**BFS explores a graph exactly like those ripples!** It visits ALL neighbors at distance 1, then ALL neighbors at distance 2, and so on.

> **Simple Definition:** BFS starts at one point and explores the graph **layer by layer**, visiting all nearby nodes before moving further away.

---

## First: What is a Graph?

A **graph** is just a collection of **dots** (called Nodes) connected by **lines** (called Edges).

```
  Example Graph:

       0 ─────── 1
       │        ╱ │
       │      ╱   │
       │    ╱     │
       2 ─╱      │
       │  ╲      │
       │    ╲    │
       │      ╲  │
       3 ─────── 4

  Node 0 connects to: 1, 2
  Node 1 connects to: 3, 4
  Node 2 connects to: 4, 3
  Node 3 connects to: 4
  Node 4 connects to: (nothing outgoing)
```

---

## BFS Traversal — Step by Step

### Starting Node: **0**

**BFS uses a QUEUE (First-In, First-Out)** — like a ticket counter line!

---

### Step 1: Start at node 0

```
  Queue:   [0]
  Visited: {0}

       ●0 ─────── 1
       │        ╱ │
       │      ╱   │
       2          │
       │          │
       3 ─────── 4

  ● = Currently processing (Layer 0)
```

### Step 2: Process node 0 → Add its neighbors (1, 2) to the queue

```
  Queue:   [1, 2]     ← Added neighbors of 0
  Visited: {0, 1, 2}

       [done]0 ─────── ○1
       │        ╱  │
       │      ╱    │
       ○2         │
       │           │
       3 ─────── 4

  [done] = Done    ○ = In queue (Layer 1)
```

### Step 3: Process node 1 → Add its unvisited neighbors (3, 4)

```
  Queue:   [2, 3, 4]  ← 1 is done, added 3 and 4
  Visited: {0, 1, 2, 3, 4}

       [done]0 ─────── [done]1
       │        ╱   │
       │      ╱     │
       ○2          │
       │            │
       ○3 ─────── ○4

  ○ = In queue (Layer 2)
```

### Step 4: Process node 2 → Neighbors 4 and 3 already visited!

```
  Queue:   [3, 4]     ← Nothing new to add
  Visited: {0, 1, 2, 3, 4}

       [done]0 ─────── [done]1
       │        ╱   │
       [done]2          │
       │            │
       ○3 ─────── ○4
```

### Step 5: Process node 3 → Neighbor 4 already visited

```
  Queue:   [4]
  Visited: {0, 1, 2, 3, 4}

       [done]0 ─────── [done]1
       │        ╱   │
       [done]2          │
       │            │
       [done]3 ─────── ○4
```

### Step 6: Process node 4 → No new neighbors. We're done!

```
  Queue:   []   ← EMPTY! All done!
  Visited: {0, 1, 2, 3, 4}

       [done]0 ─────── [done]1
       │        ╱   │
       [done]2          │
       │            │
       [done]3 ─────── [done]4

  BFS Order: 0 → 1 → 2 → 3 → 4
```

---

## Layer-by-Layer View

```
                Layer 0:        0
                               / \
                Layer 1:      1   2
                             / \ /
                Layer 2:    3   4

  BFS visits Layer 0 fully, then Layer 1 fully, then Layer 2 fully.
  Order: 0, 1, 2, 3, 4
```

---

## Two Ways to Store a Graph

### 1. Adjacency List (Dictionary)
```
  {
    0: [1, 2],      ← "Node 0 is friends with 1 and 2"
    1: [3, 4],      ← "Node 1 is friends with 3 and 4"
    2: [4, 3],
    3: [4],
    4: []
  }
```

### 2. Adjacency Matrix (Grid)
```
       0  1  2  3  4
    0 [0, 1, 1, 0, 0]    ← Node 0 connects to 1 and 2
    1 [0, 0, 0, 1, 1]    ← Node 1 connects to 3 and 4
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
