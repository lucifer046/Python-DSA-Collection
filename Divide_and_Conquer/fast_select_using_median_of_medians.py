"""
================================================================================
CONCEPTS AND THEORY: FAST SELECT USING MEDIAN OF MEDIANS (THE 'GUARANTEED' PIVOT)
================================================================================

--- TIME COMPLEXITY ANALYSIS ---
- BEST CASE:    O(n) (Linear time for pivot selection)
- AVERAGE CASE: O(n) 
- WORST CASE:   O(n) (Guarantees linear time for QuickSelect! )
--------------------------------
- SPACE COMPLEXITY: O(n) (Recursion depth and storage for block medians)

STATUS: INDEPENDENT (Contains MoM and a 'Guaranteed' QuickSelect)
================================================================================

1. WHAT IS MEDIAN OF MEDIANS (MoM)?
   Standard QuickSelect is fast but has one nightmare: if you always pick 
   the worst pivot (the smallest or biggest item), it becomes SLOW (O(n^2)).
   MoM is a "Pivot Hunter" that guaranteed to find a median that is close 
   to the REAL middle of the list every single time!

2. HOW IT WORKS (THE 'BLOCK' STRATEGY):
   - 1. Split the list into groups of **5**.
   - 2. Find the median of each small group (easy!).
   - 3. Collect all those mini-medians into a new list.
   - 4. Recursively find the median of *that* list.
   - 5. Use that "Median of Medians" as your pivot!

3. WHY GROUPS OF 5?
   Math proofs show that using 5 ensures your pivot will always be better 
   than at least 30% of the list. This "30% guarantee" is exactly what 
   forces the algorithm to stay linear (O(n)) even in the worst case!

4. REAL LIFE EXAMPLE:
   Think of **VOTING IN A LARGE COUNTRY**. 
   Instead of counting 1 billion votes at once:
   - 1. Divide voters into "Blocks" (Districts).
   - 2. Find the representative (Median) of each District.
   - 3. Those representatives then meet to decide the final result.
   This "Layered" approach is stable and much harder to "break" than 
   picking one random voter from the whole country.
================================================================================
"""

def moms(L):
    """
    Finds the median of medians for a stable pivot.
    L: list of elements
    """
    # 1. Base case: If list is small, sort and return middle
    if len(L) <= 5: # Small size
        return sorted(L)[len(L)//2] # Returns median
    
    # 2. Split list into small blocks of 5
    M = [] # M: list of block medians
    for i in range(0, len(L), 5): # i: block start index
        # 3. Extract block, sort it, and find its median
        X = L[i : i+5] # X: current block
        X.sort()
        M.append(X[len(X)//2]) # Add median of block to M
        
    # 4. Recursively find the median of the collected medians
    return moms(M)


def partition(L, low, high, v):
    """
    Standard Partition around a specific value 'v'.
    L: list, low: start index, high: end index, v: pivot value
    """
    # 1. Search for the position of the pivot value 'v'
    for idx in range(low, high + 1): # idx: iterator index
        if L[idx] == v:
            # 2. Swap the pivot value to the start position
            L[low], L[idx] = L[idx], L[low]
            break
            
    # 3. Standard partition logic using the pivot at L[low]
    p = L[low] # p: pivot value
    i = low    # i: boundary index for smaller elements
    
    # 4. Loop through the range to partition elements
    for j in range(low + 1, high + 1): # j: current scan index
        # 5. If current item is less than or equal to pivot
        if L[j] <= p:
            # 6. Increment boundary and swap
            i += 1
            L[i], L[j] = L[j], L[i]
            
    # 7. Move pivot into its final correct place
    L[low], L[i] = L[i], L[low]
    
    # 8. Return pivot location index
    return i

def fast_select(L, low, high, k):
    """
    Fast Select (QuickSelect) with MoM pivot.
    L: list, low/high: search range, k: target index
    """
    # 1. Validation: range must be valid
    if low <= high:
        # 2. Use MoM to get a guaranteed 'good enough' pivot
        v = moms(L[low : high + 1]) # v: pivot value
        
        # 3. Partition around the chosen pivot
        pos = partition(L, low, high, v) # pos: pivot index
        
        # 4. Check if current pivot is the k-th smallest
        if k == pos:
            return L[pos] # return k-th element
            
        # 5. Recurse into the side containing target k
        elif k < pos:
            return fast_select(L, low, pos - 1, k) # search left half
        else:
            return fast_select(L, pos + 1, high, k) # search right half
            
    return None

# --- START OF PROGRAM ---

# L: input list, k: target index
L = [4, 3, 5, 2, 6, 1, 8]
k = 2

print("Welcome to the Median of Medians Explorer!")
print(f"Finding rank {k} in: {L}")

# Run calculation using a copy of the list
ans = fast_select(L.copy(), 0, len(L) - 1, k)

print(f"\nResult: {ans} ✅")
