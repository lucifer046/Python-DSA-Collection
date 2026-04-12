<!-- +------------------------------------------------------+ -->
<!-- |    STRICT BINARY TREE — THE ALL-OR-NOTHING TREE      | -->
<!-- +------------------------------------------------------+ -->

# Strict Binary Tree — The All-or-Nothing Tree

## Theoretical Definition & Comparisons

**Theoretical Definition:** 
A Strict Binary Tree (also known as a **Full Binary Tree**) is a type of binary tree in which every node has either **zero** or **two** children. No node in a strict binary tree is allowed to have only one child.

**Comparison (Tree Variations):**
*   **Binary Tree:** Nodes can have 0, 1, or 2 children.
*   **Strict Binary Tree:** Nodes MUST have 0 or 2 children.
*   **Perfect Binary Tree:** A strict binary tree where all leaves are at the same depth.

---

## What is a Strict Binary Tree?

Imagine a **decision tree** for a "Yes/No" game.
- At every step, you must have two choices (Left or Right).
- You never have a step with only a "single" path; you either reach an answer (Leaf) or you have two more questions (Children).

---

## Visual Representation

```text
       OK (Strict):              NOT OK (Not Strict):
       
            ( )                        ( )
           /   \                      /   \
         ( )   ( )                  ( )   ( )
              /   \                /
            ( )   ( )            ( )    <-- Error! Only 1 child.
```

---

## Node Count Calculations (Based on Height $H$)

In a Strict Binary Tree, the restriction of "0 or 2 children" changes the minimum possible nodes for a specific height.

| Metric | Formula | Explanation |
|---|---|---|
| **Maximum Nodes** | $N_{max} = 2^{H+1} - 1$ | When the tree is **Perfectly Balanced**. |
| **Minimum Nodes** | $N_{min} = 2H + 1$ | When the tree grows by adding a leaf and a branch at each level. |

---

## Important Properties

1.  **Relation between Leaves and Internal Nodes:** 
    If a strict binary tree has $L$ leaves and $I$ internal nodes, then:
    $$L = I + 1$$
2.  **Total Nodes ($N$):**
    $$N = 2I + 1$$
3.  **Degree of Nodes:** 
    Every internal node has a degree of 2.

---

## Key Takeaways

1.  No node can have **exactly one child**.
2.  The number of leaf nodes is always one more than the number of internal nodes.
3.  For a given height $H$, it requires **more nodes** than a standard binary tree to remain "Strict" ($2H+1$ vs $H+1$).
4.  Commonly used in **Huffman Coding** and logic-based decision trees.
