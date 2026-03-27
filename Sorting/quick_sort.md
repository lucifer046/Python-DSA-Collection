<!-- ╔══════════════════════════════════════════════════╗ -->
<!-- ║  QUICK SORT — THE PICK-A-PIVOT METHOD            ║ -->
<!-- ╚══════════════════════════════════════════════════╝ -->
# Quick Sort — The Pick-a-Pivot Method

## What is Quick Sort?

Imagine you're a teacher sorting students by **height**. You pick **one student** (let's call them the "Pivot") and stand them in the middle:

- Everyone **shorter** than the Pivot stands to their **LEFT**.
- Everyone **taller** stands to their **RIGHT**.
- Now the Pivot is in their **perfect spot**!
- You repeat this process for the left group and the right group.

> **Simple Definition:** Quick Sort picks a **Pivot** number, puts everything smaller on its left and everything larger on its right, then does the same for each side.

---

## Step-by-Step Example

### Original List: `[10, 80, 30, 90, 40, 50, 70]`

---

### Pass 1: Partition around the first element (Pivot = 10)

```
  Pivot = 10
  ┌────┬────┬────┬────┬────┬────┬────┐
  │ 10 │ 80 │ 30 │ 90 │ 40 │ 50 │ 70 │
  └────┴────┴────┴────┴────┴────┴────┘
    ↑ PIVOT
  
  Scan all elements:
  80 > 10 → stays right ✓
  30 > 10 → stays right ✓
  90 > 10 → stays right ✓
  40 > 10 → stays right ✓
  50 > 10 → stays right ✓
  70 > 10 → stays right ✓
  
  Nothing is smaller than 10, so 10 goes to position 0!
  
  Result:
  ┌────┐ ┌────┬────┬────┬────┬────┬────┐
  │ 10 │ │ 80 │ 30 │ 90 │ 40 │ 50 │ 70 │
  └────┘ └────┴────┴────┴────┴────┴────┘
    [done]     (now sort this part)
  Pivot is
  in its
  final spot!
```

### Pass 2: Partition the right section (Pivot = 80)

```
  Pivot = 80
  ┌────┬────┬────┬────┬────┬────┐
  │ 80 │ 30 │ 90 │ 40 │ 50 │ 70 │
  └────┴────┴────┴────┴────┴────┘
    ↑ PIVOT

  Scan:
  30 ≤ 80 → Move to left section ✓
  90 > 80 → stays right ✓
  40 ≤ 80 → Move to left section ✓
  50 ≤ 80 → Move to left section ✓
  70 ≤ 80 → Move to left section ✓
  
  After partition:
  ┌────┬────┬────┬────┐ ┌────┐ ┌────┐
  │ 30 │ 40 │ 50 │ 70 │ │ 80 │ │ 90 │
  └────┴────┴────┴────┘ └────┘ └────┘
    (sort this)            [done]     (sort this)
                        Pivot in
                        final spot!
```

### The process continues recursively...

```
  [30, 40, 50, 70] → Pivot=30 → [30] [40, 50, 70]
  [40, 50, 70]     → Pivot=40 → [40] [50, 70]
  [50, 70]         → Pivot=50 → [50] [70]
```

### Final Sorted List:
```
  ┌────┬────┬────┬────┬────┬────┬────┐
  │ 10 │ 30 │ 40 │ 50 │ 70 │ 80 │ 90 │
  └────┴────┴────┴────┴────┴────┴────┘
    [done]   [done]   [done]   [done]   [done]   [done]   [done]
```

---

## How Partitioning Works (The Core Magic)

Let's zoom into one partition step with a clearer example:

### Partition `[50, 30, 80, 20, 70, 40]` with Pivot = 50

```
  Step 0:  Pivot = 50, boundary at position 0
           [50, 30, 80, 20, 70, 40]
            ↑P  ↑scan
            B=0

  Step 1:  30 ≤ 50 → Move boundary right, swap
           [50, 30, 80, 20, 70, 40]
                 ↑B  ↑scan

  Step 2:  80 > 50 → Do nothing
           [50, 30, 80, 20, 70, 40]
                 ↑B      ↑scan

  Step 3:  20 ≤ 50 → Move boundary right, swap 80 and 20
           [50, 30, 20, 80, 70, 40]
                     ↑B      ↑scan

  Step 4:  70 > 50 → Do nothing
           [50, 30, 20, 80, 70, 40]
                     ↑B          ↑scan

  Step 5:  40 ≤ 50 → Move boundary right, swap 80 and 40
           [50, 30, 20, 40, 70, 80]
                         ↑B      

  Final:   Swap Pivot(50) with boundary position(40)
           [40, 30, 20, 50, 70, 80]
                         ↑
                    PIVOT IS HERE!
                    (Perfect spot!)

  Result:  [40, 30, 20] < 50 > [70, 80]
             LEFT SIDE    ↑    RIGHT SIDE
                        PIVOT
```

---

## Full Recursion Tree

```
                    [10, 80, 30, 90, 40, 50, 70]
                           Pivot = 10
                    ┌──────────┴───────────┐
                   [10]              [80, 30, 90, 40, 50, 70]
                    [done]                     Pivot = 80
                                   ┌───────────┴────────┐
                           [30, 40, 50, 70]              [90]
                              Pivot = 30                   [done]
                          ┌────────┴───────┐
                         [30]        [40, 50, 70]
                          [done]           Pivot = 40
                                   ┌─────┴──────┐
                                  [40]      [50, 70]
                                   [done]        Pivot = 50
                                          ┌────┴────┐
                                         [50]      [70]
                                          [done]        [done]
  
  Final: [10, 30, 40, 50, 70, 80, 90] [done]
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
