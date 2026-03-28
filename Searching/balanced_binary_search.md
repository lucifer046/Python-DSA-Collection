<!-- +------------------------------------------------------------------+ -->
<!-- |  BALANCED BST (AVL TREE) — THE SELF-BALANCING LIBRARY            | -->
<!-- +------------------------------------------------------------------+ -->
# Balanced Binary Search Tree (AVL Tree) — The Self-Balancing Library

## What is a Binary Search Tree (BST)?

Imagine a **family tree** for numbers:
- Each person (node) can have at most **2 children** — a LEFT child and a RIGHT child.
- **Rule:** ALL numbers smaller than the parent go **LEFT**, ALL numbers larger go **RIGHT**.

> This rule makes searching super fast — you just go left or right at each step instead of checking everything!

---

## The Problem: Unbalanced Trees

What happens if you add numbers **in order** like 1, 2, 3, 4, 5?

```
  BALANCED TREE (Good!):             UNBALANCED TREE (Bad!):
  
         4                            1
        / \                            \
       2   5                            2
      / \                                \
     1   3                                3
                                           \
   Height: 3                                4
   Search: O(log n) [FAST]                   \
                                              5
                                              
                                         Height: 5
                                         Search: O(n) [SLOW]
                                         (Same as a linked list!)
```

The unbalanced tree becomes just a **straight line** — no better than a linked list!

---

## The Solution: AVL Tree (Self-Balancing!)

An **AVL Tree** (invented by Adelson-Velsky and Landis in 1962) is a BST that **automatically fixes itself** whenever it becomes unbalanced.

### The Balance Factor Rule

For every node:  
**Balance Factor = Height of Left Side − Height of Right Side**

```
  ALLOWED balance factors: -1, 0, +1  [OK]
  NOT ALLOWED: -2, +2 or worse        ❌ --> Triggers a ROTATION!
```

---

## Building an AVL Tree — Step by Step

### Example: Insert numbers [1, 2, 3, 4, 5, 6, 7]

**Insert 1:**
```
     1
  
  (Balance Factor = 0) ✅ All good!
```

**Insert 2:**
```
     1
      \
       2
  
  (BF of node 1 = 0 - 1 = -1) ✅ Still fine!
```

**Insert 3: [!] UNBALANCED!**
```
     1          Balance Factor of 1 = 0 - 2 = -2  ❌
      \
       2        PROBLEM: Right-Right heavy!
        \       
         3      SOLUTION: LEFT ROTATION on node 1
```

### LEFT ROTATION (Fixing Right-Right Imbalance)

Think of it like a see-saw that's tilting too much to the right. We need to **lift the right side up**!

```
  BEFORE (leaning right):          AFTER LEFT ROTATION:
  
       1                                 2
        \                               / \
         2                             1   3
          \
           3                    ✅ BALANCED!
```

**What happened:**
1. Node **2** (the right child) becomes the **new boss** (root)
2. Node **1** (the old boss) becomes the **left child** of 2
3. Node **3** stays as the right child of 2

**Continue inserting 4:**
```
       2                        2
      / \                      / \
     1   3          >         1   3
          \                        \
           4                        4
           
  (BF of 3 = -1) ✅ Fine!
```

**Insert 5: [!] UNBALANCED at node 3!**
```
       2                        2
      / \                      / \
     1   3          >         1   4      < LEFT ROTATION on 3
          \                      / \
           4                    3   5
            \
             5
```

**Insert 6: [!] UNBALANCED at node 2!**
```
       2                            4
      / \                          / \
     1   4          >             2   5      < LEFT ROTATION on 2
        / \                      / \   \
       3   5                    1   3   6
            \
             6
```

**Insert 7: [!] UNBALANCED at node 5!**
```
         4                          4
        / \                        / \
       2   5          >           2   6      < LEFT ROTATION on 5
      / \   \                    / \ / \
     1   3   6                  1  3 5  7
              \
               7

  FINAL BALANCED TREE! ✅
```

---

## RIGHT ROTATION (Fixing Left-Left Imbalance)

Opposite of left rotation — used when the tree is **leaning too much to the LEFT**.

```
  BEFORE (leaning left):           AFTER RIGHT ROTATION:
  
           5                            3
          /                            / \
         3                            2   5
        /
       2                       ✅ BALANCED!
```

---

## DOUBLE ROTATION (Fixing Zigzag Imbalances)

Sometimes the tree has a **zigzag** shape (Left-Right or Right-Left). A single rotation won't fix it!

### Left-Right Case:
```
  BEFORE:                STEP 1: Left rotate     STEP 2: Right rotate
                         the left child           the root
       5                      5                        4
      /                      /                        / \
     3          >           4            >           3   5
      \                    /
       4                  3              ✅ BALANCED!
```

### Right-Left Case:
```
  BEFORE:                STEP 1: Right rotate    STEP 2: Left rotate
                         the right child          the root
     3                        3                        4
      \                        \                      / \
       5          >             4           >        3   5
      /                          \
     4                            5          ✅ BALANCED!
```

---

## Tree Traversal Orders

There are 3 ways to "read" all numbers from a tree:

### Given this tree:
```
         4
        / \
       2   6
      / \ / \
     1  3 5  7
```

| Order | Rule | Result |
|---|---|---|
| **Inorder** | Left > Root > Right | `[1, 2, 3, 4, 5, 6, 7]` < Always sorted! |
| **Preorder** | Root > Left > Right | `[4, 2, 1, 3, 6, 5, 7]` |
| **Postorder** | Left > Right > Root | `[1, 3, 2, 5, 7, 6, 4]` |

### Inorder Traversal Walkthrough:
```
         4
        / \
       2   6
      / \ / \
     1  3 5  7

  Start at root (4):
    > Go LEFT to 2
      > Go LEFT to 1
        > No left child > Visit 1 ✅  > No right child
      > Visit 2 ✅
      > Go RIGHT to 3
        > No left child > Visit 3 ✅  > No right child
    > Visit 4 ✅
    > Go RIGHT to 6
      > Go LEFT to 5
        > No left child > Visit 5 ✅  > No right child
      > Visit 6 ✅
      > Go RIGHT to 7
        > No left child > Visit 7 ✅  > No right child
  
  Result: [1, 2, 3, 4, 5, 6, 7] < Perfectly sorted!
```

---

## Why AVL Trees Matter

| Feature | Normal BST | AVL Tree |
|---|---|---|
| **Worst-case height** | O(n) — becomes a line | O(log n) — always balanced |
| **Search time** | O(n) worst case | O(log n) guaranteed |
| **Insert time** | O(n) worst case | O(log n) guaranteed |
| **Self-balancing?** | ❌ No | ✅ Yes, automatically! |

> With **1 million** numbers, an AVL tree needs only about **20 steps** to find any number. A normal BST in the worst case could need **1 million steps**!

---

## Key Takeaways

1. A BST stores numbers with **smaller on the left, larger on the right**
2. If data arrives in order, a normal BST becomes a **straight line** (very slow!)
3. An **AVL Tree** fixes this by automatically **rotating** whenever it gets unbalanced
4. **Balance Factor** = Height(Left) − Height(Right), must be -1, 0, or +1
5. **Rotations** are the self-correcting moves: Left, Right, Left-Right, Right-Left
6. **Inorder traversal** always gives numbers in **sorted order**
7. Guaranteed **O(log n)** search time — even with millions of items!
