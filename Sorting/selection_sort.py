"""
================================================================================
CONCEPTS AND THEORY: SELECTION SORT (SORTING BY REPEATED PICKING)
================================================================================

--- TIME COMPLEXITY ANALYSIS ---
- BEST CASE:    O(n^2) (Always scans the entire unsorted part)
- AVERAGE CASE: O(n^2)
- WORST CASE:   O(n^2)
--------------------------------
- SPACE COMPLEXITY: O(1) (In-place sorting)

STATUS: INDEPENDENT
================================================================================

1. WHAT IS IT?
   Selection Sort is a simple way to organize a messy list of numbers 
   from smallest to largest. 

2. THE CORE IDEA:
   Imagine your list is split into two halves:
   - A **SORTED** half (initially empty).
   - An **UNSORTED** half (initially the whole list).
   
   Every step, you scan through the entire **UNSORTED** part, find the 
   SINGLE SMALLEST number, and move it into the **SORTED** part. 

3. ALGORITHM STEPS:
   - 1. Start at the first position in the list.
   - 2. Look at all the numbers to the right and find the absolute smallest one.
   - 3. Swap the first number with this 'smallest' one.
   - 4. Now the first number is officially 'sorted'.
   - 5. Move to the second position and repeat until you finish the whole list.

4. IS IT EFFICIENT?
   Not really! Because we have to scan the whole unsorted part again and 
   again, it gets very slow for large lists. 
   - Time Complexity: **O(n^2)** because of the nested loops.

5. REAL LIFE EXAMPLE:
   Think of **Sorting a Hand of Cards**. You look at all the cards in your 
   hand, find the smallest card (say, an Ace), and move it to the very left. 
   Then you look at the remaining cards, find the next smallest, and move 
   it next to the Ace. By the time you reach the last card, your whole hand 
   is sorted!
================================================================================
"""

def selection_sort(L):
    """
    Sorts a list by picking the smallest item and putting it at the front.
    L: input list of numbers
    """
    # n: length of the list
    n = len(L)
    
    # 1. Base case: If list is empty, nothing to sort
    if n < 1: 
        return L
    
    # 2. Outer loop: i represents the start of the current 'unsorted section'
    for i in range(n): # i: current sorted boundary index
        
        # 3. Assume the element at the current boundary is the minimum
        m = i # m: index of the minimum element found so far
        
        # 4. Inner loop: j scans the remaining unsorted part of the list
        for j in range(i + 1, n): # j: search index
            
            # 5. If we find a value smaller than our current minimum:
            if L[j] < L[m]:
                # 6. Update m to point to this new smallest value
                m = j # m tracks the smallest item's index
        
        # 7. Swap the smallest value found with the element at position i
        # L[i] is now in its correct sorted position!
        L[i], L[m] = L[m], L[i] # In-place swap
        
    # 8. Return the fully sorted list L
    return L

# --- START OF PROGRAM ---

# L1: messy list for sorting
L1 = [64, 25, 12, 22, 11]

print("Welcome to Selection Sort!")
print(f"Original messy list: {L1}")

# Run sorting process
ans = selection_sort(L1)

print(f"\nFinal sorted list:   {ans} ✅")
