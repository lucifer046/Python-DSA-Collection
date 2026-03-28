<!-- +--------------------------------------------------------------+ -->
<!-- |  DEPTH-FIRST SEARCH (DFS) — THE MAZE EXPLORER               | -->
<!-- +--------------------------------------------------------------+ -->
# Depth-First Search (DFS) — The Maze Explorer

## What is DFS?

Imagine you're exploring a **dark maze**. You enter a tunnel and keep walking **as deep as possible** until you hit a dead end. Then you **turn back** (backtrack) to the last fork and try a different tunnel. You keep doing this until you've explored every part of the maze.

> **Simple Definition:** DFS starts at one point and **goes as deep as possible** down one path. When it hits a dead end, it **backtracks** and tries another path.

---

## BFS vs DFS at a Glance

```
  BFS (Breadth-First):                DFS (Depth-First):
  Explores WIDE first                 Explores DEEP first
  
       0                                   0
      / \                                  |
     1   2    < Layer by Layer             1
    / \ / \                                |
   3   4        Visit: 0,1,2,3,4           3
                                           |
                                           4
                                           (then backtrack and try 2)
                                          Visit: 0,1,3,4,2
```

---

## DFS Traversal — Step by Step

### The Graph:
```
       0 ------- 1
       |        ╱ |
       |      ╱   |
       2          |
       |          |
       3 ------- 4

  Adjacency List:
  0: [1, 2]
  1: [3, 4]
  2: [4, 3]
  3: [4]
  4: []
```

### Starting Node: **0**

**DFS uses a STACK (Last-In, First-Out)** — like a stack of plates!

---

### Step 1: Start at node 0, push it on the stack

```
  Stack:   [0]    < Push 0
  Visited: {}

       ★0 ------- 1
       |        ╱ |
       2          |
       |          |
       3 ------- 4

  ★ = Next to process
```

### Step 2: Pop 0, visit it. Push its neighbors (1, 2)

```
  Stack:   [2, 1]    < Pushed 1 and 2 (1 is on top!)
  Visited: {0}

       ✅0 ------- ★1
       |        ╱   |
       ★2          |
       |            |
       3 ------- 4
```

### Step 3: Pop 1 (top of stack), visit it. Push its unvisited neighbors (3, 4)

```
  Stack:   [2, 4, 3]    < Pushed 3 and 4 (3 is on top!)
  Visited: {0, 1}

       ✅0 ------- ✅1
       |        ╱    |
       ★2           |
       |             |
       ★3 ------- ★4
```

### Step 4: Pop 3 (top), visit it. Push its unvisited neighbor (4)

```
  Stack:   [2, 4, 4]    < Pushed 4 (already in stack, but that's ok)
  Visited: {0, 1, 3}

       ✅0 ------- ✅1
       |                |
       ★2               |
       |                |
       ✅3 ------- ★4
```

### Step 5: Pop 4 (top), visit it. No unvisited neighbors.

```
  Stack:   [2, 4]
  Visited: {0, 1, 3, 4}

       ✅0 ------- ✅1
       |                |
       ★2               |
       |                |
       ✅3 ------- ✅4
```

### Step 6: Pop 4 again — already visited! Skip. Pop 2, visit it.

```
  Stack:   []    < EMPTY!
  Visited: {0, 1, 3, 4, 2}

       ✅0 ------- ✅1
       |                |
       ✅2              |
       |                |
       ✅3 ------- ✅4

  DFS Order: 0 > 1 > 3 > 4 > 2
```

---

## DFS Path Visualization (Recursive Version)

The recursive version uses the computer's built-in "call stack" — it's more elegant!

```
  Start: 0
    |
    +--> Visit 0, then go deeper into neighbor 1
    |      |
    |      +--> Visit 1, then go deeper into neighbor 3
    |      |      |
    |      |      +--> Visit 3, then go deeper into neighbor 4
    |      |      |      |
    |      |      |      +--> Visit 4 (no unvisited neighbors)
    |      |      |           BACKTRACK! <--
    |      |      |
    |      |      +--> Neighbor 4? Already visited. BACKTRACK! <--
    |      |
    |      +--> Neighbor 4? Already visited. BACKTRACK! <--
    |
    +--> Go deeper into neighbor 2
           |
           +--> Visit 2, neighbor 4? Already visited.
           |      neighbor 3? Already visited.
           +--> BACKTRACK! <--

  ALL DONE! ✅
  
  DFS Order: 0 > 1 > 3 > 4 > 2
  Parent tree: {1: 0, 3: 1, 4: 3, 2: 0}
```

### The Parent Tree:
```
  "Who discovered whom?"

       0           < Root (discovered itself)
      / \
     1   2         < 0 discovered both 1 and 2
     |
     3             < 1 discovered 3
     |
     4             < 3 discovered 4
```

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
