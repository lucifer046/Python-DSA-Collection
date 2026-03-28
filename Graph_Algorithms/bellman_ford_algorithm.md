<!-- +----------------------------------------------------------+ -->
<!-- |  BELLMAN-FORD — THE NEGATIVE WEIGHT SPECIALIST           | -->
<!-- +----------------------------------------------------------+ -->
# Bellman-Ford Algorithm — The Negative Weight Specialist

## What is Bellman-Ford?

Remember Dijkstra's Algorithm? It finds the shortest path, but it **panics** if any road has a **negative weight** (like a road that *pays you* to drive on it!).

**Bellman-Ford** is the slower but **smarter** brother. It CAN handle negative weights AND it can **detect infinite money loops** (negative cycles)!

> **Simple Definition:** Bellman-Ford finds the shortest path to all nodes by repeatedly checking every edge. It works even with negative weights and can detect negative cycles.

---

## Understanding Negative Weights

```
  Normal Graph (Positive):           Game-like Graph (Has Negatives):
  
    A --(5)--> B                       A --(5)--> B
       Energy cost: 5                     Energy cost: 5
                                       
    C --(3)--> D                       C --(-3)--> D
       Energy cost: 3                     Energy BONUS: +3! 🎁
```

In real life, a negative weight could mean:
- A road where you get **paid** to drive
- A game square that **gives you** energy instead of taking it

---

## Step-by-Step Example

### The Graph (Edge List):

```
          (4)           (5)
    [0] -------> [1] ----------> [3]
     |          /  |             |
    (2)      (1)  (5)           (2)
     v      v      |             v
    [2] ---------> [3] --------> [4]
     |     (8)                   ^
     +-----------(10)------------+

  Edge List:
  (0>1, cost 4), (0>2, cost 2), (1>2, cost 1)
  (1>3, cost 5), (2>3, cost 8), (2>4, cost 10), (3>4, cost 2)
```

### Starting Node: 0, Total Nodes: 5

---

### INITIALIZATION: Everything starts at infinity

```
  +------+----------+
  | Node | Distance |
  +------+----------+
  |  0   |    0     |  < Start
  |  1   |    ∞     |
  |  2   |    ∞     |
  |  3   |    ∞     |
  |  4   |    ∞     |
  +------+----------+
```

### ITERATION 1 (of n-1 = 4 iterations): Check ALL edges

```
  Check edge (0>1, cost 4):  dist[0] + 4 = 0 + 4 = 4  < ∞   > UPDATE dist[1] = 4 ✅
  Check edge (0>2, cost 2):  dist[0] + 2 = 0 + 2 = 2  < ∞   > UPDATE dist[2] = 2 ✅
  Check edge (1>2, cost 1):  dist[1] + 1 = 4 + 1 = 5  > 2   > No change
  Check edge (1>3, cost 5):  dist[1] + 5 = 4 + 5 = 9  < ∞   > UPDATE dist[3] = 9 ✅
  Check edge (2>3, cost 8):  dist[2] + 8 = 2 + 8 = 10 > 9   > No change
  Check edge (2>4, cost 10): dist[2] + 10= 2 + 10= 12 < ∞   > UPDATE dist[4] = 12 ✅
  Check edge (3>4, cost 2):  dist[3] + 2 = 9 + 2 = 11 < 12  > UPDATE dist[4] = 11 ✅

  +------+----------+
  | Node | Distance |
  +------+----------+
  |  0   |    0     |
  |  1   |    4     |
  |  2   |    2     |
  |  3   |    9     |
  |  4   |   11     |
  +------+----------+
```

### ITERATION 2: Check ALL edges again

```
  Check edge (0>1, cost 4):  0 + 4 = 4  = 4   > No change
  Check edge (0>2, cost 2):  0 + 2 = 2  = 2   > No change
  Check edge (1>2, cost 1):  4 + 1 = 5  > 2   > No change
  Check edge (1>3, cost 5):  4 + 5 = 9  = 9   > No change
  Check edge (2>3, cost 8):  2 + 8 = 10 > 9   > No change
  Check edge (2>4, cost 10): 2 + 10= 12 > 11  > No change
  Check edge (3>4, cost 2):  9 + 2 = 11 = 11  > No change

  No changes! Algorithm has converged. ✅
  (We still run remaining iterations as a formality)
```

### FINAL DISTANCES:
```
  +------+----------+--------------------------+
  | Node | Distance | Shortest Path             |
  +------+----------+--------------------------+
  |  0   |    0     | Start                     |
  |  1   |    4     | 0 > 1                     |
  |  2   |    2     | 0 > 2                     |
  |  3   |    9     | 0 > 1 > 3                |
  |  4   |   11     | 0 > 1 > 3 > 4           |
  +------+----------+--------------------------+
```

---

## Negative Cycle Detection

After finishing all (n-1) iterations, Bellman-Ford does **one final check**: Can we *still* relax any edge?

- If **YES** > There's a **negative cycle** (infinite loop that keeps getting cheaper!)
- If **NO** > The distances are correct

### What's a Negative Cycle?

```
  A --(2)--> B
  ^          |
  |         (1)
  |          v
  +--(-5)-- C

  Going A > B > C > A costs: 2 + 1 + (-5) = -2
  Every time we go around the loop, we SAVE 2!
  We could go around forever and the cost would keep decreasing!
  
  This means there is NO shortest path — it would be negative infinity!
```

---

## Dijkstra vs Bellman-Ford

| Feature | Dijkstra | Bellman-Ford |
|---|---|---|
| **Speed** | O((V+E) log V) — Fast | O(V × E) — Slower |
| **Negative weights?** | ❌ Cannot handle | ✅ Works perfectly |
| **Negative cycle detection?** | ❌ No | ✅ Yes! |
| **Strategy** | Greedy (pick cheapest) | Brute force (check all edges repeatedly) |

---

## Where is Bellman-Ford Used?

| Use Case | How It Helps |
|---|---|
| **Financial Arbitrage** | Finding currency exchange loops that make profit (negative cycle!) |
| **Internet Routing (RIP)** | Routers use distance-vector protocol based on Bellman-Ford |
| **Games** | Finding paths where some tiles give bonuses (negative weights) |

---

## Key Takeaways

1. Bellman-Ford relaxes **ALL edges**, repeated **(n-1) times**
2. It works with **negative edge weights** (unlike Dijkstra!)
3. It can **detect negative cycles** — infinite loops with decreasing cost
4. It's **slower** than Dijkstra but more **versatile**
5. Why n-1 times? Because the longest simple path has at most n-1 edges
