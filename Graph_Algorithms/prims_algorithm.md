<!-- +------------------------------------------------------+ -->
<!-- |  PRIM'S ALGORITHM — THE GREEDY TREE BUILDER          | -->
<!-- +------------------------------------------------------+ -->
# Prim's Algorithm — The Greedy Tree Builder

## What is Prim's Algorithm?

Imagine you're the **mayor of a town** and you need to build **water pipelines** to connect ALL houses. Each pipe costs money based on distance. You want to **connect everyone** while spending the **least total money**.

> **Simple Definition:** Prim's Algorithm finds the **Minimum Spanning Tree (MST)** — the cheapest way to connect ALL nodes in a graph using the least total edge weight, without creating any loops.

---

## What is a Minimum Spanning Tree (MST)?

A tree that:
- **MINIMUM** — Cheapest total cost
- **SPANNING** — Reaches every single node
- **TREE** — No cycles (no loops)

```
  ORIGINAL GRAPH:                    MST (Cheapest connections):
  
       2        8                         2
  0-------1-------3                  0-------1        3
  |       |      ╱|                          |       |
  | 6     |3   7  |1                         |3      |1
  |       | ╱     |                          |       |
  3-------2-------4                  3       2       4
       5

  Total edges: 7                     Total edges: 4 (n-1)
  Total cost: 2+8+6+3+7+5+1 = 32    Total cost: 2+3+1+... = MINIMUM!
```

---

## Step-by-Step Example

### The Graph:

```
  Node 0: > 1(cost 2), > 3(cost 6)
  Node 1: > 0(cost 2), > 2(cost 3), > 3(cost 8), > 4(cost 5)
  Node 2: > 1(cost 3), > 3(cost 7)
  Node 3: > 0(cost 6), > 1(cost 8), > 2(cost 7), > 4(cost 1)
  Node 4: > 1(cost 5), > 3(cost 1)
```

---

### Step 1: Start with Node 0 (the seed 🌱)

```
  In MST: {0}
  Not yet: {1, 2, 3, 4}
  
  Available edges from MST to outside:
  • 0 > 1, cost 2  < CHEAPEST! ⭐
  • 0 > 3, cost 6

  Pick: Edge 0>1 (cost 2)
  
       ●0-------●1        3
       |                  |
       | 6                |1
       |                  |
       3        2        4

  MST cost so far: 2
```

### Step 2: Add Node 1

```
  In MST: {0, 1}
  Not yet: {2, 3, 4}
  
  Available edges from MST to outside:
  • 0 > 3, cost 6
  • 1 > 2, cost 3  < CHEAPEST! [*]
  • 1 > 3, cost 8
  • 1 > 4, cost 5

  Pick: Edge 1>2 (cost 3)
  
       ●0-------●1        3
                 |        |
                 | 3      |1
                 |        |
       3        ●2        4

  MST cost so far: 2 + 3 = 5
```

### Step 3: Add Node 2

```
  In MST: {0, 1, 2}
  Not yet: {3, 4}
  
  Available edges from MST to outside:
  • 0 > 3, cost 6
  • 1 > 3, cost 8
  • 1 > 4, cost 5
  • 2 > 3, cost 7

  Pick: Edge 1>4 (cost 5)... Wait, let me check ALL options:
  Cheapest = 1 > 4, cost 5 [*]
  
       ●0-------●1        3
                 |╲       |
                 |  ╲5    |1
                 |   ╲    |
       3        ●2   ●4

  MST cost so far: 2 + 3 + 5 = 10
```

### Step 4: Add Node 4

```
  In MST: {0, 1, 2, 4}
  Not yet: {3}
  
  Available edges from MST to outside:
  • 0 > 3, cost 6
  • 1 > 3, cost 8
  • 2 > 3, cost 7
  • 4 > 3, cost 1  < CHEAPEST! [*]

  Pick: Edge 4>3 (cost 1)
  
       ●0-------●1        ●3
                 |╲       |
                 |  ╲5    |1
                 |   ╲    |
                ●2   ●4--+

  MST cost so far: 2 + 3 + 5 + 1 = 11
```

### DONE! All nodes connected! ✅

```
  FINAL MST:                        +--------------+
                                    | SELECTED EDGES|
       0-------1                    | 0-1 (cost 2)  |
               |╲                   | 1-2 (cost 3)  |
               |  ╲                 | 1-4 (cost 5)  |
               |   ╲                | 4-3 (cost 1)  |
              2    4---3            |               |
                                    | TOTAL: $11    |
                                    +--------------+
```

---

## Prim's Growth Animation

```
  Step 1:    {0}                -->  Connect cheapest neighbor
  Step 2:    {0, 1}             -->  Connect cheapest neighbor
  Step 3:    {0, 1, 2}          -->  Connect cheapest neighbor
  Step 4:    {0, 1, 2, 4}       -->  Connect cheapest neighbor
  Step 5:    {0, 1, 2, 4, 3}    -->  ALL CONNECTED! ✅

  MST grows like a plant — starting from a seed and reaching outward!
```

---

## Where is Prim's Used?

| Use Case | How It Helps |
|---|---|
| **Laying cables/pipes** | Connect all buildings with minimum cable length |
| **Computer networks** | Connect all routers with minimum fiber optic |
| **Electricity grids** | Connect all houses with minimum power lines |
| **Telephone networks** | Connect all towers with minimum wiring cost |

---

## Key Takeaways

1. Prim's **grows from a seed node** outward
2. At each step, it picks the **cheapest edge** connecting the MST to an outside node
3. It's **Greedy** — always picks the locally cheapest option
4. The result has exactly **n-1 edges** (for n nodes)
5. Total cost is the **minimum possible** to connect all nodes without cycles
