"""
================================================================================
CONCEPTS AND THEORY: INSERTION SORT (THE 'SLOT-IN' METHOD)
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

def insertion_sort(unsorted_list):
    """
    Sorts a list by picking each item and sliding it left until it 
    finds its correct position.
    """
    # 1. Measure how many numbers we need to sort
    list_length = len(unsorted_list)
    
    # 2. Base case: If the list is empty, return it as is
    if list_length < 1:
        return(unsorted_list)
    
    # 3. Outer Loop: Go through every single number in the list
    for current_index in range(list_length):
        
        # 4. 'shifting_index' tracks our current number as it slides left
        shifting_index = current_index
        
        # 5. Inner Loop (Slide Left): While our current number is NOT at 
        # the very start (index 0) AND is SMALLER than the number to its left:
        while(shifting_index > 0 and unsorted_list[shifting_index] < unsorted_list[shifting_index - 1]):
            
            # 6. Swap! Since our current number is smaller, exchange it 
            # with the one to its left to move it one step closer to the front.
            (unsorted_list[shifting_index], unsorted_list[shifting_index - 1]) = \
            (unsorted_list[shifting_index - 1], unsorted_list[shifting_index])
            
            # 7. Move our tracker one step to the left to follow the number we just swapped
            shifting_index = shifting_index - 1
            
    # Give back the final, fully sorted list!
    return(unsorted_list)

# --- START OF PROGRAM ---

# 1. Our messy list of numbers
my_numbers = [12, 11, 13, 5, 6]

print("Welcome to Insertion Sort!")
print(f"Original messy list: {my_numbers}")

# Run the sorting process
sorted_result = insertion_sort(my_numbers)

print(f"\nFinal sorted list:   {sorted_result}")
