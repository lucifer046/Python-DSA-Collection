<!-- ╔══════════════════════════════════════════╗ -->
<!-- ║  BINARY SEARCH — THE PHONEBOOK METHOD    ║ -->
<!-- ╚══════════════════════════════════════════╝ -->
# Binary Search — The Phonebook Method

## What is Binary Search?

Imagine you're looking for a name in a **thick phone book**. Would you start at page 1 and read every single name? Of course not!

You'd open the book **in the middle**. If the name you want comes before the middle page, you flip to the **left half**. If it comes after, you flip to the **right half**. You keep halving until you find the name!

> **Simple Definition:** Binary Search is a super-fast way to find a number in a **sorted list** by cutting the search area in **half** with each step.

> **Critical Rule:** The list MUST be sorted first! Binary Search doesn't work on messy lists.

---

## Step-by-Step Example

### The Sorted List:
```
  Index:   0    1    2    3    4    5    6    7    8    9
        ┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐
  List: │  2 │  5 │  8 │ 12 │ 16 │ 23 │ 38 │ 56 │ 72 │ 91 │
        └────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘
```

### Goal: Find the number **23**

---

### Step 1: Look at the FULL list

```
  start = 0                                          end = 9
    │                                                  │
    ▼                                                  ▼
  ┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐
  │  2 │  5 │  8 │ 12 │ 16 │ 23 │ 38 │ 56 │ 72 │ 91 │
  └────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘
                            ↑
                        middle = 4
                       value = 16

  Question: Is 16 == 23?  NO.
  Question: Is 16 < 23?   YES → Target is in the RIGHT half!
  Action:   Move start to middle + 1 = 5
```

### Step 2: Search the RIGHT half only

```
                              start = 5                end = 9
                                │                        │
                                ▼                        ▼
  ┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐
  │  2 │  5 │  8 │ 12 │ 16 │ 23 │ 38 │ 56 │ 72 │ 91 │
  └────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘
  ░░░░░░░░░░░░░░░░░░░░░░░░░░         ↑
    (ignored — thrown away!)      middle = 7
                                 value = 56

  Question: Is 56 == 23?  NO.
  Question: Is 56 > 23?   YES → Target is in the LEFT half!
  Action:   Move end to middle - 1 = 6
```

### Step 3: Search an even smaller section

```
                              start = 5   end = 6
                                │           │
                                ▼           ▼
  ┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐
  │  2 │  5 │  8 │ 12 │ 16 │ 23 │ 38 │ 56 │ 72 │ 91 │
  └────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘
  ░░░░░░░░░░░░░░░░░░░░░░░░░░    ↑    ░░░░░░░░░░░░░░░░
                             middle = 5
                            value = 23

  Question: Is 23 == 23?  YES!!
  FOUND IT at index 5!
```

---

## The "Halving" Effect — Why It's So Fast

```
  Step 1:  Search 10 items     ──────────────────────────────
  Step 2:  Search 5 items      ───────────────
  Step 3:  Search 2 items      ──────
  FOUND!

  Total steps: Just 3! (instead of checking all 10 one by one)
```

### How many steps for bigger lists?

| List Size | Linear Search (One-by-One) | Binary Search (Halving) |
|---|---|---|
| 10 items | Up to 10 checks | Up to 4 checks |
| 1,000 items | Up to 1,000 checks | Up to 10 checks |
| 1,000,000 items | Up to 1,000,000 checks | Up to 20 checks |
| 1,000,000,000 items | Up to 1 billion checks | Up to **30 checks**! |

---

## Two Ways to Write Binary Search

### Iterative (Using a While Loop)

```
  Start ──▶ Calculate Middle ──▶ Compare ──▶ Adjust boundaries ──▶ Repeat
                 ↑                                                    │
                 └────────────────────────────────────────────────────┘
                               (Loop until found or empty)
```

### Recursive (Function Calls Itself)

```
  search([2,5,8,12,16,23,38,56,72,91], target=23, start=0, end=9)
         │
         ├──▶ middle=4, value=16, 16 < 23 → search RIGHT
         │
         └──▶ search([...], target=23, start=5, end=9)
                   │
                   ├──▶ middle=7, value=56, 56 > 23 → search LEFT
                   │
                   └──▶ search([...], target=23, start=5, end=6)
                             │
                             └──▶ middle=5, value=23 == 23 → FOUND! [done]
```

Both methods give the **same result**. The recursive version calls itself with a smaller range each time.

---

## Linear Search vs Binary Search

```
  LINEAR SEARCH (One by one):
  Check 2? No. Check 5? No. Check 8? No. Check 12? No. Check 16? No. Check 23? YES!
  ──▶──▶──▶──▶──▶──▶
  (6 checks!)

  BINARY SEARCH (Halving):
  Middle=16? Too small, look right. Middle=56? Too big, look left. Middle=23? YES!
  (Only 3 checks!)
```

---

## Key Takeaways

1. Binary Search only works on **sorted lists**
2. It cuts the search area in **half** with every step
3. Time complexity: **O(log n)** — incredibly fast even for billions of items
4. It works like finding a name in a phonebook — you don't read every page!
5. Two implementations: **Iterative** (while loop) and **Recursive** (self-calling function)
