<!-- +------------------------------------------------------+ -->
<!-- |  DIJKSTRA'S ALGORITHM — THE SMARTEST PATH FINDER    | -->
<!-- +------------------------------------------------------+ -->
# Dijkstra's Algorithm — The Smartest Path Finder

## What is Dijkstra's Algorithm?

Imagine you're using **Google Maps** to find the fastest route from your home to your office. Each road has a **travel time** (weight). Dijkstra's Algorithm finds the **absolute shortest path** considering all road times.

> **Simple Definition:** Dijkstra's finds the cheapest/fastest/shortest path between two points in a graph where each edge has a **cost** (weight).

---

## The Graph We'll Use

```
          (4)           (5)
    [0] --------- [1] --------- [3]
     |             |             |
    (2)           (1)           (2)
     |             |             |
    [2] -----------+           [4]
     |                          |
     |           (10)           |
     +--------------------------+

  Adjacency List & Costs:
  Node 0: > 1(4), > 2(2)
  Node 1: > 0(4), > 2(1), > 3(5)
  Node 2: > 0(2), > 1(1), > 4(10)
  Node 3: > 1(5), > 4(2)
  Node 4: > 2(10), > 3(2)
```

---

## Finding Shortest Path: 0 --> 4

### Step 1: Initialize — Everything starts at "infinity" (unknown)

```
  +------+----------+---------+
  | Node | Distance | Visited |
  +------+----------+---------+
  |  0   |    0     |   No    |  < Start here! Distance = 0
  |  1   |    ∞     |   No    |
  |  2   |    ∞     |   No    |
  |  3   |    ∞     |   No    |
  |  4   |    ∞     |   No    |
  +------+----------+---------+
```

### Step 2: Process node 0 (cheapest unvisited = 0 with distance 0)

```
  From node 0, we can reach:
  • Node 1 via cost 4:  0 + 4 = 4   (4 < ∞? YES! Update!)
  • Node 2 via cost 2:  0 + 2 = 2   (2 < ∞? YES! Update!)

  +------+----------+---------+------------------------+
  | Node | Distance | Visited | How we got there        |
  +------+----------+---------+------------------------+
  |  0   |    0     |   ✅    | Start                   |
  |  1   |    4     |   No    | 0 > 1 (cost 4)         |
  |  2   |    2     |   No    | 0 > 2 (cost 2)         |
  |  3   |    ∞     |   No    |                         |
  |  4   |    ∞     |   No    |                         |
  +------+----------+---------+------------------------+
```

### Step 3: Process node 2 (cheapest unvisited = 2 with distance 2)

```
  From node 2, we can reach:
  • Node 0: already visited, skip
  • Node 1 via cost 1:  2 + 1 = 3   (3 < 4? YES! SHORTER PATH FOUND!)
  • Node 3 via cost 8:  2 + 8 = 10  (10 < ∞? YES!)
  • Node 4 via cost 10: 2 + 10 = 12 (12 < ∞? YES!)

  +------+----------+---------+------------------------+
  | Node | Distance | Visited | How we got there        |
  +------+----------+---------+------------------------+
  |  0   |    0     |   ✅    | Start                   |
  |  1   |    3 ⬇️  |   No    | 0 > 2 > 1 (cost 2+1)  |
  |  2   |    2     |   ✅    | 0 > 2 (cost 2)         |
  |  3   |   10     |   No    | 0 > 2 > 3 (cost 2+8)  |
  |  4   |   12     |   No    | 0 > 2 > 4 (cost 2+10) |
  +------+----------+---------+------------------------+

  ⬇️ = Distance was REDUCED! This is called "RELAXATION"
```

### Step 4: Process node 1 (cheapest unvisited = 1 with distance 3)

```
  From node 1, we can reach:
  • Node 0: already visited, skip
  • Node 2: already visited, skip
  • Node 3 via cost 5:  3 + 5 = 8   (8 < 10? YES! SHORTER PATH FOUND!)

  +------+----------+---------+------------------------+
  | Node | Distance | Visited | How we got there        |
  +------+----------+---------+------------------------+
  |  0   |    0     |   ✅    | Start                   |
  |  1   |    3     |   ✅    | 0 > 2 > 1              |
  |  2   |    2     |   ✅    | 0 > 2                   |
  |  3   |    8 ⬇️  |   No    | 0 > 2 > 1 > 3 (2+1+5) |
  |  4   |   12     |   No    | 0 > 2 > 4              |
  +------+----------+---------+------------------------+
```

### Step 5: Process node 3 (cheapest unvisited = 3 with distance 8)

```
  From node 3, we can reach:
  • Node 4 via cost 2:  8 + 2 = 10   (10 < 12? YES! SHORTER PATH FOUND!)

  +------+----------+---------+------------------------------+
  | Node | Distance | Visited | How we got there              |
  +------+----------+---------+------------------------------+
  |  0   |    0     |   ✅    | Start                         |
  |  1   |    3     |   ✅    | 0 > 2 > 1                    |
  |  2   |    2     |   ✅    | 0 > 2                         |
  |  3   |    8     |   ✅    | 0 > 2 > 1 > 3                |
  |  4   |   10 ⬇️  |   No    | 0 > 2 > 1 > 3 > 4 (2+1+5+2)|
  +------+----------+---------+------------------------------+
```

### Step 6: Process node 4 — This is our DESTINATION! 🎉

```
  SHORTEST PATH FROM 0 TO 4:
  
  0 --(2)--> 2 --(1)--> 1 --(5)--> 3 --(2)--> 4
  
  Total Cost: 2 + 1 + 5 + 2 = 10 ✅
```

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

## Key Takeaways

1. Dijkstra's finds the **shortest path in a weighted graph**
2. It uses **Relaxation** — keep updating distances when shorter paths are found
3. It's **Greedy** — always processes the cheapest unvisited node
4. Time complexity: **O((V+E) log V)** with a priority queue
5. ⚠️ **Cannot handle negative edge weights** — use Bellman-Ford for that
6. Used in **GPS navigation, network routing, and game pathfinding**
