<!-- +------------------------------------------------------+ -->
<!-- |  DYNAMIC PROGRAMMING — SOLVING BY SAVING RESULTS     | -->
<!-- +------------------------------------------------------+ -->

# Dynamic Programming — solving Problems by Saving Results

## What is Dynamic Programming (DP)?

Imagine a teacher asks a student: _"What is 1 + 1 + 1 + 1 + 1?"_
The student counts on their fingers and says: **"5!"**

Now the teacher asks: _"What is 1 + 1 + 1 + 1 + 1 + 1?"_
Instead of counting from scratch, the student immediately says: **"6!"**

**Teacher:** _"How did you know so fast?"_
**Student:** _"I just added 1 to the '5' I already remembered!"_

> **Simple Definition:** Dynamic Programming is just **Recursion with a Memory**. Instead of recalculating the same answer over and over, we solve a small problem **ONCE**, save the result, and look it up later.

---

## Two Main Ingredients for DP

For a problem to be solved using DP, it must have:

1.  **Overlapping Subproblems:** You find yourself solving the _exact same_ smaller problem many times.
2.  **Optimal Substructure:** The big answer can be built perfectly using the answers to the smaller pieces.

---

## 1. The Problem: Standard Recursion (The "Forgetful" Method)

In standard recursion, the computer is like a goldfish—it forgets everything it just did.

### ASCII Recursion Tree for Fibonacci(5)

Look at how many times we calculate `fib(2)` and `fib(1)`!

```text
                                     fib(5)
                                    /      \
                                   /        \
                     fib(4)                        fib(3)
                    /      \                      /      \
                   /        \                    /        \
            fib(3)            fib(2)          fib(2)       [fib(1)]
           /      \          /      \        /      \
          /        \        /        \      /        \
       fib(2)    fib(1)    [f1]    [f0]    [f1]    [f0]
      /      \
     /        \
   [f1]     [f0]

[ ] = Recalculating the same thing again!
```

**Complexity:** $O(2^n)$ — This grows **exponentially**. If $n=50$, your computer might take years to finish!

---

## 2. Memoization — Top-Down (The "Note-Taking" Method)

**Memoization** is like recursion, but we keep a **Notebook** (Dictionary/Array).
Before calculating `fib(n)`, we check the notebook:

1. Is the answer already there? **Use it!**
2. If not: Calculate it, **write it in the notebook**, and then return it.

> **Direction:** We start at the **TOP** (the big problem) and break it down to the **BOTTOM** (base cases).

**Complexity:** $O(n)$ — High speed, but uses some extra memory for the "notebook" and the function call stack.

---

## 3. Tabulation — Bottom-Up (The "Building-Block" Method)

**Tabulation** skips the recursion entirely. It's like building a skyscraper: you start at the **FOUNDATION** (base cases) and build your way to the **TOP**.

We use a **Table** (usually an array) and fill it in order:
`Table[0] -> Table[1] -> Table[2] ... -> Table[n]`

```text
    DP Table:
    +---+---+---+---+---+---+
    | 0 | 1 | 1 | 2 | 3 | 5 | ...
    +---+---+---+---+---+---+
      0   1   2   3   4   5 (index)
```

> **Direction:** We start at the **BOTTOM** and work our way up to the **TOP**.

**Complexity:** $O(n)$ — Very fast and often more memory-efficient than memoization.

---

## 4. Space Optimization (The "Minimalist" Method)

Do we really need the _whole_ table?
To find the next Fibonacci number, we only need the **last two** numbers. We can throw the rest of the table away!

Instead of an array, we just use **two variables** (`prev1`, `prev2`).

**Complexity:**

- Time: $O(n)$
- Space: $O(1)$ — **The ultimate optimization!**

---

## Comparison Table

| Feature          | Recursion              | Memoization (Top-Down)  | Tabulation (Bottom-Up) |
| :--------------- | :--------------------- | :---------------------- | :--------------------- |
| **Strategy**     | Solve from scratch     | Recursion + Notebook    | Fill a Table           |
| **Direction**    | Top -> Bottom          | Top -> Bottom           | Bottom -> Top          |
| **Speed**        | ❌ Exponential ($2^n$) | ✅ Linear ($n$)         | ✅ Linear ($n$)        |
| **Memory**       | ❌ High (Stack)        | ⚠️ Medium (Stack + Map) | ✅ Low (Array)         |
| **Ease of Code** | Very Simple            | Simple                  | Moderate               |

---

## Key Takeaways

1.  **Don't Re-calculate:** If you see the same problem twice, save the answer!
2.  **Memoization** is great for problems where you don't need to solve _every_ single sub-part.
3.  **Tabulation** is usually faster because it avoids the "overhead" of calling functions thousands of times.
4.  **Space Optimization** can often turn an $O(n)$ space problem into an $O(1)$ space problem by only keeping what's necessary.
5.  **Dynamic Programming** makes the impossible $O(2^n)$ problems possible in $O(n)$ or $O(n^2)$.
