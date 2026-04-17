<!-- +------------------------------------------------------+ -->
<!-- |  UNIQUE GRID PATHS — THE ROBOT'S JOURNEY             | -->
<!-- +------------------------------------------------------+ -->

# Unique Grid Paths — The Robot's Journey

## Theoretical Definition & Comparisons

**Theoretical Definition:** 
Unique Grid Paths is a 2D dynamic programming problem that calculates the number of ways to travel from $(0,0)$ to $(m,n)$ on a grid, moving only Right or Down. Each cell's value is the sum of the cell above it and the cell to its left.

**Context & Comparison:**
*   **Pascal's Triangle:** This grid is a transformed version of Pascal's Triangle.
*   **Combinatorics:** Can be solved using combinations: $\binom{m+n-2}{m-1}$.

---


## The Scenario

Imagine a **robot** starting at the top-left corner of a grid. Its mission is to reach the bottom-right corner. However, this robot has very limited movement circuits: it can **only move Right or Down**.

> **Goal:** How many different, unique paths can the robot take to reach its destination?

---

![Unique Grid Path "Robot Journey" Diagram](docs/images/grid_paths_diagram.png)

## 1. The Dynamic Discovery

Think about any square in the middle of the grid. How could the robot have gotten there?
- It could have come from the square directly **Above** it.
- It could have come from the square directly to its **Left**.

**The Mathematical Key:**
The number of ways to reach a square is simply the **Sum** of the ways to reach its neighbors.

$$Paths(r, c) = Paths(r-1, c) + Paths(r, c-1)$$

---

## 2. Visualizing the Grid (Tabulation)

Let's look at a $3 \times 3$ grid:

### Step 1: The Boundaries
There is only one way to stay on the top edge or the left edge (move in a straight line). We fill them with `1`.

```text
    1  1  1
    1  .  .
    1  .  .
```

### Step 2: Filling the Inner Grid
For every empty square, we add the number from the top and the number from the left.

```text
    1   1   1
    1   2   3  (1+1=2, 2+1=3)
    1   3   6  (1+2=3, 3+3=6)
```

**Result:** In a $3 \times 3$ grid, there are **6 unique paths**!

---

## 3. Space Optimization (The "Row Slide")

Do we need to store the whole grid in memory?
- To calculate the next cell in a row, we only need the value above it (from the **Previous Row**) and the value to its left (the **cell we just calculated**).
- We can just use a **single array** and keep updating it as we move down the rows. This saves a massive amount of memory for large grids!

---

## 4. Summary Table

| Approach | Logic | Complexity |
| :--- | :--- | :--- |
| **Recursion** | Bruteforce exploration of every step. | $O(2^{m+n})$ - Terrible! |
| **Memoization** | Save paths for every (r, c) coordinate. | $O(m \times n)$ - Linear! |
| **Tabulation** | Build the grid row by row. | $O(m \times n)$ - Fast! |
| **Optimized** | Same as tabulation, but only keep one row. | $O(min(m, n))$ **Space!** |

> [!TIP]
> **Teacher's Perspective:** "The Grid Path problem is beautiful because it shows how **Pascal's Triangle** is hidden everywhere! If you tilt the grid 45 degrees, you'll see the numbers growing exactly like the famous triangle. It's a perfect example of how complex counting problems become trivial when you solve them by building on previous answers."
