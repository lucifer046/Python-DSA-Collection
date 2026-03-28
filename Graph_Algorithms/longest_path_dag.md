<!-- +------------------------------------------------------+ -->
<!-- |  LONGEST PATH IN DAG — THE CRITICAL PATH METHOD      | -->
<!-- +------------------------------------------------------+ -->
# Longest Path in DAG — The Critical Path Method

## What is the Longest Path?

Imagine you're **building a spaceship**. There are many tasks to complete: build the engine, wire the electronics, assemble the cabin, paint the exterior. Some tasks can happen **at the same time**, but many must **wait** for others.

The **Longest Path** through this dependency map tells NASA exactly how long the **entire project** will take. Even if some tasks finish early, the project isn't done until the **longest chain** of dependent tasks is complete!

> **Simple Definition:** The Longest Path in a DAG (Directed Acyclic Graph) finds the **maximum number of steps** needed to reach each node from the starting points.

---

## Why "Longest" Instead of "Shortest"?

```
  Building a House:
  
  Foundation (2 days) --> Walls (5 days) --> Roof (3 days)    = 10 days
  Foundation (2 days) --> Plumbing (1 day)                     = 3 days
  Foundation (2 days) --> Electrical (2 days)                  = 4 days
  
  ALL three branches must finish before the house is done.
  The house takes 10 days (the LONGEST path), not 3!
  
  The longest path = The EARLIEST the project can finish!
```

---

## Step-by-Step Example

### The DAG:

```
  0 > 2, 3, 4
  1 > 2, 7
  2 > 5
  3 > 5, 7
  4 > 7
  5 > 6
  6 > 7
  7 > (end)

  Visual:
  
  0--->2--->5--->6--->7
  |         ^         ^
  +--->3---+----------+
  |                    |
  +--->4---------------+
  
  1--->2
  |
  +------------------->7
```

---

### Step 1: Calculate In-Degrees and find starting nodes

```
  +------+-----------+------------+
  | Node | In-Degree |Path Length  |
  +------+-----------+------------+
  |  0   |     0 [*]  |     0      |
  |  1   |     0 [*]  |     0      |
  |  2   |     2     |     0      |
  |  3   |     1     |     0      |
  |  4   |     1     |     0      |
  |  5   |     2     |     0      |
  |  6   |     1     |     0      |
  |  7   |     4     |     0      |
  +------+-----------+------------+
  
  Nodes 0 and 1 are STARTING POINTS (In-Degree = 0)
```

### Step 2: Process node 0 (path length = 0)

```
  Node 0 points to: 2, 3, 4
  
  For node 2: path = MAX(current 0, path_of_0 + 1) = MAX(0, 1) = 1
  For node 3: path = MAX(current 0, path_of_0 + 1) = MAX(0, 1) = 1
  For node 4: path = MAX(current 0, path_of_0 + 1) = MAX(0, 1) = 1

  +------+------------+
  | Node |Path Length  |
  +------+------------+
  |  0   | 0 ✅       |
  |  1   | 0          |
  |  2   | 1          |
  |  3   | 1          |
  |  4   | 1          |
  |  5   | 0          |
  |  6   | 0          |
  |  7   | 0          |
  +------+------------+
```

### Step 3: Process node 1 (path length = 0)

```
  Node 1 points to: 2, 7
  
  For node 2: path = MAX(current 1, path_of_1 + 1) = MAX(1, 1) = 1  (no change)
  For node 7: path = MAX(current 0, path_of_1 + 1) = MAX(0, 1) = 1

  Node 2's in-degree is now 0 > READY!
```

### Step 4: Process node 3 (path length = 1)

```
  Node 3 points to: 5, 7
  
  For node 5: path = MAX(current 0, 1 + 1) = MAX(0, 2) = 2
  For node 7: path = MAX(current 1, 1 + 1) = MAX(1, 2) = 2
```

### Step 5: Process node 4 (path length = 1)

```
  Node 4 points to: 7
  
  For node 7: path = MAX(current 2, 1 + 1) = MAX(2, 2) = 2  (no change)
```

### Step 6: Process node 2 (path length = 1)

```
  Node 2 points to: 5
  
  For node 5: path = MAX(current 2, 1 + 1) = MAX(2, 2) = 2  (no change)
  
  Node 5's in-degree is now 0 > READY!
```

### Step 7: Process node 5 (path length = 2)

```
  Node 5 points to: 6
  
  For node 6: path = MAX(current 0, 2 + 1) = MAX(0, 3) = 3
```

### Step 8: Process node 6 (path length = 3)

```
  Node 6 points to: 7
  
  For node 7: path = MAX(current 2, 3 + 1) = MAX(2, 4) = 4 ✅
```

### Step 9: Process node 7 (path length = 4)

```
  Node 7 has no outgoing edges. DONE!
```

---

## Final Results

```
  +------+------------+----------------------------------+
  | Node | Depth      | Longest Path To This Node        |
  +------+------------+----------------------------------+
  |  0   | 0          | Starting point                   |
  |  1   | 0          | Starting point                   |
  |  2   | 1          | 0 > 2   (or 1 > 2)              |
  |  3   | 1          | 0 > 3                            |
  |  4   | 1          | 0 > 4                            |
  |  5   | 2          | 0 > 3 > 5                       |
  |  6   | 3          | 0 > 3 > 5 > 6                   |
  |  7   | 4          | 0 > 3 > 5 > 6 > 7 < CRITICAL!  |
  +------+------------+----------------------------------+

  The CRITICAL PATH (longest): 0 > 3 > 5 > 6 > 7 (depth = 4)
```

### Visual of Depths:
```
  Depth 0:    0    1
              |    |
  Depth 1:    2    3    4
                   |
  Depth 2:         5
                   |
  Depth 3:         6
                   |
  Depth 4:         7     < The project's total "length"!
```

---

## Where is Longest Path Used?

| Use Case | How It Helps |
|---|---|
| **Critical Path Method (CPM)** | Finding the minimum time to finish a construction project |
| **Project Management** | Identifying which tasks will delay the whole project if delayed |
| **Game Tech Trees** | How deep is a technology tree in a strategy game? |
| **Compiler optimization** | Determining the longest chain of dependent operations |

---

## Key Takeaways

1. Combines **Topological Sort + Dynamic Programming**
2. The longest path determines the **minimum project completion time**
3. Uses the formula: `depth[neighbor] = MAX(depth[neighbor], depth[current] + 1)`
4. **MAX** ensures we always keep the **longest** path (not the shortest!)
5. A task on the critical path **cannot be delayed** without delaying the whole project
6. Only works on **DAGs** — no cycles allowed!
