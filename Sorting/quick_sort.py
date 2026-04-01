"""
================================================================================
CONCEPTS AND THEORY: QUICK SORT (THE 'PICK A PIVOT' METHOD)
================================================================================

--- TIME COMPLEXITY ANALYSIS ---
- BEST CASE:    O(n log n) (When pivot splits the list perfectly in half)
- AVERAGE CASE: O(n log n) 
- WORST CASE:   O(n^2) (When pivot is the smallest or largest element)
--------------------------------
- SPACE COMPLEXITY: O(log n) (For the recursive search depth)

STATUS: LINKED (Requires partition helper function)
================================================================================

1. WHAT IS IT?
   Quick Sort is one of the fastest and most efficient ways to sort 
   a list. It's often used by computers in the real world because it's 
   very quick and doesn't need much extra memory.

2. THE CORE IDEA (PARTITIONING):
   Instead of just splitting the list in half like Merge Sort, Quick Sort:
   - 1. Picks one number as a **PIVOT** (like a middle point).
   - 2. Shuffles all other numbers so that **Smaller** ones are on 
        the left and **Larger** ones are on the right. 
   - 3. Now the Pivot is in its **exact correct spot** in the final list!
   - 4. We then 'Quick Sort' the left group and the right group.

3. WHY PICK A PIVOT?
   The pivot acts as a benchmark. Once the partition is done, we KNOW 
   that everything on its left belongs on its left, and everything 
   on its right belongs on its right.

4. TIME COMPLEXITY:
   - Average Case: **O(n log n)**. This is super fast.
   - Worst Case: **O(n^2)** if we pick a really bad pivot (like if the list 
     was already sorted!).

5. REAL LIFE EXAMPLE:
   Think of **Sorting a Line of students**. You pick one student (say, Alex) 
   and stand them in the middle of a room. 
   - You say: "If you are shorter than Alex, stand on his left. 
     If you are taller, stand on his right."
   - Now, Alex is in the perfect spot! Even if the groups on his left 
     and right aren't sorted yet, Alex himself is finished.
   - You then repeat this for the group on his left and the group on 
     his right. Eventually, everyone is in height order!
================================================================================
"""

def partition(L, low, high): # L: list, low/high: range indices
    """
    Rearranges the list around a pivot element.
    Returns the final position of the pivot.
    """
    # 1. Pick the first element as the pivot
    p = L[low] # p: pivot value
    
    # 2. i: tracks the end of the 'smaller elements' section
    i = low 
    
    # 3. Scan through the list from low + 1 to high
    for j in range(low + 1, high + 1): # j: current scan index
        # 4. If current element is less than or equal to pivot:
        if L[j] <= p:
            # 5. Move it into the 'smaller elements' section
            i += 1 # increment boundary
            L[i], L[j] = L[j], L[i] # swap L[i] and L[j]
            
    # 6. Place the pivot into its final correct position
    L[low], L[i] = L[i], L[low] # swap pivot with the boundary item
    
    # 7. Return the pivot's final index
    return i

def quick_sort(L, low, high): # L: list, low/high: range
    """
    Recursively sorts the list using partitioning.
    """
    # 1. Base case: If start and end point cross, the segment is sorted
    if low < high:
        # 2. Partition the list and get the pivot's final spot
        pi = partition(L, low, high) # pi: pivot index
        
        # 3. Recursively sort elements before and after the pivot
        quick_sort(L, low, pi - 1) # sort left half
        quick_sort(L, pi + 1, high) # sort right half
        
    # 4. Return the sorted list L
    return L

# --- START OF PROGRAM ---

# L1: messy list of numbers
L1 = [10, 80, 30, 90, 40, 50, 70]

print("Welcome to Quick Sort!")
print(f"Original messy list: {L1}")

# Run process with first and last indices
ans = quick_sort(L1, 0, len(L1) - 1)

print(f"\nFinal sorted list:   {ans} ✅")
