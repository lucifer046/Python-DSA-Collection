<!-- +------------------------------------------------------+ -->
<!-- |      BINARY HEAP — THE PRIORITY MASTER             | -->
<!-- +------------------------------------------------------+ -->

# Binary Heap — The Priority Master

## Theoretical Foundation

**Theoretical Definition:** 
A Binary Heap is a complete binary tree that satisfies the **Heap Property**: in a Min-Heap, each node is smaller than or equal to its children; in a Max-Heap, each node is larger than or equal to its children. Because it is a complete tree, it is most efficiently stored as an **Array**.

### Comparison: Heap vs. BST vs. Array

| Feature | Binary Heap | Binary Search Tree (BST) | Unsorted Array |
|---|---|---|---|
| **Goal** | Quick access to Min/Max | Efficient searching/sorting | Simple storage |
| **Search Time** | $O(n)$ | $O(\log n)$ | $O(n)$ |
| **Get Min/Max** | **$O(1)$** | $O(\log n)$ | $O(n)$ |
| **Insertion** | $O(\log n)$ | $O(\log n)$ | $O(1)$ |
| **Best Use Case** | Priority Queues, Scheduling | Ordered data, fast searches | Small, static lists |

---

## What is a Heap? (The Triage Metaphor)

Imagine a **Hospital Emergency Room**. Patients are not treated "first-come, first-served." Instead, the one with the most urgent condition gets treated first. 
- A **Min-Heap** is like a list where the person with the "shortest wait time" is always at the top.
- A **Max-Heap** is like a tournament bracket where the "strongest player" is at the top.

> **Simple Definition:** A Heap is a specialized tree that keeps the **most important** item (the smallest or largest) at the very top (the root).

---

## Visual Representation

```text
       MIN-HEAP:                    MAX-HEAP:
          (1)                          (10)
         /   \                        /    \
       (5)   (3)                    (8)    (9)
      /  \                         /  \
    (10) (12)                    (3)  (5)
```

---

## Node Count Calculations (Based on Height $H$)

Since a Heap is a **Complete Binary Tree**, its nodes are packed as densely as possible.

| Metric | Formula | Explanation |
|---|---|---|
| **Maximum Nodes** | $N_{max} = 2^{H+1} - 1$ | When all levels are completely full (Perfect Tree). |
| **Minimum Nodes** | $N_{min} = 2^H$ | When the last level has exactly one node. |

---

## Step-by-Step Breakdown: "Heapify Up"

When we insert a new number, it might break the rule. We fix it by **bubbling it up**.

1. **Insert 2** into a Min-Heap: `[5, 10, 8]`.
2. 2 is added at the first empty spot: `[5, 10, 8, 2]`.
3. **Compare with parent (10):** 2 is smaller than 10. **Swap!**
4. **Compare with new parent (5):** 2 is smaller than 5. **Swap!**
5. **Result:** 2 is now the root. The tree is balanced again!

---

## Heap Sort Algorithm

Heap Sort uses the heap structure to sort an array efficiently without extra space (if done in-place).

### 1. Max-Heap Sort (For Ascending Order)
- Build a Max-Heap from the array.
- Repeatedly swap the root (max) with the last element.
- Shrink the heap size and "Heapify Down" the new root.
- **Complexity:** $O(n \log n)$.

### 2. Min-Heap Sort (For Descending Order)
- Build a Min-Heap.
- Extract the minimum repeatedly.
- **Complexity:** $O(n \log n)$.

---

## technical Summary: Time Complexities

| Operation | Time Complexity | Explanation |
|---|---|---|
| **Insertion** | $O(\log n)$ | Path from leaf to root. |
| **Deletion (Extract)** | $O(\log n)$ | Path from root to leaf. |
| **Update (Known Index)** | $O(\log n)$ | Either Heapify Up or Down. |
| **Update (Unknown Index)**| $O(n)$ | Must find the element first ($O(n)$), then update ($O(\log n)$). |
| **Peek Min/Max** | $O(1)$ | Always at index 0. |

---

## Key Takeaways

1.  Heaps are **not sorted**; they only guarantee the root is the extreme value.
2.  Implemented using **arrays** for memory efficiency.
3.  **Complete tree structure** ensures the height is always $\log n$.
4.  Standard tool for **Priority Queues** and **HeapSort**.
5.  **Building a heap** from an array takes $O(n)$ time using the bottom-up approach.
