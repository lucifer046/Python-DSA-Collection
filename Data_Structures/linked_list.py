"""
================================================================================
CONCEPTS AND THEORY: LINKED LIST (THE 'CHAIN OF CLUES')
================================================================================

--- TIME COMPLEXITY ANALYSIS ---
- ACCESS (by Index):    O(n) (Must walk through each clue from the head)
- SEARCH (by Value):    O(n) 
- INSERT (at Head):     O(1) (Instant addition at the start)
- INSERT (at Tail):     O(n) (Must walk to the very end to append)
- DELETE (at Head):     O(1) (Instant removal)
--------------------------------
- SPACE COMPLEXITY: O(n) (One node is created for every single item)

STATUS: INDEPENDENT (Self-contained Node class with helper methods)
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

class Node:
    """
    A single link in the chain. knows its value and the next person in line.
    """
    def __init__(self, v=None):
        # v: value stored in node, n: next node pointer
        self.v = v # v = node value
        self.n = None # n = next node link
        return

    def is_empty(self):
        """ Checks if the node is empty. """
        return self.v is None # returns True if value is None

    def add(self, x):
        """ Appends a new value x to the end of the chain (Recursive). """
        # 1. If this node is empty, take the value
        if self.is_empty(): 
            self.v = x
            
        # 2. If this is the last node, create a new link
        elif self.n is None:
            self.n = Node(x)
            
        # 3. Otherwise, pass the value to the next link
        else:
            self.n.add(x) # pass the value down
        return

    def put(self, x):
        """ Appends a new value x to the end of the chain (Iterative). """
        # 1. If starting node is empty, take x
        if self.is_empty():
            self.v = x
            return
            
        # 2. w: walker that traverses the list
        w = self # w = current node walker
        
        # 3. Walk until we reach the end of the chain
        while w.n is not None:
            w = w.n # move walker to next node
            
        # 4. Create and attach the new node at the end
        w.n = Node(x) 
        return

    def push(self, x):
        """ Inserts a new value x at the current front position. """
        # 1. If empty, simply assign x
        if self.is_empty():
            self.v = x
            return
            
        # 2. Create a new node to hold the incoming value
        nx = Node(x) # nx = new node
        
        # 3. Swap current value with new node's value and re-link
        self.v, nx.v = nx.v, self.v # exchange values
        self.n, nx.n = nx, self.n # re-link new node as next
        return

    def drop(self, t):
        """ Removes the first occurrence of target value 't'. """
        # 1. Check if list has any content
        if self.is_empty(): return
            
        # 2. If this node matches the target t
        if self.v == t:
            self.v = None # clear value
            
            # 3. If there's a next node, copy its data and skip it
            if self.n is not None:
                self.v = self.n.v # take next node's value
                self.n = self.n.n # skip next node
            return
            
        # 4. Search recursively in the next node
        else:
            if self.n is not None:
                self.n.drop(t) # ask next node to drop t
                
                # 5. Cleanup: If next node cleared itself, remove the link
                if self.n.v is None:
                    self.n = None
        return

    def show(self):
        """ Prints the entire list structure. """
        # 1. If empty, print None
        if self.is_empty():
            print('Empty Chain ')
        else:
            w = self # w: list walker
            # 2. Traverse and print each value
            while w is not None:
                print(f"({w.v})", end=" ") # print node value
                w = w.n
            print("END") # end of chain indicator

# --- START OF PROGRAM ---

# H: the base 'head' node of our chain list
H = Node(10)

print("Welcome to the Linked List Chain Demo!\n")

# Adding values using different methods
H.add(20); H.add(30) # recursive add
H.put(40); H.put(50) # iterative add

# Display chain
print("Chain status after adding values:")
H.show()

# Deleting a value
print("\nRemoving value (30) from the chain...")
H.drop(30)

# Final result
print("\nFinal Result:")
H.show()
