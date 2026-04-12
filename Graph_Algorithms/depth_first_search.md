<!-- +--------------------------------------------------------------+ -->
<!-- |  DEPTH-FIRST SEARCH (DFS) — THE MAZE EXPLORER               | -->
<!-- +--------------------------------------------------------------+ -->
# Depth-First Search (DFS) — The Maze Explorer

## Theoretical Definition & Comparisons

**Theoretical Definition:** 
Depth-First Search (DFS) is a graph traversal algorithm that explores as deep as possible along a single branch before backtracking. It relies on a Stack (LIFO structure), usually implemented via system recursion.

**Comparison (Graph Traversals):**
*   **Depth-First Search (DFS):** Best for cycle detection, compiling topological sorts, solving puzzles (like mazes), and exploring all possibilities in decision trees.
*   **Breadth-First Search (BFS):** Explores layer-by-layer rather than deep-diving. Best for finding the absolute **shortest path** on unweighted graphs and analyzing level depths.

---

## What is DFS?

Imagine you're exploring a **dark maze**. You enter a tunnel and keep walking **as deep as possible** until you hit a dead end. Then you **turn back** (backtrack) to the last fork and try a different tunnel. You keep doing this until you've explored every part of the maze.

> **Simple Definition:** DFS starts at one point and **goes as deep as possible** down one path. When it hits a dead end, it **backtracks** and tries another path.

---

## Visual Representation

![DFS "Maze Explorer" Deep-First Diagram](docs/images/dfs_diagram.png)

> [!NOTE]
> **Teacher's Perspective:** "Imagine you're exploring a **pitch-black maze** with only a ball of string. You enter a tunnel and keep walking **as deep as possible** until you hit a dead end. Then, you follow your string **backtrack** to the last fork in the road and try a different tunnel. You keep doing this—diving deep, then coming back—until you've touched every wall of the maze. **DFS** is that brave explorer who always wants to see how far the rabbit hole goes before looking at anything else!"

---

## Step-by-Step Breakdown (Teacher's Guide)

Let's watch our explorer dive into a graph starting at Node **0**:

### 1. The Strategy (The Stack)
DFS is a "Go Deep First" strategy. It uses a **Stack** (Last-In, First-Out)—like a stack of heavy plates. You can only look at the plate on the very top. If you find a new path, you put a new plate on top and focus *only* on that until it's done.

### 2. The Deep Dive
- Start at Node 0. It has friends 1 and 2. 
- We pick **1** and dive in! (Node 2 is left waiting on the stack).
- From Node 1, we see friend 3. **Dive again!**
- From Node 3, we see friend 4. **Dive again!**
- Now at Node 4, there are no new friends. **Dead end!**

### 3. The Backtrack (The String)
- We "pop" Node 4 off our stack and go back to Node 3.
- Node 3 has no other friends. "Pop" it and go back to Node 1.
- Node 1 has no other friends. "Pop" it and go back to Node 0.
- **Wait!** Node 0 still has that friend **2** we ignored earlier. 
- **Dive into 2!**

---

---

## Steps to Perform (Visual Trace)

Let's watch our explorer dive deep from **Node 0**.

### 1. The Initial Choice
Explorer starts at 0. Neighbors are 1 and 2. We pick 1.
- **Stack:** `[0, 1]`
```text
  [0]* <-- Start
  / \
(1) (2)
 |
(3)
```

### 2. The Deep Dive
From 1, explorer dives into 3.
- **Stack:** `[0, 1, 3]`
```text
  (0)
  / \
 [1] (2)
  |
 [3]* <-- Deepest point
```

### 3. The Dead End
Node 3 has no more unvisited neighbors.
- **Backtrack!** We return to Node 1.
- Node 1 has no more neighbors. Return to Node 0.
- **Stack:** `[0]`
```text
  (0) <-- Back at base
  / \
 (1) (2)
  |
 (3) (Visited)
```

### 4. Exploring the Other Branch
Node 0 still has neighbor 2. **Dive into 2!**
- **Stack:** `[0, 2]`
```text
  (0)
  / \
 (1)[2]* <-- Exploring new path
  |
 (3)
```

---

## Why does DFS "backtrack"?
Because DFS doesn't want to miss anything! Backtracking is how it says, "Okay, I've seen everything down *this* tunnel, now let me go back and check the other one I saw earlier." It's perfect for things like **solving puzzles** or **detecting if a road leads back in a circle (cycles)**.

---


---

## Iterative vs Recursive DFS

| Feature | Iterative (Manual Stack) | Recursive (Elegant) |
|---|---|---|
| **What remembers the path?** | A manual Stack object | The computer's call stack |
| **Easier to understand?** | Maybe — you can see the stack | Yes — very clean code |
| **Risk of crashing?** | No | Yes — for very deep graphs (stack overflow) |
| **Tracks parent path?** | Need extra code | Naturally built-in |

---

## Where is DFS Used?

| Use Case | How DFS Helps |
|---|---|
| **Solving Mazes** | Go deep down one path, backtrack when stuck |
| **Detecting Cycles** | If you visit a node you've already seen, there's a cycle! |
| **Topological Sorting** | Used to order tasks based on dependencies |
| **Finding connected parts** | Discover all nodes reachable from a starting point |

---

## Key Takeaways

1. DFS uses a **Stack** (Last-In, First-Out) — or recursion
2. It explores **as deep as possible** before backtracking
3. It does **NOT** guarantee the shortest path (unlike BFS)
4. It's great for **mazes, cycles, and topological sorting**
5. **Iterative** = manual stack, **Recursive** = function calls itself
6. DFS visits nodes like exploring a cave — go deep, then come back and try another tunnel!

