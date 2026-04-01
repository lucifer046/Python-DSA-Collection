<!-- +------------------------------------------------------+ -->
<!-- |      FLOYD-WARSHALL — ALL-PAIRS SHORTEST PATH        | -->
<!-- +------------------------------------------------------+ -->
# Floyd-Warshall — All-Pairs Shortest Path

## What is Floyd-Warshall?

Imagine you are an **airline logistics manager**. You need a **master table** that shows the shortest flying path between EVERY combination of cities in the world (e.g., London to Tokyo, Paris to New York, Sydney to Dubai).

> **Simple Definition:** Floyd-Warshall finds the **absolute shortest distance** between **every possible pair** of nodes in a graph at once!

Unlike Dijkstra's (which starts at ONE node), Floyd-Warshall finds the answers for **everyone**!

---

## The "Transitive" Strategy

Floyd-Warshall works using **Dynamic Programming**. It asks a simple question:

*"Is it cheaper to go from **A** to **C** directly, or is it better to stop at **B** in the middle?"*

---

## Step-by-Step Evolution

### Step 1: The Adjacency Matrix
Start with a grid showing the **direct** costs between nodes.

```
      A    B    C
   A [0   3   INF]
   B [2   0    4 ]  <-- B to C costs 4
   C [INF 1    0 ]  <-- C to B costs 1
```

### Step 2: Try Every Middle Point (The Magic)
We cycle through every node (like `k = B`) and use it as a "layover city" to see if it provides a shortcut.

```
   Checking shortcut through B:
   Can we go A -> B -> C cheaper than A -> C?
   A -> B is 3, B -> C is 4. Total = 7.
   Since 7 < INF, we found a path! Update A -> C to 7! ✅
```

---

## Visualizing the Process

```
   (3)        (4)
   A ------> B ------> C
   ^                   |
   |                   |
   +------- (7) -------+  <--- Floyd-Warshall finds 
                               that A to C is 3 + 4 = 7!
```

---

## Comparing Algorithms

| Feature | Dijkstra | Bellman-Ford | Floyd-Warshall |
| :--- | :--- | :--- | :--- |
| **Goal** | One node to all others | One node to all others | **ALL nodes to ALL nodes** |
| **Complexity** | $O(E \log V)$ | $O(VE)$ | $O(V^3)$ |
| **Negatives?** | No ❌ | Yes ✅ | Yes ✅ |
| **Best For** | Daily GPS/Navigation | Detecting negative cycles | Large offline path tables |

---

## Key Takeaways

1. **All-to-All:** A single run gives the distance matrix for the entire graph.
2. **Logic:** $dist(i,j) = \min(dist(i,j), dist(i,k) + dist(k,j))$.
3. **Negative Weights:** It can handle negative weights but NOT negative cycles.
4. **Performance:** $O(V^3)$ is slow for large graphs, so use it when the number of nodes is small (usually less than 500).
5. **Real-Life Use:** Transitive closure (finding "who knows whom"), network routing, and project scheduling.
