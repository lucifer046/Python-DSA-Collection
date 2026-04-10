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

## 🖼️ Visual Representation

![Selection Sort "Minimum Finder" Diagram](docs/images/selection_sort_diagram.png)

> [!NOTE]
> **Teacher's Perspective:** "Imagine you have a row of students of different heights. You walk down the line, starting from the first student, looking for the absolute **shortest** one. Once you find them, you swap them with the first person in line. Now, that first spot is 'solved'! You repeat this for the rest of the line until everyone is perfectly organized."

---

## 🎓 Step-by-Step Breakdown (Teacher's Guide)

Let's sort these numbers: `[64, 25, 12, 22, 11]`

### Pass 1: The First Scan
- We look at everyone: 64, 25, 12, 22, 11.
- **Winner:** 11 is the smallest!
- **Action:** Swap 11 with the first person (64).
- **Current Row:** `[11]` | `25, 12, 22, 64` (11 is now in his permanent home!)

### Pass 2: The Second Scan
- We ignore 11 and look at: 25, 12, 22, 64.
- **Winner:** 12 is the smallest here.
- **Action:** Swap 12 with the first person in the *unsorted* part (25).
- **Current Row:** `[11, 12]` | `25, 22, 64`

### Pass 3: Keep it Going
- Scan 25, 22, 64.
- **Winner:** 22.
- **Action:** Swap 22 with 25.
- **Current Row:** `[11, 12, 22]` | `25, 64`

### Pass 4 & 5: Finishing Up
- We see 25 is smaller than 64, so it stays. Finally, 64 is the last man standing.
- **Final Result:** `[11, 12, 22, 25, 64]` ✅ **All Sorted!**

---

## 🧠 Why is it called "Selection" Sort?
Because at every step, your only job is to **Select** the smallest remaining item and put it in the next available spot. It's like picking the best fruit from a basket one by one!

---


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

