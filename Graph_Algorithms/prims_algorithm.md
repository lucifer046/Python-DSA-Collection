<!-- +------------------------------------------------------+ -->
<!-- |  PRIM'S ALGORITHM — THE GREEDY TREE BUILDER          | -->
<!-- +------------------------------------------------------+ -->
# Prim's Algorithm — The Greedy Tree Builder

## What is Prim's Algorithm?

Imagine you're the **mayor of a town** and you need to build **water pipelines** to connect ALL houses. Each pipe costs money based on distance. You want to **connect everyone** while spending the **least total money**.

> **Simple Definition:** Prim's Algorithm finds the **Minimum Spanning Tree (MST)** — the cheapest way to connect ALL nodes in a graph using the least total edge weight, without creating any loops.

---

## 🖼️ Visual Representation

![Prim's MST "Growing Seed" Diagram](docs/images/prim_diagram.png)

> [!NOTE]
> **Teacher's Perspective:** "Imagine you're the **Mayor of a small town** 🏛️ and you need to connect all the houses with water pipes. Each pipe costs money based on how long it is. You want to **connect everyone** while spending the **least total money**. **Prim's Algorithm** is like planting a seed: You start at one house (the seed), and then you look for the absolute cheapest pipe that connects a new house to your existing network. You keep 'growing' your network, one cheap pipe at a time, until every single house in town has water!"

---

## 🎓 Step-by-Step Breakdown (Teacher's Guide)

Let's watch our network grow from a single house (Node 0):

### 1. Plant the Seed (Node 0)
We pick Node 0 as our starting point. We look at all the pipes leading out of it.
- Pipe to Node 1 costs $2.
- Pipe to Node 3 costs $6.
- **The Rule:** We *always* pick the cheapest one that connects to a new house. So, we build the **$2 pipe to Node 1**.

### 2. Expanding the Network
Now we have two houses (0 and 1) in our network. We look at ALL the pipes leading from either of them to houses we haven't visited yet.
- From 1, we see a pipe to 2 for $3.
- From 1, we see a pipe to 4 for $5.
- From 0, we still have that $6 pipe to 3.
- **The Winner:** The **$3 pipe to Node 2** is the cheapest! We add it to our network.

### 3. Reaching Every House
We keep repeating this—checking the "fringe" of our network for the cheapest possible expansion—until every house is connected. By always taking the shortest leap, we ensure the total cost of all pipes combined is the lowest possible!

---

## 🧠 Prim's vs. Kruskal's: What's the difference?
While both find the exact same "Minimum Spanning Tree," they have different styles. **Prim's** grows like a **plant** 🌱 from a single seed, always staying connected. **Kruskal's** builds **bridges** 🏝️ all over the ocean at once and merges them later. Both are smart, just different!

---


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

