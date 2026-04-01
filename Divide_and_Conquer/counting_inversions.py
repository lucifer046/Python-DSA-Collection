"""
================================================================================
CONCEPTS AND THEORY: COUNTING INVERSIONS (THE 'DISAGREEMENT' MEASURE)
================================================================================

--- TIME COMPLEXITY ANALYSIS ---
- BEST CASE:    O(n log n) (Even if list is sorted)
- AVERAGE CASE: O(n log n)
- WORST CASE:   O(n log n)
--------------------------------
- SPACE COMPLEXITY: O(n) (For sorting temporary lists)
================================================================================

1. WHAT IS AN INVERSION?
   In a sorted list, every smaller number comes before every larger number. 
   An **Inversion** happens when a larger number appears *before* a smaller 
   number. 
   Example: In the list `[2, 4, 1, 3]`, 4 comes before 1. That's an inversion!

2. THE DIVIDE AND CONQUER STRATEGY:
   We can find inversions by checking every pair (slow, O(n^2)), or we can 
   use a clever trick based on **Merge Sort**:
   - 1. Split the list in half.
   - 2. Count inversions in the **Left Half**.
   - 3. Count inversions in the **Right Half**.
   - 4. Count 'Split Inversions' while merging the two halves together.

3. THE MERGE TRICK:
   During the merge, if we pick a number from the **Right Half** because it's 
   smaller than the current number in the **Left Half**, it must be 
   smaller than *all* the numbers remaining in the Left Half. 
   We add that 'remaining count' to our total inversions!

4. WHY IS IT USEFUL?
   - **Recommendation Engines**: Amazon or Netflix can see how 'inverted' 
     your movie rankings are compared to other users to find people with 
     similar tastes.
   - **Sorting Analysis**: Tells us exactly how 'out of order' a list is.

5. REAL LIFE EXAMPLE:
   Think of **RANKING TOP 5 MOVIES**. 
   - You rank them: [Avatar, Batman, Cars, Dumbo, ET]
   - Your friend ranks them: [Cars, Avatar, Batman, ET, Dumbo]
   - The number of inversions tells you how much you **disagree**. 
     If the count is 0, you agree perfectly. If the count is high, 
     your tastes are opposites!
================================================================================
"""

def merge_and_count(L, R):
    """
    Combines two sorted lists and counts 'Split Inversions'.
    L: left sorted list, R: right sorted list
    """
    n1, n2 = len(L), len(R) # n1, n2: lengths of L and R
    res, i, j, c = [], 0, 0, 0 # res: merged list, i/j: pointers, c: inversion count
    
    # 1. Loop until we finish at least one half
    while i < n1 and j < n2: # Scan both halves
        # 2. If left item is smaller (Correct Order)
        if L[i] <= R[j]:
            res.append(L[i]) # add left item
            i += 1 # move left pointer
        # 3. If right item is smaller (An Inversion!)
        else:
            res.append(R[j]) # add right item
            j += 1 # move right pointer
            # 4. Add all remaining elements in L to inversion count
            c += (n1 - i) # count split inversions
            
    # 5. Append any leftover elements from L and R
    return res + L[i:] + R[j:], c

def count_inversions(A):
    """
    Recursively counts inversions in list A.
    A: input list
    """
    n = len(A) # n: length of list
    
    # 1. Base case: 0 or 1 element means no inversions
    if n <= 1:
        return A, 0 # return list and zero count
    
    # 2. Split: Divide the list into two halves
    m = n // 2 # m: midpoint index
    
    # 3. Recurse: Solve for Left and Right halves
    L, cL = count_inversions(A[:m]) # L: sorted left, cL: left inversions
    R, cR = count_inversions(A[m:]) # R: sorted right, cR: right inversions
    
    # 4. Merge: Combine sorted halves and count split inversions
    B, cB = merge_and_count(L, R) # B: final sorted list, cB: split inversions
    
    # 5. Total: Sum all inversion types
    return B, cL + cR + cB # result and total count

# ================================================================================
# VERSION 2: THE MOST COMPACT & SHORTEST WAY
# ================================================================================

def fast_count(A):
    """
    Compact recursive inversion counter.
    A: array list
    """
    if len(A) <= 1: return A, 0
    m = len(A) // 2 # m: middle
    L, cL = fast_count(A[:m]) # L: left
    R, cR = fast_count(A[m:]) # R: right
    res, i, j, cS = [], 0, 0, 0 # cS: split count
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            res.append(L[i]); i += 1
        else:
            res.append(R[j]); j += 1
            cS += (len(L) - i) # add remaining left items
    return res + L[i:] + R[j:], cL + cR + cS

# --- START OF PROGRAM ---

# L1: input list
L1 = [2, 4, 3, 1, 5]

print("Welcome to the Inversion Counter!")
print(f"Original List: {L1}")

# Run calculation
sorted_list, total_count = count_inversions(L1)

print(f"\nTotal Inversions: {total_count}")
print(f"Sorted Result:    {sorted_list}")

# --- TEST SHORTEST VERSION ---
_, short_count = fast_count(L1)
print(f"Compact Count Result: {short_count}")
