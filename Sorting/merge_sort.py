"""
================================================================================
CONCEPTS AND THEORY: MERGE SORT (THE 'DIVIDE AND CONQUER' WAY)
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

# This helper function takes two lists that are ALREADY SORTED and 
# 'zips' them together into one single sorted list.
def merge_two_sorted_lists(left_list, right_list):
    """
    Zips two sorted stacks into one big sorted stack.
    """
    # 1. Measure the length of both lists
    left_length = len(left_list)
    right_length = len(right_list)
    
    # 2. Preparation: Create an empty result list and two index 'trackers'
    merged_result = []
    left_index = 0
    right_index = 0
    
    # 3. CASE 1: While BOTH lists still have items to check...
    while left_index < left_length and right_index < right_length:
        # 4. Compare the 'top' item of the left list with the 'top' of the right
        if left_list[left_index] <= right_list[right_index]:
            # If the left item is smaller, add it to our result list
            merged_result.append(left_list[left_index])
            # Move the left tracker one step forward
            left_index += 1
        else:
            # Otherwise, the right item is smaller, so add it
            merged_result.append(right_list[right_index])
            # Move the right tracker one step forward
            right_index += 1
    
    # 5. CASE 2: If we finished the right list, but the left list still has items left...
    # (Since the left list was ALREADY sorted, we can just grab everything at once!)
    while left_index < left_length:
        merged_result.append(left_list[left_index])
        left_index += 1
    
    # 6. CASE 3: If we finished the left list, but the right still has items left...
    while right_index < right_length:
        merged_result.append(right_list[right_index])
        right_index += 1
    
    # Return our newly combined, perfectly sorted list   
    return merged_result

# This is the main function that keeps 'cutting' the list in half
def merge_sort(input_list): 
    """
    Recursively divides the problem into sub-problems until they are easy to solve.
    """
    # 1. Grab the current length of the list we are looking at
    current_length = len(input_list)
    
    # 2. BASE CASE: If the list has only 0 or 1 item, it's ALREADY sorted!
    if current_length <= 1:
        return(input_list)
    
    # 3. DIVIDE STEPS:
    # Find the middle point and split the current list into two halves.
    middle_point = current_length // 2
    
    # Ask 'merge_sort' to go and sort the left half (Recursion!)
    left_half_sorted = merge_sort(input_list[:middle_point]) 
    
    # Ask 'merge_sort' to go and sort the right half (Recursion!)
    right_half_sorted = merge_sort(input_list[middle_point:]) 
    
    # 4. CONQUER STEP (Merging):
    # Now that we have two sorted halves, use our 'zip' function to join them.
    final_sorted_list = merge_two_sorted_lists(left_half_sorted, right_half_sorted) 
    
    # Give back the final result
    return(final_sorted_list)

# --- START OF PROGRAM ---

# 1. Our messy, unsorted list of numbers
my_numbers = [38, 27, 43, 3, 9, 82, 10]

print("Welcome to Merge Sort!")
print(f"Original messy list: {my_numbers}")

# Run the sorting process
sorted_result = merge_sort(my_numbers)

print(f"\nFinal sorted list:   {sorted_result}")
