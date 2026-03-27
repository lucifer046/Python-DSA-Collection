"""
================================================================================
CONCEPTS AND THEORY: QUICK SORT (THE 'PICK A PIVOT' METHOD)
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

# This helper function does the 'Shuffling' or 'Partitioning' work.
# It places the pivot in the correct spot and moves smaller numbers to its left.
def organize_around_pivot(number_list, start_point, end_point):
    """
    Partitions the list so that smaller numbers end up on one side 
    and larger ones on the other.
    """
    # 1. We pick the first number in the list segment as our 'Pivot Benchmark' 
    pivot_value = number_list[start_point]
    
    # 2. 'smaller_elements_last_idx' tracks where the part for smaller numbers ends
    # Initially, we set it right at our start point
    smaller_elements_last_idx = start_point
    
    # 3. SCAN LOOP: We check every number from the next position to the end.
    for current_scanning_index in range(start_point + 1, end_point + 1):
        # 4. If we find a number SMALLER than or equal to our pivot:
        if number_list[current_scanning_index] <= pivot_value:
            # Shift our 'smaller parts' boundary by one
            smaller_elements_last_idx += 1
            # Swap: Move that smaller number inside the boundary
            (number_list[smaller_elements_last_idx], number_list[current_scanning_index]) = \
            (number_list[current_scanning_index], number_list[smaller_elements_last_idx])
            
    # 5. FINAL SWAP: After checking everyone, move the pivot from the 
    # original start point to its final correctly sorted position!
    (number_list[start_point], number_list[smaller_elements_last_idx]) = \
    (number_list[smaller_elements_last_idx], number_list[start_point])
    
    # Give back the final position of our pivot
    return smaller_elements_last_idx

# This is the main function that keeps 'Quick Sorting' smaller chunks
def quick_sort(number_list, start_point, end_point):
    """
    Recursively sorts the list by repeatedly picking a pivot and partitioning.
    """
    # 1. BASE CASE: If the start and end point overlap, the list piece is sorted!
    if start_point < end_point:
        # 2. PARTITION STEP: Organize around a pivot and find its final spot
        final_pivot_spot = organize_around_pivot(number_list, start_point, end_point)
        
        # 3. RECURSIVE MOVES:
        # Now, call Quick Sort for the group to the LEFT of the pivot spot
        quick_sort(number_list, start_point, final_pivot_spot - 1)
        
        # Then, call Quick Sort for the group to the RIGHT of the pivot spot
        quick_sort(number_list, final_pivot_spot + 1, end_point)
        
    # Give back the final list
    return number_list

# --- START OF PROGRAM ---

# 1. Our messy list of numbers
my_numbers = [10, 80, 30, 90, 40, 50, 70]

print("Welcome to Quick Sort!")
print(f"Original messy list: {my_numbers}")

# 2. Run the sorting process
# Note: We pass (list, first_index, last_index)
sorted_result = quick_sort(my_numbers, 0, len(my_numbers) - 1)

print(f"\nFinal sorted list:   {sorted_result}")
