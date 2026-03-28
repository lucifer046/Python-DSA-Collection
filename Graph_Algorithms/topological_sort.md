<!-- +---------------------------------------------+ -->
<!-- |  TOPOLOGICAL SORT — THE TASK SCHEDULER       | -->
<!-- +---------------------------------------------+ -->
# Topological Sort — The Task Scheduler

## What is Topological Sort?

Imagine you're **getting dressed** in the morning. You can't put on **shoes before socks**, and you can't put on a **shirt before undershirt**. Some tasks MUST happen before others!

**Topological Sort** finds a **legal order** to complete all tasks so that every task starts AFTER its prerequisites are done.

> **Simple Definition:** Given tasks with dependencies (Task A must finish before Task B can start), Topological Sort finds a valid order to complete all tasks.

> ⚠️ **Requirement:** The graph must be a **DAG** (Directed Acyclic Graph) — no circular dependencies allowed!

---

## Example: The Task Dependency Graph

```
  Tasks: 0, 1, 2, 3, 4, 5, 6, 7

  Dependencies (arrows mean "must come before"):
  0 > 2, 3, 4
  1 > 2, 7
  2 > 5
  3 > 5, 7
  4 > 7
  5 > 6
  6 > 7

  Visual Graph:
  
  0----->2----->5----->6----->7
  |       ^              ^     ^
  +-->3--+--------------+     |
  |   |                        |
  +-->4------------------------+
       ^
  1--->2
  |
  +--------------------------->7
```

---

## The "In-Degree" Concept

**In-Degree** = How many arrows point **INTO** a node = How many prerequisites it has.

```
  +------+-----------+----------------------+
  | Node | In-Degree | Meaning               |
  +------+-----------+----------------------+
  |  0   |     0     | No prerequisites! [*]  |
  |  1   |     0     | No prerequisites! [*]  |
  |  2   |     2     | Needs 0 and 1 first   |
  |  3   |     1     | Needs 0 first          |
  |  4   |     1     | Needs 0 first          |
  |  5   |     2     | Needs 2 and 3 first   |
  |  6   |     1     | Needs 5 first          |
  |  7   |     4     | Needs 1,3,4,6 first   |
  +------+-----------+----------------------+

  Rule: A task is READY when its In-Degree becomes 0!
```

---

## Kahn's Algorithm — Step by Step

### Step 1: Find all tasks with In-Degree 0 (no prerequisites)

```
  Ready Queue: [0, 1]   < These can start immediately!
  
  Tasks 0 and 1 have NO prerequisites.
```

### Step 2: Process task 0

```
  Remove task 0 from queue > Add to result.
  Result: [0]
  
  Task 0 was a prerequisite for: 2, 3, 4
  Reduce their in-degrees by 1:

  +------+-----------+
  | Node | In-Degree |
  +------+-----------+
  |  2   | 2>1       |
  |  3   | 1>0 [*]    |  < NOW READY!
  |  4   | 1>0 [*]    |  < NOW READY!
  +------+-----------+
  
  Ready Queue: [1, 3, 4]
```

### Step 3: Process task 1

```
  Result: [0, 1]
  
  Task 1 was a prerequisite for: 2, 7
  
  +------+-----------+
  | Node | In-Degree |
  +------+-----------+
  |  2   | 1>0 [*]    |  < NOW READY!
  |  7   | 4>3       |
  +------+-----------+
  
  Ready Queue: [3, 4, 2]
```

### Step 4: Process task 3

```
  Result: [0, 1, 3]
  
  Task 3 was a prerequisite for: 5, 7
  
  +------+-----------+
  |  5   | 2>1       |
  |  7   | 3>2       |
  +------+-----------+
  
  Ready Queue: [4, 2]
```

### Step 5: Process task 4

```
  Result: [0, 1, 3, 4]
  
  Task 4 was a prerequisite for: 7
  
  +------+-----------+
  |  7   | 2>1       |
  +------+-----------+
  
  Ready Queue: [2]
```

### Step 6: Process task 2

```
  Result: [0, 1, 3, 4, 2]
  
  Task 2 was a prerequisite for: 5
  
  +------+-----------+
  |  5   | 1>0 ⭐    |  < NOW READY!
  +------+-----------+
  
  Ready Queue: [5]
```

### Step 7: Process task 5

```
  Result: [0, 1, 3, 4, 2, 5]
  
  Task 5 was a prerequisite for: 6
  
  +------+-----------+
  |  6   | 1>0 ⭐    |  < NOW READY!
  +------+-----------+
  
  Ready Queue: [6]
```

### Step 8: Process task 6

```
  Result: [0, 1, 3, 4, 2, 5, 6]
  
  Task 6 was a prerequisite for: 7
  
  +------+-----------+
  |  7   | 1>0 ⭐    |  < NOW READY!
  +------+-----------+
  
  Ready Queue: [7]
```

### Step 9: Process task 7

```
  Result: [0, 1, 3, 4, 2, 5, 6, 7]   < FINAL ORDER! ✅
  
  Ready Queue: [] < Empty! ALL DONE!
```

---

## 📐 The Final Valid Order

```
  0 > 1 > 3 > 4 > 2 > 5 > 6 > 7

  Verification:
  ✅ 0 before 2, 3, 4     (0's dependencies)
  ✅ 1 before 2, 7         (1's dependencies)
  ✅ 2 before 5             (2's dependency)
  ✅ 3 before 5, 7          (3's dependencies)
  ✅ 4 before 7             (4's dependency)
  ✅ 5 before 6             (5's dependency)
  ✅ 6 before 7             (6's dependency)
  
  ALL DEPENDENCIES SATISFIED! ✅
```

---

## Real-Life Examples

### Getting Dressed:
```
  Socks > Shoes
  Underwear > Pants > Shoes
  Shirt > Jacket

  Valid order: Underwear, Socks, Shirt, Pants, Jacket, Shoes ✅
  Invalid:    Shoes, Socks ❌ (Can't put shoes before socks!)
```

### University Course Planning:
```
  Math 101 > Math 201 > Math 301
  CS 101 > CS 201
  Math 101 > CS 201

  Valid: Math 101, CS 101, Math 201, CS 201, Math 301 ✅
```

---

## Key Takeaways

1. Topological Sort finds a **valid ordering** of tasks with dependencies
2. It only works on **DAGs** (Directed Acyclic Graphs) — no circular dependencies!
3. **In-Degree** = number of prerequisites a task has
4. Tasks are **ready** when their In-Degree drops to **0**
5. There may be **multiple valid orderings** — all are correct!
6. Used in **course planning, build systems, project management**
