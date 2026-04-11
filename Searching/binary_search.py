"""
================================================================================
CONCEPTS AND THEORY: BINARY SEARCH (DIVIDE AND CONQUER)
================================================================================

--- TIME COMPLEXITY ANALYSIS ---
- BEST CASE:    O(1) (Target is found exactly at the first middle point)
- AVERAGE CASE: O(log n) 
- WORST CASE:   O(log n) (Searching until only one item remains)
--------------------------------
- SPACE COMPLEXITY: O(1) (Iterative) or O(log n) (Recursive call stack)

STATUS: INDEPENDENT (Contains both Iterative and Recursive versions)
================================================================================

1. WHAT IS IT?
   Binary Search is a super-fast way to find one specific item in a 
   list that is already **SORTED**. 

2. THE CORE IDEA (DIVIDE AND CONQUER):
   Instead of checking every single item one-by-one starting from the 
   beginning (which is slow!), we jump straight to the **MIDDLE**. 
   - If our target is smaller than the middle item: We throw away the 
     right half and only search the left.
   - If our target is larger: We throw away the left half and only 
     search the right.
   We keep cutting the list in HALF until we find our item (or run out of list).

3. THE CRITICAL REQUIREMENT:
   Binary Search ONLY works if the list is already sorted (e.g., [1, 5, 8, 12]). 
   If it's messy, we have to sort it first!

4. WHY IS IT SO FAST? (The Efficiency):
   With every single step, you throw away 50% of the remaining search area.
   - Even with 1 BILLION items, Binary Search can find any number in 
     just **30 checks**!
   - Linear Search (one by one) could take up to 1,000,000,000 checks.

5. TIME COMPLEXITY:
   - Search Time: **O(log n)**. Matches the power of dividing in half.

6. REAL LIFE EXAMPLE:
   Think of finding a name in a **Physical Phonebook**. You don't start 
   at page 1 and read every name. You open the book in the middle. 
   If you see 'M' but you want 'B', you flip to the middle of the first 
   half. You keep doing this until you find the exact page!

7. ITERATIVE vs RECURSIVE:
   - **Iterative**: Uses a simple 'while loop' to keep cutting the list.
   - **Recursive**: The function calls its smaller self repeatedly until 
     the answer is found.
================================================================================
"""

# ================================================================================
# VERSION 1: ITERATIVE IMPLEMENTATION (Using a While Loop)
# ================================================================================

def search_iterative(L, t):
    """
    Finds target 't' in sorted list 'L' using a loop.
    L: sorted list, t: target value
    """
    # 1. l/r: search boundaries (left index and right index)
    l, r = 0, len(L) - 1 # l: start, r: end
    
    # 2. Logic: repeatedly narrow down the range until the pointers meet
    while l <= r: # l: left pointer, r: right pointer
        
        # 3. m: find the exact midpoint index to divide the search territory
        m = (l + r) // 2 # m: midpoint index
        
        # 4. Check target against midpoint value L[m]
        # if target is smaller, ignore everything on the right
        if L[m] > t:
            r = m - 1 # move right boundary inwards
            
        # 5. If target is larger, ignore everything on the left
        elif L[m] < t:
            l = m + 1 # move left boundary inwards
            
        # 6. Target found exactly at the middle!
        else:
            return m # return the index m where t was found
            
    # 7. Return False if target is never located
    return False

# ================================================================================
# VERSION 2: RECURSIVE IMPLEMENTATION (Function calling itself)
# ================================================================================

def search_recursive(L, t, l, r):
    """
    Finds target 't' in sorted list 'L' using recursion.
    L: sorted list, t: target, l/r: current search boundaries
    """
    # 1. Base case: Check if the search territory has disappeared
    if r < l: 
        return False # target t is not in list L
        
    # 2. m: calculate midpoint index for this recursive step
    m = (l + r) // 2 # m: middle index
    
    # 3. Success condition: target located in the middle
    if t == L[m]:
        return m # return resulting index
        
    # 4. Binary split: decide which half to recursively explore
    # If target is smaller than middle, search the left half territory
    if t < L[m]:
        return search_recursive(L, t, l, m - 1) # dive left
        
    # 5. Otherwise, search the right half territory
    else:
        return search_recursive(L, t, m + 1, r) # dive right

# --- START OF PROGRAM ---

# L1: sorted sample list, t1: target number to find
L1 = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
t1 = 23

print("Binary Search Algorithm Simulator (Search by Halving)!\n")
print(f"Sorted List: {L1}")
print(f"Target Selection: {t1}\n")

# Run iterative version
res1 = search_iterative(L1, t1)
print(f"Iterative Search: Found at Index {res1} ✅")

# Run recursive version
res2 = search_recursive(L1, t1, 0, len(L1) - 1)
print(f"Recursive Search: Found at Index {res2} ✅")

print("\nSearch operation successful! ")
