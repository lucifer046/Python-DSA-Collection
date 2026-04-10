<!-- +--------------------------------------------------+ -->
<!-- |  INSERTION SORT — THE CARD-SORTING METHOD        | -->
<!-- +--------------------------------------------------+ -->
# Insertion Sort — The Card-Sorting Method

## What is Insertion Sort?

Think of how you **sort cards in your hand** when playing a game.

You pick up cards one at a time. Each time you pick a new card, you **slide it left** into its correct position among the cards you're already holding.

> **Simple Definition:** Insertion Sort takes one item at a time and **inserts** it into the correct spot in the already-sorted part of the list.

---

## 🖼️ Visual Representation

![Insertion Sort "Card Sliding" Diagram](docs/images/insertion_sort_diagram.png)

> [!NOTE]
> **Teacher's Perspective:** "Imagine you're playing a card game. You pick up cards one by one. Each time you get a new card, you **slide it left** through your hand until it finds its perfect spot between a smaller card and a larger one. By the time you've picked up all the cards, your hand is perfectly sorted!"

---

## 🎓 Step-by-Step Breakdown (Teacher's Guide)

Let's sort these numbers: `[12, 11, 13, 5, 6]`

### Step 1: Holding the first card
- You hold **12**. A single card is already sorted!
- **Hand:** `[12]` | Next card to pick: 11

### Step 2: Picking 11
- You pick up 11. Is 11 smaller than 12? **Yes!**
- **Action:** Slide 12 to the right and drop 11 into the first spot.
- **Hand:** `[11, 12]` | Next card to pick: 13

### Step 3: Picking 13
- You pick up 13. Is 13 smaller than 12? **No.**
- **Action:** Keep 13 right where it is.
- **Hand:** `[11, 12, 13]` | Next card: 5

### Step 4: Picking 5 (The Big Slide)
- You pick up 5. It's smaller than 13... smaller than 12... even smaller than 11!
- **Action:** Everyone slides to the right to make room. 5 drops into the very first spot.
- **Hand:** `[5, 11, 12, 13]` | Next card: 6

### Step 5: Final Card (6)
- Pick up 6. Smaller than 13, 12, 11... but BIGGER than 5.
- **Action:** It slides past 13, 12, and 11, then settles right after 5.
- **Final Hand:** `[5, 6, 11, 12, 13]` ✅ **Perfectly Sorted!**

---

## 🧠 Why is it called "Insertion" Sort?
Because you take an item and **Insert** it into its correct position within the already-sorted part of the list. It's exactly how humans naturally sort things!

---


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

