<!-- +--------------------------------------------------+ -->
<!-- |  SELECTION SORT — SORTING BY REPEATED PICKING    | -->
<!-- +--------------------------------------------------+ -->
# Selection Sort — Sorting by Repeated Picking

## What is Selection Sort?

Imagine you have a messy hand of **playing cards**. To sort them:

1. Look at **ALL** the cards and find the **smallest** one.
2. Move it to the very **left** of your hand.
3. Now look at the remaining (unsorted) cards, find the next smallest.
4. Put it next to the first card.
5. Keep repeating until every card is in place!

> **Simple Definition:** Selection Sort splits your list into two parts — a **SORTED** part (left) and an **UNSORTED** part (right). Each time, it **selects** the smallest item from the unsorted part and adds it to the sorted part.

---

## Step-by-Step Example

### Original List: `[64, 25, 12, 22, 11]`

---

### Pass 1: Find the smallest in the ENTIRE list

```
  UNSORTED (everything)
  +----+----+----+----+----+
  | 64 | 25 | 12 | 22 | 11 |
  +----+----+----+----+----+
    ^                    ^
  start                smallest = 11 (at index 4)

  ACTION: Swap 64 and 11

  Result:
  SORTED | UNSORTED
  +----+ +----+----+----+----+
  | 11 | | 25 | 12 | 22 | 64 |
  +----+ +----+----+----+----+
    ✅
```

### Pass 2: Find the smallest in the UNSORTED part

```
  SORTED | UNSORTED
  +----+ +----+----+----+----+
  | 11 | | 25 | 12 | 22 | 64 |
  +----+ +----+----+----+----+
           ^    ^
         start  smallest = 12 (at index 2)

  ACTION: Swap 25 and 12

  Result:
  SORTED      | UNSORTED
  +----+----+ +----+----+----+
  | 11 | 12 | | 25 | 22 | 64 |
  +----+----+ +----+----+----+
    ✅   ✅
```

### Pass 3: Find the smallest again

```
  SORTED      | UNSORTED
  +----+----+ +----+----+----+
  | 11 | 12 | | 25 | 22 | 64 |
  +----+----+ +----+----+----+
                ^    ^
              start  smallest = 22 (at index 3)

  ACTION: Swap 25 and 22

  Result:
  SORTED           | UNSORTED
  +----+----+----+ +----+----+
  | 11 | 12 | 22 | | 25 | 64 |
  +----+----+----+ +----+----+
    ✅   ✅   ✅
```

### Pass 4: Almost done!

```
  SORTED           | UNSORTED
  +----+----+----+ +----+----+
  | 11 | 12 | 22 | | 25 | 64 |
  +----+----+----+ +----+----+
                      ^
                smallest = 25 (already in place!)

  Result:
  SORTED                | UNSORTED
  +----+----+----+----+ +----+
  | 11 | 12 | 22 | 25 | | 64 |
  +----+----+----+----+ +----+
    ✅   ✅   ✅   ✅
```

### Final Result:
```
  ALL SORTED! ✅
  +----+----+----+----+----+
  | 11 | 12 | 22 | 25 | 64 |
  +----+----+----+----+----+
    ✅   ✅   ✅   ✅   ✅
```

---

## Visual Summary of All Passes

```
  Pass 1:  [64, 25, 12, 22, 11]  > Find min(11) > Swap with 64  > [11, 25, 12, 22, 64]
  Pass 2:  [11, 25, 12, 22, 64]  > Find min(12) > Swap with 25  > [11, 12, 25, 22, 64]
  Pass 3:  [11, 12, 25, 22, 64]  > Find min(22) > Swap with 25  > [11, 12, 22, 25, 64]
  Pass 4:  [11, 12, 22, 25, 64]  > Find min(25) > Already there > [11, 12, 22, 25, 64]
  
  DONE! ✅  [11, 12, 22, 25, 64]
```

---

## How Fast Is It?

| List Size | Comparisons Needed |
|---|---|
| 5 items | 10 comparisons |
| 10 items | 45 comparisons |
| 100 items | 4,950 comparisons |
| 1,000 items | 499,500 comparisons |

**Time Complexity: O(n²)** — It's simple but **slow** for large lists!

---

## Key Takeaways

1. Selection Sort **scans** the entire unsorted section to find the smallest item
2. It **swaps** that smallest item to the front of the unsorted section
3. The sorted section **grows by 1** with each pass
4. It's **simple to understand** but **slow** for big lists — O(n²)
5. Best for small lists or when you want a simple, easy-to-code solution
