"""
================================================================================
CONCEPTS AND THEORY: QUICKSELECT (FINDING THE K-TH SMALLEST ELEMENT)
================================================================================

--- TIME COMPLEXITY ANALYSIS ---
- BEST CASE:    O(n) (Pivot is the median, found in the first division)
- AVERAGE CASE: O(n) (Linear time expected!)
- WORST CASE:   O(n^2) (If the pivot is always the largest or smallest element)
--------------------------------
- SPACE COMPLEXITY: O(1) or O(n) (Depending on the recursion stack depth)

STATUS: INDEPENDENT (Contains both a full and a compact implementation)
================================================================================

1. WHAT IS QUICKSELECT?
   Imagine you have a class of 1,000 students and you want to find the 
   3rd tallest student. Do you need to sort the WHOLE class from tallest 
   to shortest? NO! 
   QuickSelect is a "smart sorting" algorithm that only sorts the 
   half of the list that contains the answer you are looking for.

2. HOW IT WORKS (THE 'PARTITION' TRICK):
   Like QuickSort, we pick a **PIVOT** (a random student).
   - Students shorter than the pivot go Left.
   - Students taller than the pivot go Right.
   Now, we check: Is the 3rd tallest rank in the Left side or the Right side?
   We **ignore** the side that doesn't contain the answer and REPEAT 
   the process on the other side!

3. WHY USE THIS OVER FULL SORTING?
   - **QuickSort** (Sorting) takes O(n log n).
   - **QuickSelect** (Selection) only takes O(n) on average. 
   If you have a billion items and only want the 1,000th one, QuickSelect 
   is massively faster because it throws away half the work at every step!

4. REAL LIFE EXAMPLE:
   Think of **AN UNORDERED PILE OF PAPERS**. 
   You want the 5th highest mark. You pick a random paper (Pivot = 60).
   You split the pile into "Under 60" and "Above 60". 
   If the "Above 60" pile has 10 papers, you know your 5th highest mark 
   is somewhere in that pile! You throw the "Under 60" pile in the bin 
   and keep searching.
================================================================================
"""

def get_pivot(L):
    """
    Returns the first element as the pivot.
    L: list of elements
    """
    # Return the first item
    return L[0]

def partition(L, low, high, pvt):
    """
    Moves elements smaller than 'pvt' to the left.
    L: list, low: start index, high: end index, pvt: pivot value
    """
    # 1. Find where the chosen 'pvt' is currently 
    for idx in range(low, high + 1): # idx: iterator index
        if L[idx] == pvt:
            # 2. Move the pivot to the start position
            L[low], L[idx] = L[idx], L[low]
            break
            
    # 3. Standard partition around the pivot at L[low]
    p = L[low] # p: pivot value
    i = low    # i: boundary index for smaller elements
    
    # 4. Scan through the list from low + 1 to high
    for j in range(low + 1, high + 1): # j: current scan index
        # 5. If current item is smaller than or equal to pivot
        if L[j] <= p:
            # 6. Increment boundary and swap
            i += 1
            L[i], L[j] = L[j], L[i]
            
    # 7. Move pivot to its final correct position
    L[low], L[i] = L[i], L[low]
    
    # 8. Return pivot position
    return i

def quick_select(L, low, high, k):
    """
    Finds k-th smallest element (index k).
    L: list, low: start, high: end, k: target index
    """
    # 1. Base case: If the search range is valid
    if low <= high:
        # 2. Pick a pivot from the current range
        v = get_pivot(L[low : high + 1]) # v: pivot value
        
        # 3. Partition around the chosen pivot
        pos = partition(L, low, high, v) # pos: resulting pivot index
        
        # 4. If target k is exactly the pivot's position
        if k == pos:
            return L[pos] # return the result
            
        # 5. If target k is on the left side
        elif k < pos:
            return quick_select(L, low, pos - 1, k) # search left half
            
        # 6. If target k is on the right side
        else:
            return quick_select(L, pos + 1, high, k) # search right half
            
    return None

# ================================================================================
# VERSION 2: THE MOST COMPACT & SHORTEST WAY
# ================================================================================

def fast_select(L, k):
    """
    Compact version using list comprehensions.
    L: list, k: index
    """
    if len(L) == 1: return L[0]
    p = L[0] # p: pivot
    # l: left, m: middle, r: right
    l = [x for x in L if x < p]
    m = [x for x in L if x == p]
    r = [x for x in L if x > p]
    
    if k < len(l):
        return fast_select(l, k)
    elif k < len(l) + len(mid):
        return m[0]
    else:
        return fast_select(r, k - len(l) - len(m))

# --- START OF PROGRAM ---

# L: input list, k: target index (2 = 3rd smallest)
L = [4, 3, 5, 2, 6, 1, 8]
k = 2

print("Welcome to the QuickSelect Algorithm!")
print(f"Finding rank {k} in: {L}")

# Run calculation on a copy of the list
ans = quick_select(L.copy(), 0, len(L) - 1, k)

print(f"\nResult: {ans} ✅")
