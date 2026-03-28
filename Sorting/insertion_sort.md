<!-- +--------------------------------------------------+ -->
<!-- |  INSERTION SORT — THE CARD-SORTING METHOD        | -->
<!-- +--------------------------------------------------+ -->
# Insertion Sort — The Card-Sorting Method

## What is Insertion Sort?

Think of how you **sort cards in your hand** when playing a game.

You pick up cards one at a time. Each time you pick a new card, you **slide it left** into its correct position among the cards you're already holding.

> **Simple Definition:** Insertion Sort takes one item at a time and **inserts** it into the correct spot in the already-sorted part of the list.

---

## Step-by-Step Example

### Original List: `[12, 11, 13, 5, 6]`

---

### Step 1: Start with the first number (12)

```
  SORTED   | UNSORTED
  +----+   +----+----+----+----+
  | 12 |   | 11 | 13 |  5 |  6 |
  +----+   +----+----+----+----+
    ✅       Pick next: 11
```

A single number is already "sorted" by itself!

### Step 2: Pick 11 and INSERT it in the correct spot

```
  Pick up 11. Compare with 12.
  11 < 12? YES > Slide 12 to the right, insert 11 before it.

  +----+----+   +----+----+----+
  | 11 | 12 |   | 13 |  5 |  6 |
  +----+----+   +----+----+----+
    ✅   ✅       Pick next: 13

  Visualization of the slide:
  [12, 11, ...]  >  11 picks up  >  12 slides right  >  11 drops in  >  [11, 12, ...]
       ^ pick         [card]              -->               [v]
```

### Step 3: Pick 13 and INSERT

```
  Pick up 13. Compare with 12.
  13 < 12? NO > 13 stays where it is!

  +----+----+----+   +----+----+
  | 11 | 12 | 13 |   |  5 |  6 |
  +----+----+----+   +----+----+
    ✅   ✅   ✅       Pick next: 5
```

### Step 4: Pick 5 and INSERT

```
  Pick up 5. Compare backwards:
  5 < 13? YES > Slide 13 right
  5 < 12? YES > Slide 12 right
  5 < 11? YES > Slide 11 right
  No more to check > Insert 5 at position 0!

  Sliding animation:
  [11, 12, 13,  5, ...]
                ^ pick up 5 [card]
  
  [11, 12, __, 13, ...]  < 13 slides right
  [11, __, 12, 13, ...]  < 12 slides right
  [__, 11, 12, 13, ...]  < 11 slides right
  [ 5, 11, 12, 13, ...]  < Insert 5! ✅

  Result:
  +----+----+----+----+   +----+
  |  5 | 11 | 12 | 13 |   |  6 |
  +----+----+----+----+   +----+
    ✅   ✅   ✅   ✅       Pick next: 6
```

### Step 5: Pick 6 and INSERT

```
  Pick up 6. Compare backwards:
  6 < 13? YES > Slide 13 right
  6 < 12? YES > Slide 12 right
  6 < 11? YES > Slide 11 right
  6 < 5?  NO  > Insert 6 RIGHT HERE!

  [ 5, __, 11, 12, 13]  
  [ 5,  6, 11, 12, 13]  < Insert 6! ✅

  FINAL RESULT:
  +----+----+----+----+----+
  |  5 |  6 | 11 | 12 | 13 |
  +----+----+----+----+----+
    ✅   ✅   ✅   ✅   ✅   ALL SORTED!
```

---

## Summary of All Steps

```
  Start:    [12, 11, 13,  5,  6]
  
  Step 1:   [12] 11, 13,  5,  6     < 12 is sorted by itself
  Step 2:   [11, 12] 13,  5,  6     < 11 inserted before 12
  Step 3:   [11, 12, 13]  5,  6     < 13 already in place
  Step 4:   [ 5, 11, 12, 13]  6     < 5 inserted at the start
  Step 5:   [ 5,  6, 11, 12, 13]    < 6 inserted after 5
  
  DONE! ✅
```

---

## Selection Sort vs Insertion Sort

| Feature | Selection Sort | Insertion Sort |
|---|---|---|
| **Strategy** | Find the minimum, place it | Pick an item, slide it into place |
| **Best case** | O(n²) always | O(n) if already sorted! |
| **Worst case** | O(n²) | O(n²) |
| **Good for** | Small lists | Nearly-sorted lists |

> **Fun fact:** Insertion Sort is **very fast** if the list is already almost sorted! It barely needs to slide anything.

---

## Key Takeaways

1. Insertion Sort works like **sorting cards in your hand**
2. Pick each item and **slide it left** until it reaches its correct position
3. The sorted section grows from left to right
4. **Best case: O(n)** — if the list is nearly sorted, it's blazing fast!
5. **Worst case: O(n²)** — if the list is in reverse order, lots of sliding needed
