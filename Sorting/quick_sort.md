<!-- +--------------------------------------------------+ -->
<!-- |  QUICK SORT — THE PICK-A-PIVOT METHOD            | -->
<!-- +--------------------------------------------------+ -->
# Quick Sort — The Pick-a-Pivot Method

## What is Quick Sort?

Imagine you're a teacher sorting students by **height**. You pick **one student** (let's call them the "Pivot") and stand them in the middle:

- Everyone **shorter** than the Pivot stands to their **LEFT**.
- Everyone **taller** stands to their **RIGHT**.
- Now the Pivot is in their **perfect spot**!
- You repeat this process for the left group and the right group.

> **Simple Definition:** Quick Sort picks a **Pivot** number, puts everything smaller on its left and everything larger on its right, then does the same for each side.

---

## Visual Representation

![Quick Sort Partitioning Diagram](docs/images/quick_sort_diagram.png)

> [!NOTE]
> **Teacher's Perspective:** "Look at the diagram above. The **Pivot** (gold) is the middle-ground student we picked. Notice how everyone shorter (to the left) and everyone taller (to the right) is organized around them. Once this step is done, the Pivot doesn't need to move ever again—they are in their final, perfect spot!"

---

## Step-by-Step Breakdown (Teacher's Guide)

Let's walk through an example. If we have a list of students with heights `[10, 80, 30, 90, 40, 50, 70]`:

### Pass 1: Choosing a Leader (Pivot)
We pick the first student, **10**, as our Pivot. 
- We scan the rest of the line. 
- Since **10** is the shortest already, everyone else naturally stays to its right.
- **Result:** `[10]` is locked in. Now we focus on `[80, 30, 90, 40, 50, 70]`.

### Pass 2: The Next Group
We pick **80** as the new leader for this group.
- **Shorty Check:** 30, 40, 50, and 70 are all shorter than 80. They move to the **LEFT** of 80.
- **Tall Check:** 90 is taller than 80. It stays to the **RIGHT**.
- **Result:** `[30, 40, 50, 70]` < **80** > `[90]`. 
- Now **80** and **90** are perfectly placed!

### Pass 3: Finishing Up
We repeat this for the small group `[30, 40, 50, 70]` until everyone is standing in line perfectly from shortest to tallest.

---

## Why does this work so well?
Quick Sort is like a delegator. Instead of trying to sort 100 people at once, it picks one person to divide the group into two smaller, easier-to-manage groups. It keeps doing this until the groups are so small (1 person) that they are already "sorted"!

---

## Full Recursion Tree

```
                    [10, 80, 30, 90, 40, 50, 70]
                           Pivot = 10
                    +----------+-----------+
                   [10]              [80, 30, 90, 40, 50, 70]
                    ✅                     Pivot = 80
                                   +-----------+--------+
                           [30, 40, 50, 70]              [90]
                              Pivot = 30                   ✅
                          +--------+-------+
                         [30]        [40, 50, 70]
                          ✅           Pivot = 40
                                   +-----+------+
                                  [40]      [50, 70]
                                   ✅        Pivot = 50
                                          +----+----+
                                         [50]      [70]
                                          ✅        ✅
  
  Final: [10, 30, 40, 50, 70, 80, 90] ✅
```

---

## Quick Sort vs Merge Sort

| Feature | Merge Sort | Quick Sort |
|---|---|---|
| **Strategy** | Split in half, merge sorted halves | Pick pivot, partition, recurse |
| **Average speed** | O(n log n) | O(n log n) |
| **Worst case** | O(n log n) always | O(n²) if bad pivot chosen |
| **Extra memory** | Needs extra space for merging | Sorts in-place (no extra space!) |
| **Real-world use** | Python's sorted() uses a variant | Many systems use Quick Sort |

---

## Key Takeaways

1. Quick Sort picks a **Pivot** and puts everything smaller to its left, larger to its right
2. After partitioning, the Pivot is in its **final correct position**
3. The process repeats for the left and right groups
4. **Average case: O(n log n)** — very fast!
5. **Worst case: O(n²)** — happens when the pivot is always the smallest or largest
6. It sorts **in-place** — no extra memory needed (unlike Merge Sort)

