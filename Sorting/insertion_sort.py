"""
================================================================================
CONCEPTS AND THEORY: INSERTION SORT (THE 'SLOT-IN' METHOD)
================================================================================

--- TIME COMPLEXITY ANALYSIS ---
- BEST CASE:    O(n) (When the list is ALREADY sorted!)
- AVERAGE CASE: O(n^2) 
- WORST CASE:   O(n^2) (When the list is in reverse order)
--------------------------------
- SPACE COMPLEXITY: O(1) (In-place sorting)

STATUS: INDEPENDENT
================================================================================

1. WHAT IS IT?
   Insertion Sort is a very natural way to sort items. It's almost 
   exactly how most people sort their cards in a game!

2. THE CORE IDEA (SLIDING INTO PLACE):
   - You take one number at a time and decide where it belongs in 
     the already-sorted part of the list to its left. 
   - You "insert" it into its correct spot by shifting the larger 
     numbers to the side.

3. ALGORITHM STEPS:
   - 1. Consider the first number sorted by itself.
   - 2. Pick the second number and compare it with the first. 
   - 3. If it's smaller, 'slide' it to the left. 
   - 4. Pick the third number and slide it left until it hits a 
        number that is smaller than it.
   - 5. Repeat for all numbers in the list.

4. IS IT EFFICIENT?
   Like Selection Sort, it takes O(n^2) for messy lists. 
   BUT, if the list is ALMOST sorted, it's very FAST! (O(n) best-case).

5. REAL LIFE EXAMPLE:
   Think of **Sorting your Cards in a game**. You have a stack of cards. 
   You pick the first card (say, a 5) and hold it. Then you pick the 
   next card (say, a 2). Obviously, 2 is smaller than 5, so you 
   slide the 2 into the slot BEFORE the 5. Then you pick a 7 and 
   leave it after the 5. You keep sliding each new card into 
   its correct 'slot' in your hand!
================================================================================
"""

def insertion_sort(L):
    """
    Sorts a list by picking items and sliding them into their correct slots.
    L: input list of items
    """
    # n: length of the list
    n = len(L)
    
    # 1. Base case: Check if list needs sorting
    if n < 1: 
        return L
    
    # 2. Outer loop: i represents the current item we want to 'insert'
    for i in range(n): # i: index of the current item to sort
        
        # 3. j: pointer to track the item as it slides left
        j = i 
        
        # 4. Inner loop: Slide item left while it's smaller than its neighbor
        while j > 0 and L[j] < L[j - 1]: # j > 0: ensure we don't go out of bounds
            
            # 5. Swap the current item with the one to its left
            L[j], L[j - 1] = L[j - 1], L[j] # swap L[j] and L[j-1]
            
            # 6. Move our tracker j one step to the left to follow the item
            j -= 1 # move pointer left
            
    # 7. Return the final sorted list
    return L

# --- START OF PROGRAM ---

# L1: unsorted numbers
L1 = [12, 11, 13, 5, 6]

print("Welcome to Insertion Sort!")
print(f"Original messy list: {L1}")

# Run process
ans = insertion_sort(L1)

print(f"\nFinal sorted list:   {ans} ✅")
