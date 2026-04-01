<!-- +------------------------------------------------------+ -->
<!-- |     QUICKSELECT — FINDING THE K-TH SMALLEST      | -->
<!-- +------------------------------------------------------+ -->
# QuickSelect — Finding the K-th Smallest Element

## What is QuickSelect?

Imagine you have a **stack of 1,000 ungraded exams**. You want to find the **3rd highest mark** in the class. 

Do you need to sort all 1,000 exams from highest to lowest? **No!** That would be a waste of time. You only need to find the exam that would be in the 3rd spot if they *were* sorted.

> **Simple Definition:** QuickSelect is a "selection algorithm" based on **QuickSort**. Instead of sorting the entire list, it only recurses into the partition that contains the target element.

---

## Why Use This Over Sorting?

- **Sorting ($O(N \log N)$):** If you sort first and then pick the $k$-th element, you are doing work for the entire list.
- **QuickSelect ($O(N)$):** On average, QuickSelect is **linear**. It effectively "throws away" half of the list at every step!

---

## How It Works (The Partition Trick)

Like QuickSort, it uses a **Pivot**.

1. **Pick a Pivot:** Choose a random element (e.g., $X$).
2. **Partition:** Move everything smaller than $X$ to the left, and everything larger than $X$ to the right.
3. **Check the Index:**
   - Did the Pivot land on exactly the index you were looking for? **Return it! 🎉**
   - Is your target index in the Left half? **Search only the Left.**
   - Is it in the Right half? **Search only the Right.**

---

## Visualizing the Search

```
   Target: 2nd Smallest (Index 2)
   Original: [4, 3, 5, 2, 6, 1, 8]
   
   Pivot = 4
   Partition: [3, 2, 1, (4), 6, 5, 8]
                         ^ 
                         | Pivot is at index 3. 
                           Target (index 2) is on the LEFT. 
                           THROW AWAY [4, 6, 5, 8] 🗑️
   
   Searching only in [3, 2, 1]:
   Pivot = 3
   Partition: [2, 1, (3)]
                       ^
                       | Pivot is at index 2. 
                         MATCH! Return 3 ✅
```

---

## Comparing Algorithms

| Algorithm | Complexity (Avg) | Memory | Best Use-Case |
| :--- | :--- | :--- | :--- |
| **QuickSort** | $O(N \log N)$ | $O(\log N)$ | You need the **entire list** in order. |
| **QuickSelect**| **$O(N)$** | **$O(1)$** | You only need **one specific rank**. |

---

## Key Takeaways

1. **Efficiency:** Fastest way to find a median or a specific percentile.
2. **Dividing:** Uses the same "Partition" logic as QuickSort.
3. **Discarding:** In every step, it narrows down the search space.
4. **Performance:** Expect linear time ($O(N)$), but watch out for the $O(N^2)$ worst case!
5. **Real-Life Use:** Finding the median of a dataset, calculating percentiles, and selecting the top $k$ items.
