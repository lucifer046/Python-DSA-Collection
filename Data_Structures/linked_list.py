"""
================================================================================
CONCEPTS AND THEORY: LINKED LIST (THE 'CHAIN OF CLUES')
================================================================================

1. WHAT IS A LINKED LIST?
   A Linked List is a series of data points called **NODES**. 
   Unlike a standard list (array), where all items sit together in a row, 
   Linked List nodes can be scattered anywhere in your computer's memory!

2. HOW NODES WORK:
   Each Node has two parts:
   - 1. **VALUE**: The data you want to store (like a number or string).
   - 2. **NEXT**: A 'pointer' or 'clue' that tells you where the next node is.

3. ADVANTAGES OVER ARRAYS:
   - 1. **GROWING**: You can add new nodes at any time without resizing 
        the whole list.
   - 2. **INSERTING**: You can 'hook' a new node into the middle of the 
        chain instantly without shifting everyone else.

4. DISADVANTAGE:
   - **SEARCHING**: You can't jump straight to the 10th item. You have to 
     start at the 'Head' and walk through each node one-by-one until 
     you find what you want (O(n) time).

5. REAL LIFE EXAMPLE:
   Think of a **TREASURE HUNT**. 
   - You find the first clue. It gives you a piece of treasure (Value) 
     and tells you where the *next* clue is hidden (Link). 
   - You go to that spot, find more treasure, and get the *next* location. 
   - You keep going until the final clue says: "The hunt ends here" (None).
================================================================================
"""

class LinkedListNode:
    """
    A single link in our chain. Each Node knows its value and the next person in line.
    """
    def __init__(self, initial_value=None):
        # The actual data we want to keep
        self.value = initial_value
        # The link to the next Node (starts at None because it's the last one for now)
        self.next = None
        return

    # A simple way to check: "Is this node empty?"
    def isempty(self):
        # If the value is None, nobody lives in this node
        return self.value is None

    # --- RECURSIVE APPEND (The 'Pass the Parcel' Method) ---
    def append_recursive(self, new_value):
        """
        Asks the current node to add a new value. If it's busy, it passes the task to the next node.
        """
        # 1. If this exact node is empty, just take the value
        if self.isempty(): 
            self.value = new_value
            
        # 2. If this is the LAST node in the chain (no one follows me):
        elif self.next is None:
            # Create a new Node and hook it up as my next person
            self.next = LinkedListNode(new_value)
            
        # 3. Otherwise, pass the request to the next person in line
        else:
            self.next.append_recursive(new_value) 
        return

    # --- ITERATIVE APPEND (The 'Walking' Method) ---
    def append_iterative(self, new_value):
        """
        Starts at the beginning and walks the entire chain to find the end.
        """
        # 1. If the starting node is empty, take the value and finish
        if self.isempty():
            self.value = new_value
            return
            
        # 2. Start at 'self' and use a 'walker' to go through the list
        current_walker = self
        
        # 3. While there is a next person in line, keep moving forward
        while current_walker.next is not None:
            current_walker = current_walker.next
            
        # 4. Once we reach the last person, hook the new Node to them
        current_walker.next = LinkedListNode(new_value) 
        return

    # --- INSERT AT FRONT (The 'Swap and Connect' Method) ---
    def insert_at_front(self, new_value):
        """
        Inserts a new value into the current spot by shifting the old value forward.
        """
        # 1. If the node is currently empty, just take the value
        if self.isempty():
            self.value = new_value
            return
            
        # 2. Create a 'copy' node to hold our current information
        newly_created_node = LinkedListNode(new_value)
        
        # 3. Swap Trick: 
        # Exchange the value in 'self' with the value in 'newly_created_node'
        (self.value, newly_created_node.value) = (newly_created_node.value, self.value)
        
        # 4. Change Links: 
        # Hook the 'newly_created_node' as my next child, and have it point 
        # to my *original* next child.
        (self.next, newly_created_node.next) = (newly_created_node, self.next)
        return

    # --- RECURSIVE DELETE (The 'Search and Cut' Method) ---
    def delete_recursive(self, target_value):
        """
        Finds a specific value and removes its node from the chain.
        """
        # 1. If the list is completely empty, there's nothing to delete
        if self.isempty():
            return
            
        # 2. If WE are the one to be deleted:
        if self.value == target_value:
            # Clear our value
            self.value = None
            # If we have a child, we 'copy' their life into ours and skip them!
            if self.next is not None:
                self.value = self.next.value
                self.next = self.next.next
            return
            
        # 3. If we aren't the target, check our neighbor (the next node)
        else:
            if self.next is not None:
                # Ask the neighbor to try deleting the value
                self.next.delete_recursive(target_value)
                
                # Cleanup Step: If the neighbor deleted itself and became empty:
                if self.next.value is None:
                    # Remove the link to them entirely
                    self.next = None
        return

    # --- DISPLAY (The 'Show the Whole Chain' Method) ---
    def display_list(self):
        """
        Prints the entire chain from the current spot to the end.
        """
        if self.isempty():
            print('None')
        else:
            current_walker = self
            # Keep walking and printing until we run out of clues
            while current_walker is not None:
                print(f"[{current_walker.value}]", end=" -> ")
                current_walker = current_walker.next
            print("None") # Marks the end of the chain

# --- START OF PROGRAM ---

print("Welcome to the Linked List Chain!")

# 1. Create the 'Head' (the first clue of our treasure hunt)
head = LinkedListNode(10)

# 2. Let's add more clues using different methods
print("\n--- Adding nodes 20 and 30 (Recursively) ---")
head.append_recursive(20)
head.append_recursive(30)

print("--- Adding nodes 40 and 50 (Iteratively) ---")
head.append_iterative(40)
head.append_iterative(50)

# 3. Let's see our hunt so far
print("\n--- Current Chain ---")
head.display_list()

# 4. Let's delete a clue (The number 30)
print("\n--- Deleting node 30 ---")
head.delete_recursive(30)

# 5. Final Result
print("--- Final Chain ---")
head.display_list()
