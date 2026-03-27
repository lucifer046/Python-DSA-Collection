"""
================================================================================
CONCEPTS AND THEORY: STACK (LAST-IN, FIRST-OUT)
================================================================================

1. WHAT IS A STACK?
   A Stack is simplest data structure in computing. It follows a 
   very strict rule: **LAST-IN, FIRST-OUT (LIFO)**.

2. THE TWO MAIN ACTIONS:
   - 1. **PUSH**: Adding a new item to the VERY TOP of the pile.
   - 2. **POP**: Removing the item that is currently on the VERY TOP.

3. THE RULES:
   You cannot touch anything in the middle or bottom of a Stack. 
   If you want the 3rd item down, you must 'Pop' (remove) the top 
   two items first!

4. WHY IS IT USEFUL?
   - **Undo History**: When you press 'Undo', it removes your last 
     action (which was on the top of the action pile).
   - **Function Calls**: Your computer keeps a 'Stack' of programs 
     to remember where to return after a function finishes.

5. REAL LIFE EXAMPLE:
   Think of a **STACK OF DINNER PLATES**. 
   - When you finish washing a plate, you place it on TOP of the pile (Push).
   - When you need a plate for dinner, you take the one from the TOP (Pop).
   - You never pull a plate from the middle because everything else 
     would crash. The last plate you washed is always the first one 
     you use!
================================================================================
"""

class PlateStack:
    """
    A class that represents a physical stack of items.
    """
    def __init__(self):
        # We use a standard Python list as our internal 'storage pile'
        self.storage_pile = []
        
    def is_stack_empty(self):
        """
        Simply checks if we have any items in our pile.
        """
        # If the list is empty, return True
        return self.storage_pile == []
        
    def push_item(self, new_item):
        """
        Adds an item to the very top (the end of our list).
        """
        # Python's 'append' adds an item to the end, which is our 'Top'
        self.storage_pile.append(new_item)
        print(f"Pushed: {new_item}")
        
    def pop_item(self):
        """
        Removes and gives back the item on the very top.
        """
        # 1. Create a variable to hold our removed item
        item_to_remove = None
        
        # 2. Safety Check: We can't pop from an empty stack!
        if not self.is_stack_empty():
            # 'pop()' in Python removes the last item and returns it
            item_to_remove = self.storage_pile.pop()
            print(f"Popped: {item_to_remove}")
        else:
            print("Notice: Stack is already empty!")
            
        # Give back the item we took off the top
        return item_to_remove    
        
    # This special function tells Python how to print our stack
    def __str__(self):
        return f"Current Stack (Bottom to Top): {self.storage_pile}"

# --- START OF PROGRAM ---

# Create our Stack object
my_piles = PlateStack()

print("Welcome to the Stack Simulator!")

# 1. Push items onto the stack
my_piles.push_item(10)
my_piles.push_item(20)
my_piles.push_item(30)
my_piles.push_item(40)

# Show the stack after pushing
print(f"\n{my_piles}")

# 2. Pop the items off the top (Notice they come off in reverse order!)
print("\n--- Popping 2 items ---")
first_out = my_piles.pop_item()
second_out = my_piles.pop_item()

# 3. Final Result
print(f"Final {my_piles}")
