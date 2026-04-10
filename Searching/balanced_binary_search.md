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

## 🖼️ Visual Representation

![AVL Tree Balancing Rotations Diagram](docs/images/avl_tree_diagram.png)

> [!NOTE]
> **Teacher's Perspective:** "Imagine a balanced scale! If you add too much weight (numbers) to one side, the scale tips. In a normal tree, it just stays tipped over and becomes hard to use. But an **AVL Tree** is smart! The moment it feels too much weight on one side, it performs a **Rotation**—a quick 'swing' of the branches—to bring everything back to a perfect balance. This keeps the tree short and the search speed lightning fast!"

---

## 🎓 Step-by-Step Breakdown (Teacher's Guide)

Let's see why we need these "rotations" to keep things fair.

### The Problem: The "Straight Line" Disaster
If we add numbers in perfect order (1, 2, 3, 4, 5), a normal tree grows like a long, spindly twig. 
- To find **5**, you'd have to walk down 5 steps. 
- In a big tree of 1 million items, you'd walk **1 million steps**! That's too slow.

### The Solution: The AVL "Self-Fix"
An AVL tree has a rule: No side can be more than **1 level** taller than the other. If it is, we **ROTATE**.

1. **Insert 1, then 2:** Tree looks fine.
2. **Insert 3:** Now the right side is 2 levels deep while the left is empty. **TILT!**
3. **Action (Left Rotation):** We lift 2 up to be the new boss. 1 becomes its left child, and 3 becomes its right child.
4. **Result:** A perfect, balanced triangle! Now to find any number, you only need **2 steps** instead of 3.

---

## 🧠 Why are "Rotations" the Secret Sauce?
A rotation is a mathematical trick that changes the structure of the tree **without** breaking the sorted order rule (smaller numbers still on the left, larger on the right). It's like re-organizing your bookshelf so you can reach every book easily!

---


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

