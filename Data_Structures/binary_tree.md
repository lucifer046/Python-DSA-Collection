<!-- +------------------------------------------------------+ -->
<!-- |      BINARY TREE — THE HIERARCHICAL FOUNDATION      | -->
<!-- +------------------------------------------------------+ -->

# Binary Tree — The Hierarchical Foundation

## Theoretical Definition & Comparisons

**Theoretical Definition:** 
A Binary Tree is a non-linear data structure where each node has at most two children, referred to as the left child and the right child. It is the fundamental building block for more complex structures like BSTs, AVL Trees, and Heaps.

**Comparison (Tree Structures):**
*   **Binary Tree:** Every node has 0, 1, or 2 children. No specific ordering rule.
*   **Strict Binary Tree:** Every node has either 0 or 2 children. No node has only 1 child.
*   **Binary Search Tree (BST):** A binary tree with an ordering rule (Left < Parent < Right).

---

## What is a Binary Tree?

Imagine an **organizational chart** of a company where every manager can have at most **two direct reports**.
- The top-most person is the **Root**.
- People with no reports are the **Leaves**.
- The connections between them are **Edges**.

---

## Visual Representation

```text
          (Root)
           /  \
        (A)    (B)
        / \      \
     (C)  (D)    (E)
```

---

## Node Count Calculations (Based on Height $H$)

The height $H$ is the number of edges on the longest path from the root to a leaf.

| Metric | Formula | Explanation |
|---|---|---|
| **Maximum Nodes** | $N_{max} = 2^{H+1} - 1$ | Occurs when the tree is **Full** (every level is packed). |
| **Minimum Nodes** | $N_{min} = H + 1$ | Occurs when the tree is **Skewed** (like a linked list). |

---

## Key Types of Binary Trees

1.  **Full Binary Tree:** Every node has 0 or 2 children.
2.  **Complete Binary Tree:** All levels are completely filled except possibly the last, which is filled from left to right.
3.  **Perfect Binary Tree:** All internal nodes have two children and all leaves are at the same level.
4.  **Balanced Binary Tree:** The height of the left and right subtrees of every node differs by at most 1 (e.g., AVL Tree).

---

## Key Takeaways

1.  Each node has a **maximum of 2 children**.
2.  **Height** determines the maximum capacity of the tree.
3.  **Leaf nodes** have no children.
4.  Standard for representing hierarchical data and hierarchical decisions.
