<!-- +----------------------------------------------------------+ -->
<!-- |  MST VIA DIJKSTRA LOGIC — THE UNIFIED GREEDY APPROACH    | -->
<!-- +----------------------------------------------------------+ -->
# MST via Dijkstra Logic — The Unified Greedy Approach

## Theoretical Definition & Comparisons

**Theoretical Definition:** 
Minimum Spanning Tree (MST) and Shortest Path (SP) algorithms share a common mathematical heritage: **Greedy Priority-Queue Expansion**. By slightly modifying the "Relaxation" step in Dijkstra's algorithm, we can transform it into Prim's algorithm for MST construction.

## The Logic Bridge

| Feature | Dijkstra's Algorithm (SP) | Prim's Algorithm (MST) |
|---|---|---|
| **Relaxation Step** | `if d[v] > d[u] + w` | `if d[v] > w` |
| **Logic** | Minimize **cumulative** distance from source. | Minimize **local** edge weight to the tree. |
| **Engine** | Min-Priority Queue | Min-Priority Queue |
| **Goal** | Find the best path to one node. | Find the best connection for the whole group. |

---

## What is the Dijkstra Logic Connection?

Imagine you are building a **water pipeline** (MST) vs. finding a **GPS route** (Shortest Path).

### 1. The Shortest Path (Dijkstra)
In Dijkstra, you care about the **total trip length**. If you are at Node A and looking at Node C, you ask: "How far is it from my *original house* to C through A?" 

### 2. The MST (Prim)
In Prim, you only care about the **cost of the pipe**. You don't care how far Node C is from your house; you just want to know: "What is the cheapest way to connect Node C to the *existing pipe network*?"

> **Simple Definition:** Prim's Algorithm is essentially Dijkstra's Algorithm where the "distance" to a node is just the weight of the single edge connecting it, rather than the sum of all edges from the start.

---

## Step-by-Step Breakdown (The Swap)

To turn Dijkstra into Prim, we only change **one line of code**:

### Dijkstra's Step:
```python
if dist[neighbor] > dist[current] + weight:
    dist[neighbor] = dist[current] + weight
```

### Prim's Step:
```python
if dist[neighbor] > weight:
    dist[neighbor] = weight
```

**Why does this work?**
Because in an MST, we are trying to connect a new node to *anywhere* in our current tree for the lowest price. We don't care about the path back to the start; we only care that it is now "connected."

---

## Kruskal's Connection: Global Greedy
While Prim is a "local" expansion like Dijkstra, **Kruskal's** is a "global" greedy approach. It uses a Priority Queue to store **every single edge** in the graph and picks the cheapest one first. This is the same fundamental "Process Cheapest First" logic that powers Dijkstra!

---

## Key Takeaways

1. **Prim is Dijkstra** with a different relaxation formula
2. **Kruskal is Dijkstra** on edges instead of nodes
3. Both use a **Priority Queue** to make the "best local choice"
4. The **Min-Heap** is the engine that drives all three algorithms
5. Understanding one makes it much easier to master the others!
