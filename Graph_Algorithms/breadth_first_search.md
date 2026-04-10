<!-- +--------------------------------------------------------------+ -->
<!-- |  BREADTH-FIRST SEARCH (BFS) — LAYER-BY-LAYER EXPLORATION    | -->
<!-- +--------------------------------------------------------------+ -->
# Breadth-First Search (BFS) — Layer-by-Layer Exploration

## What is BFS?

Imagine you **drop a stone in a pond**. Ripples spread outwards in perfect circles — first the closest ring, then the next ring, then the next.

**BFS explores a graph exactly like those ripples!** It visits ALL neighbors at distance 1, then ALL neighbors at distance 2, and so on.

> **Simple Definition:** BFS starts at one point and explores the graph **layer by layer**, visiting all nearby nodes before moving further away.

---

## 🖼️ Visual Representation

![BFS "Ripples in a Pond" Layer-by-Layer Diagram](docs/images/bfs_diagram.png)

> [!NOTE]
> **Teacher's Perspective:** "Imagine you **drop a stone in a calm pond**. Ripples spread outwards in perfect circles—first the circle right next to the stone, then the next circle, and then the next. **BFS** works exactly like those ripples! It visits all the 'Layer 1' neighbors first, then all the 'Layer 2' neighbors, and so on. It never moves to a deeper layer until it has finished exploring the current one. This 'fair' exploration is why BFS is the king of finding the **Shortest Path**!"

---

## 🎓 Step-by-Step Breakdown (Teacher's Guide)

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

## 🧠 Why is BFS the "Shortest Path" King?
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

