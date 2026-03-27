"""
================================================================================
CONCEPTS AND THEORY: BINARY SEARCH (DIVIDE AND CONQUER)
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

def binary_search_iterative(sorted_list, target_value):
    """
    Finds the target_value by repeatedly moving the search boundaries.
    """
    # 1. Start our search area at the very edges of the list
    start_point = 0
    end_point = len(sorted_list) - 1
    
    # 2. Keep searching as long as there is at least one item left to check
    while start_point <= end_point: 
        
        # 3. Find the middle spot between our start and end points
        middle_index = (start_point + end_point) // 2
        
        # 4. If the item in the middle is LESS than what we want:
        if sorted_list[middle_index] < target_value:
            # We move the 'start_point' past the middle (ignore the left half)
            start_point = middle_index + 1
            
        # 5. If the item in the middle is MORE than what we want:
        elif sorted_list[middle_index] > target_value:
            # We move the 'end_point' before the middle (ignore the right half)
            end_point = middle_index - 1
            
        # 6. If it's not smaller and not larger, it must be the ONE!
        else:
            # We found it! Return the position (index) where it lives
            return middle_index
            
    # If the loop finishes without finding the item:
    return False

# ================================================================================
# VERSION 2: RECURSIVE IMPLEMENTATION (Function calling itself)
# ================================================================================

def binary_search_recursive(sorted_list, target_value, start_point, end_point):
    """
    Finds the target_value by asking the function to search a smaller half.
    """
    # 1. BASE CASE: If the search area is gone (empty), we failed to find it
    if end_point - start_point < 0:
        return False
        
    # 2. Find the middle index
    middle_index = (end_point + start_point) // 2
    
    # 3. CHECK: Did we find it exactly at the middle?
    if target_value == sorted_list[middle_index]:
        return middle_index
        
    # 4. RECURSIVE MOVE (Left): If target is smaller, search the left half
    if target_value < sorted_list[middle_index]:
        # Return the result of the SAME function, but with a smaller 'end_point'
        return binary_search_recursive(sorted_list, target_value, start_point, middle_index - 1)
        
    # 5. RECURSIVE MOVE (Right): Otherwise, search the right half
    else:
        # Return the result of the SAME function, but with a smaller 'start_point'
        return binary_search_recursive(sorted_list, target_value, middle_index + 1, end_point)

# --- START OF PROGRAM ---

# 1. Our sorted list of mystery numbers
my_numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
my_target = 23

print("Welcome to the Binary Search Demo!")
print(f"List: {my_numbers}")
print(f"Goal: Find the location of number '{my_target}'\n")

# --- TESTING ITERATIVE VERSION ---
result_idx = binary_search_iterative(my_numbers, my_target)
print("--- Result from Iterative Version ---")
if result_idx is not False:
    print(f"Found it at index position: {result_idx}")
else:
    print("Sorry, that number is not in the list.")

# --- TESTING RECURSIVE VERSION ---
# For recursion, we have to tell it the initial start and end points [0, len-1]
result_idx = binary_search_recursive(my_numbers, my_target, 0, len(my_numbers) - 1)
print("\n--- Result from Recursive Version ---")
if result_idx is not False:
    print(f"Found it at index position: {result_idx}")
else:
    print("Sorry, that number is not in the list.")
