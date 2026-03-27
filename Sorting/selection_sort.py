"""
================================================================================
CONCEPTS AND THEORY: SELECTION SORT (SORTING BY REPEATED PICKING)
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

def selection_sort(unsorted_list):
    """
    Sorts a list by repeatedly picking the smallest item and putting it in front.
    """
    # 1. Measure the length of the list so we know when to stop
    list_length = len(unsorted_list)
    
    # 2. Base case: If the list is empty, there is nothing to sort!
    if list_length < 1:
        return(unsorted_list)
    
    # 3. Outer Loop: This marks the 'Starting Gate' for our search.
    # Everything to the left of this index is ALREADY sorted.
    for current_start_index in range(list_length):
        
        # 4. Assume the number at the 'Starting Gate' is the smallest for now
        smallest_index_found = current_start_index
        
        # 5. Inner Loop: Start searching from the next position all the way to the end
        for search_index in range(current_start_index + 1, list_length):
            
            # 6. Check: Is the number at our 'search_index' smaller than our current smallest?
            if unsorted_list[search_index] < unsorted_list[smallest_index_found]:
                # If yes, update our tracker to point to this new smaller number
                smallest_index_found = search_index
        
        # 7. Once we finish scanning the whole unsorted part, we have the TRULY smallest.
        # Now, swap it with the number at our 'Starting Gate' (current_start_index).
        (unsorted_list[current_start_index], unsorted_list[smallest_index_found]) = \
        (unsorted_list[smallest_index_found], unsorted_list[current_start_index])
        
    # Give back the final, fully sorted list!
    return(unsorted_list)

# --- START OF PROGRAM ---

# 1. Our messy, unsorted list of numbers
my_numbers = [64, 25, 12, 22, 11]

print("Welcome to Selection Sort!")
print(f"Original messy list: {my_numbers}")

# Run the sorting process
sorted_result = selection_sort(my_numbers)

print(f"\nFinal sorted list:   {sorted_result}")
