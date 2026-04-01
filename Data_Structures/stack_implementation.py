"""
================================================================================
CONCEPTS AND THEORY: STACK (LAST-IN, FIRST-OUT)
================================================================================

--- TIME COMPLEXITY ANALYSIS ---
- PUSH (Add):   O(1) (Instantly adding to the very top)
- POP (Remove): O(1) (Instantly taking off the very top)
- PEEK (Look):  O(1) (Instantly seeing what is on top)
- SEARCH:       O(n) (Must remove or scan everything to find an item)
--------------------------------
- SPACE COMPLEXITY: O(n) (We need space for every item in the pile)

STATUS: INDEPENDENT (Self-contained 'Stack' class)
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

class Stack:
    """
    Simulates a Last-In, First-Out (LIFO) stack.
    """
    def __init__(self):
        # s: internal storage list for the stack items
        self.s = [] # s = stack storage
        
    def is_empty(self):
        """ Checks if the stack is currently empty. """
        # Returns True if list s is empty, else False
        return len(self.s) == 0
        
    def push(self, x):
        """ Adds item x to the top of the stack. """
        # x: data item to push
        self.s.append(x) # add x to end of list (top of stack)
        print(f"Pushed: {x} 📥")
        
    def pop(self):
        """ Removes and returns the top item from the stack. """
        # 1. Safety check for empty stack popping
        if self.is_empty():
            print("Notice: Stack is empty! 🚫")
            return None # cannot pop from empty stack
            
        # 2. Use list.pop() to remove and return last element
        v = self.s.pop() # v: value taken from top
        print(f"Popped: {v} 📤")
        
        # 3. Return the popped item
        return v    
        
    def __str__(self):
        """ Displays the stack's current state. """
        return f"Current Stack: {self.s} (Top at end)"

# --- START OF PROGRAM ---

# S: instance of our Stack class
S = Stack()

print("Welcome to the Stack Simulator!\n")

# 1. Add items using push
S.push(10); S.push(20); S.push(30)

# Show current stack
print(f"\n{S}")

# 2. Remove items using pop
v1 = S.pop() # v1: first popped item
v2 = S.pop() # v2: second popped item

# Final status
print(f"\nFinal State: {S} ✅")
