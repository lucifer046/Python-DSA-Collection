<!-- +------------------------------------------------------+ -->
<!-- |      FLOYD-WARSHALL — ALL-PAIRS SHORTEST PATH        | -->
<!-- +------------------------------------------------------+ -->

# Floyd-Warshall — All-Pairs Shortest Path

## What is Floyd-Warshall?

Imagine you are an **airline logistics manager**. You need a **master table** that shows the shortest flying path between EVERY combination of cities in the world (e.g., London to Tokyo, Paris to New York, Sydney to Dubai).

> **Simple Definition:** Floyd-Warshall finds the **absolute shortest distance** between **every possible pair** of nodes in a graph at once!

Unlike Dijkstra's (which starts at ONE node), Floyd-Warshall finds the answers for **everyone**!

![Floyd-Warshall "All-Pairs Shortest Path" Diagram](docs/images/floyd_warshall_diagram.png)

> [!NOTE]
> **Teacher's Perspective:** "Imagine you are an **Airline Logistics Manager** . You don't just need the shortest path from one city to another; you need a **Master Master-Table** that shows the quickest route between _every single_ pair of cities in the world! Floyd-Warshall is the grandmaster of this task. It looks at every node and asks a simple question: 'Is it faster to go directly from A to C, or is there a **B** somewhere in the middle that provides a better shortcut?' By checking every possible middle-man, it builds the ultimate travel guide for your entire network!"

---

## Step-by-Step Breakdown (Teacher's Guide)

Let's see how our Master Table evolves:

### 1. The Starting Grid (Adjacency Matrix)

We start with a simple grid. If two cities have a direct road, we write down the cost. If they don't, we write "Infinity" (∞) because we haven't found a path yet.

### 2. The Layover Test (Iteration)

We pick one city at a time (let's call it B) to act as a "Layover City." We then check every pair of cities (A and C) to see if stopping at B saves time.

**The Recurrence Formula:**
$$SP^k[i, j] = \min(SP^{k-1}[i, j], SP^{k-1}[i, k] + SP^{k-1}[k, j])$$
Where $k$ is the intermediate node being considered.

- **The logic:** `A to C = Minimum of (Current A to C, OR A to B + B to C)`
- If stopping at B is cheaper, we update our Master Table with the new, shorter cost!

### 3. Shortest Path for Everyone!

We repeat this for _every_ city in the graph. In the end, our grid is transformed from a list of direct roads into a complete map of the most efficient shortcuts possible. No matter where you start or end, you'll have the best answer!

---

## Why is it a "Grand Master Plan"?

While algorithms like Dijkstra are fast for one-to-all travel, Floyd-Warshall is the only one that gives you **All-to-All** answers in one go. It's slower ($O(V^3)$), but it's incredibly thorough and can even handle those tricky negative-weight roads that Dijkstra hates!

---

---

## Comparing Algorithms

| Feature        | Dijkstra               | Bellman-Ford              | Floyd-Warshall             |
| :------------- | :--------------------- | :------------------------ | :------------------------- |
| **Goal**       | One node to all others | One node to all others    | **ALL nodes to ALL nodes** |
| **Complexity** | $O(E \log V)$          | $O(VE)$                   | $O(V^3)$                   |
| **Negatives?** | No ❌                  | Yes ✅                    | Yes ✅                     |
| **Best For**   | Daily GPS/Navigation   | Detecting negative cycles | Large offline path tables  |

---

## Key Takeaways

1. **All-to-All:** A single run gives the distance matrix for the entire graph.
2. **Logic:** $dist(i,j) = \min(dist(i,j), dist(i,k) + dist(k,j))$.
3. **The Golden Rule (Negatives):** 
   - **Negative Weights?** YES ✅! It handles negative paths perfectly.
   - **Negative Cycles?** NO ❌. It cannot provide a valid answer if the graph contains a negative total cycle.
4. **Performance:** $O(V^3)$ is slow for large graphs, so use it when the number of nodes is small (usually less than 500).
5. **Real-Life Use:** Transitive closure (finding "who knows whom"), network routing, and project scheduling.
