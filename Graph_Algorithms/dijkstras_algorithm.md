<!-- +------------------------------------------------------+ -->
<!-- |  DIJKSTRA'S ALGORITHM — THE SMARTEST PATH FINDER    | -->
<!-- +------------------------------------------------------+ -->
# Dijkstra's Algorithm — The Smartest Path Finder

## Theoretical Definition & Comparisons

**Theoretical Definition:** 
Dijkstra's algorithm is a greedy algorithm that finds the shortest path from a single source vertex to all other vertices in a weighted graph with strictly non-negative edge weights.

## Shortest Path Algorithms Comparison

While Dijkstra's is the most common, different graph scenarios require different shortest-path strategies:

| Feature | Dijkstra's Algorithm | Bellman-Ford Algorithm | Floyd-Warshall Algorithm |
|---|---|---|---|
| **Goal** | Single-Source Shortest Path | Single-Source Shortest Path | **All-Pairs** Shortest Path |
| **Negative Weights** | **NO** ❌ | **YES** ✅ | **YES** ✅ |
| **Cycle Detection** | ❌ No | ✅ Detects Negative Cycles | ✅ Detects Negative Cycles |
| **Strategy** | Greedy (Priority Queue) | Iterative Relaxation | Dynamic Programming |
| **Complexity** | $O(E \log V)$ | $O(V \times E)$ | $O(V^3)$ |
| **Best Use Case** | Standard maps & networks. | Graphs with potential negative costs. | When you need paths between *every* city pairs. |

---

## What is Dijkstra's Algorithm?

Imagine you're using **Google Maps** to find the fastest route from your home to your office. Each road has a **travel time** (weight). Dijkstra's Algorithm finds the **absolute shortest path** considering all road times.

**Dijkstra's Algorithm** is the gold standard for finding the shortest path, but it has one major rule: every road **MUST** have a positive weight.

### The Golden Rule of Negatives
- **Negative Weights?** NO ❌. Dijkstra's greedy nature assumes once a node is visited, its distance is finalized. A negative weight later on would break its brain!
- **Negative Cycles?** NO ❌. If it can't handle single negative weights, it definitely can't handle loops that subtract cost infinitely.

> **Simple Definition:** Dijkstra's finds the cheapest/fastest/shortest path between two points in a graph carefully picking the closest city first. It only works if all costs are positive.

---

## Visual Representation

