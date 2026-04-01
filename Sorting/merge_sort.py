"""
================================================================================
CONCEPTS AND THEORY: MERGE SORT (THE 'DIVIDE AND CONQUER' WAY)
================================================================================

--- TIME COMPLEXITY ANALYSIS ---
- BEST CASE:    O(n log n) (The list is already sorted)
- AVERAGE CASE: O(n log n) 
- WORST CASE:   O(n log n) 
--------------------------------
- SPACE COMPLEXITY: O(n) (For storing the new merged lists)

STATUS: LINKED (Requires merge_two_sorted_lists helper function)
================================================================================

1. WHAT IS IT?
   Merge Sort is a very clever and fast way to sort a list. It follows 
   the 'Divide and Conquer' rule: "If a problem is too big, break it 
   into smaller pieces until they are tiny and easy to solve."

2. THE TWO MAIN STEPS:
   - 1. **DIVIDE**: Keep cutting the list in half until every piece 
        is just one single number (a single number is already 'sorted').
   - 2. **MERGE**: Take two sorted halves and zip them together into 
        one big sorted list. This is the 'magic' part!

3. WHY IS IT SO FAST?
   Merging two lists that are *already* sorted is extremely efficient. 
   Unlike Selection/Insertion Sort, Merge Sort doesn't waste time 
   re-checking the same numbers over and over.
   - Time Complexity: **O(n log n)**. This makes it perfect for sorting 
     millions of items quickly.

4. REAL LIFE EXAMPLE:
   Imagine you have **100 Exam Papers** to sort by student name. 
   Instead of doing it alone, you split the stack:
   - Give 50 to a friend, keep 50 yourself. 
   - Each of you sorts your stack (maybe you split them even further!).
   - Now you have two sorted stacks. 
   - You look at the TOP paper of each stack and pick the one that 
     comes first alphabetically. You keep doing this until all papers 
     are in one big sorted stack!
================================================================================
"""

def merge(L, R): # L: left list, R: right list
    """
    Zips two sorted lists into one unified sorted list.
    """
    n1, n2 = len(L), len(R) # n1, n2: lengths of L and R
    res, i, j = [], 0, 0 # res: result list, i/j: pointers
    
    # 1. Compare elements from both lists while both have items
    while i < n1 and j < n2: # Scan both L and R
        if L[i] <= R[j]: # If L item is smaller
            res.append(L[i]) # add L item to res
            i += 1 # advance L pointer
        else: # Otherwise R item is smaller
            res.append(R[j]) # add R item to res
            j += 1 # advance R pointer
            
    # 2. Append any leftover elements from L and R
    return res + L[i:] + R[j:] # Merge remaining elements

def merge_sort(A): # A: input list
    """
    Recursively splits the list and merges it back in sorted order.
    """
    n = len(A) # n: length of list
    
    # 1. Base case: 0 or 1 element is already sorted
    if n <= 1: 
        return A
        
    # 2. Divide: Split the list at the midpoint
    m = n // 2 # m: midpoint index
    
    # 3. Recurse: Sort the Left and Right halves
    L = merge_sort(A[:m]) # L: sorted left half
    R = merge_sort(A[m:]) # R: sorted right half
    
    # 4. Merge: Combine the two sorted halves
    return merge(L, R) # Return combined result

# --- START OF PROGRAM ---

# L1: input list
L1 = [38, 27, 43, 3, 9, 82, 10]

print("Welcome to Merge Sort!")
print(f"Original messy list: {L1}")

# Run process
ans = merge_sort(L1)

print(f"\nFinal sorted list:   {ans} ✅")