![Dijkstra's Shortest Path "GPS" Diagram](docs/images/dijkstra_diagram.png)

> [!NOTE]
> **Teacher's Perspective:** "Imagine you're using **Google Maps** to get to a concert. There are many roads, but some have heavy traffic (high cost) and some are clear highways (low cost). **Dijkstra's Algorithm** is the brain inside your GPS! It starts at your house and 'explores' every road, but it's very smart—it always focuses on the path that currently has the **lowest total time**. This clever 'greedy' strategy ensures that when it finally reaches the concert hall, it has found the absolute fastest way to get there!"

---

## Step-by-Step Breakdown (Teacher's Guide)

Let's find the shortest path from your House (0) to the Concert (4):

### 1. The Scoreboard (Initialization)
Before we start, we write "Infinity" (∞) on every node because we don't know the cost yet. The only node we know is our House (0), which has a cost of **0**.

### 2. Checking the Neighbors
- We look at the roads leading out of our House. Node 1 costs 4 minutes, and Node 2 costs 2 minutes.
- We update our scoreboard: `Node 1 = 4`, `Node 2 = 2`.
- **The Rule:** We *always* pick the cheapest unvisited node next. So, we go to **Node 2**!

### 3. The "Wait, I Found a Shortcut!" (Relaxation)
- From Node 2, we see a road to Node 1 that only costs 1 minute.
- Now, think: We already knew a way to Node 1 that took 4 minutes (directly from House). 
- But now we see: `House -> Node 2 -> Node 1` only takes `2 + 1 = 3` minutes!
- **Scoreboard Update:** We erase "4" and write **"3"**. 
- This update is called **Relaxation**—we've found a better, "more relaxed" way to get there!

### 4. Reaching the Goal
We keep picking the cheapest node and updating the scoreboard until we've visited our destination. The final number on the Concert (Node 4) is our guaranteed shortest time!

---

## Why "Greedy" works here?
Because Dijkstra *always* picks the shortest known path first, it builds the solution bit by bit. It's like building a puzzle where you only ever place the pieces that you're 100% sure about. By the time the puzzle is finished, you know it's perfect!

---


---

## The "Relaxation" Concept

**Relaxation** is the key move in Dijkstra's. It means:  
*"I found a CHEAPER way to get there - let me UPDATE the cost!"*

```
  BEFORE relaxation:
  Distance to node 1 = 4  (via path: 0 > 1)
  
  AFTER relaxation:
  Distance to node 1 = 3  (via path: 0 > 2 > 1)  < CHEAPER! Update! ✅
```

Think of it like this: You thought it took 4 hours to get to City B. But then you discovered a shortcut through City C that only takes 3 hours. You "relax" your estimate!

---

## Limitation: No Negative Weights!

```
  Dijkstra WORKS:             Dijkstra FAILS:
  
    A --(3)--> B                A --(3)--> B
    |         |                 |         |
   (2)      (1)               (2)      (-5)  < NEGATIVE!
    |         |                 |         |
    C --------+                 C --------+
    
  All costs positive ✅        Has negative cost ❌
                               (Use Bellman-Ford instead!)
```

---

## Steps to Perform (Execution Trace)

Let's trace Dijkstra's algorithm step-by-step on a 5-node graph. Our goal is to find the shortest path from **Node 0** to all other nodes.

### 1. Initialization
Everyone starts at $\infty$ except the source (Node 0).
```text
(0)---[0]---(1)---[∞]
 |  \        | 
[2]  [4]    [5]
 |     \     | 
(2)---[∞]---(3)---[∞]
 |           | 
[10]        [2]
 |           | 
(4)-----------[∞]
```
**Queue:** `[(0, Node 0)]`

### 2. Process Node 0 (The Start)
Look at neighbors (1, 2).
- Node 1: $0 + 4 = 4$
- Node 2: $0 + 2 = 2$
```text
(0)*--[0]---(1)---[4] 
 |  \        | 
[2]  [4]    [5]
 |     \     | 
(2)---[2]   (3)---[∞]
```
**Queue:** `[(2, Node 2), (4, Node 1)]`

### 3. Process Node 2 (Greedy Choice)
Pick **Node 2** (Cost 2) because it's the smallest in the queue. Look at neighbors (3, 4).
- Node 3: $2 + 8 = 10$
- Node 4: $2 + 10 = 12$
```text
(0)---[0]---(1)---[4]
 |  \        | 
[2]  [4]    [5]
 |     \     | 
(2)*--[2]---(3)---[10]
 |           | 
[10]        [2]
 |           | 
(4)-----------[12]
```
**Queue:** `[(4, Node 1), (10, Node 3), (12, Node 4)]`

### 4. Process Node 1 (Relaxation)
Pick **Node 1** (Cost 4). Check neighbor (3).
- **Shortcut found!** $4 (\text{at } 1) + 5 (\text{edge}) = 9$. This is better than the existing $10$ at Node 3. Update!
```text
(0)---[0]---(1)*--[4]
 |  \        | 
[2]  [4]    [5]   <-- Relaxing this path!
 |     \     | 
(2)---[2]---(3)---[9] ✅ (Was 10)
```
**Queue:** `[(9, Node 3), (12, Node 4)]`

### 5. Finalize Node 3 & 4
Process **Node 3** (Cost 9). Check neighbor (4).
- **Shortcut found!** $9 (\text{at } 3) + 2 (\text{edge}) = 11$. Better than the existing $12$ at Node 4. Update!
```text
(3)*--[9]---(4)---[11] ✅ (Was 12)
```
**Result:** All nodes visited. Final costs: `[0, 4, 2, 9, 11]`.

---

## Key Takeaways

1. Dijkstra's finds the **shortest path in a weighted graph**
2. It uses **Relaxation** — keep updating distances when shorter paths are found
3. It's **Greedy** — always processes the cheapest unvisited node
4. Time complexity: **O((V+E) log V)** with a priority queue
5. **Cannot handle negative edge weights** — use Bellman-Ford for that
6. Used in **GPS navigation, network routing, and game pathfinding**


