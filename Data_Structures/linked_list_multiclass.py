"""
================================================================================
CONCEPTS AND THEORY: TWO-CLASS LINKED LIST (THE MANAGER & THE WORKER)
================================================================================

--- TIME COMPLEXITY ANALYSIS ---
- ACCESS (by Index):    O(n) (Manager must walk the entire train starting from the head)
- SEARCH (by Value):    O(n) 
- INSERT (at Head):     O(1) (Manager simply swaps the 'Engine' head pointer)
- INSERT (at Tail):     O(n) (Manager must travel to the very end of the train)
- DELETE (at Head):     O(1) (Instant engine unhooking)
--------------------------------
- SPACE COMPLEXITY: O(n) (One 'CarriageNode' object is created for every item)

STATUS: LINKED (The 'TrainManager' class relies on the 'CarriageNode' class)
================================================================================

1. WHAT IS THE DIFFERENCE?
   In the previous 'Single-Class' version, every Node thought it was 
   the entire list. In this 'Two-Class' version, we have a clear 
   separation of duties:
   - 1. **THE WORKER (Node Class)**: Simple and focused. It only knows 
        its own value and who is behind it.
   - 2. **THE MANAGER (LinkedList Class)**: The 'Boss' who keeps track 
        of the very first Node (The Head) and knows how to search, 
        add, or delete from the entire chain.

2. WHY USE TWO CLASSES?
   This is called **Separation of Concerns**. It's much cleaner! 
   The user only talks to the 'Manager' (LinkedList), and the 
   Manager handles all the messy 'Node' logic behind the scenes.

3. REAL LIFE EXAMPLE:
   Think of a **TRAIN AND STATION MANAGER**.
   - **The Node is a Carriage**: It carries some cargo (Data) and is 
     hooked to the carriage behind it (Next).
   - **The LinkedList is the Station Manager**: The manager knows 
     exactly where the 'Train Engine' (The Head) is parked. 
   - If you want to add a carriage, you tell the Manager. The manager 
     walks from the Engine to the very end of the train and hooks 
     the new carriage on!
================================================================================
"""

# --- CLASS 1: THE WORKER (CARRIAGE) ---
class Node:
    """ Holds a value and a link to the next node. """
    def __init__(self, x):
        # x: data item value, n: next node link
        self.v = x # v = value
        self.n = None # n = next reference

# --- CLASS 2: THE MANAGER (LIST MANAGER) ---
class LinkedList:
    """ Manages the collection of Nodes as a single List. """
    def __init__(self):
        # h: pointer to the very first node (Head)
        self.h = None # h = head of the list
        
    def is_empty(self):
        """ Checks if the list has any nodes. """
        return self.h is None # returns True if head is None
        
    def add(self, x):
        """ Appends a new node with value x to the end of the list. """
        # 1. If list is empty, new node becomes the Head
        if self.is_empty():
            self.h = Node(x)
            return
            
        # 2. Walk to the end of the chain
        w = self.h # w = walker node
        while w.n is not None:
            w = w.n # w moves forward
            
        # 3. Hook the new node to the last node's next pointer
        w.n = Node(x)
            
    def drop(self, t):
        """ Removes the first node containing target value 't'. """
        # 1. Error check: Cannot drop from empty list
        if self.is_empty(): return
            
        # 2. Special case: If the Head itself is the target
        if self.h.v == t:
            self.h = self.h.n # update Head to the next node
            return
        
        # 3. General search: Stay one step behind to re-link easily
        p = self.h # p = previous node walker
        c = self.h.n # c = current node walker
        
        # 4. Loop until current node matches target or end is reached
        while c is not None:
            if c.v == t:
                # 5. Bypass current node 'c' by linking 'p' directly to c.n
                p.n = c.n # 'cuts' node c from the chain
                return
            # 6. Move both walkers forward
            p = c
            c = c.n
            
    def show(self):
        """ Displays all nodes in the list. """
        # 1. Handle empty list case
        if self.is_empty():
            print('List is Empty 🚫')
            return
            
        # 2. Iterate and print each value
        w = self.h # w = walker
        while w is not None:
            print(f"[{w.v}]", end=" 🔗 ") # print current value
            w = w.n # move forward
        print("END")

# --- START OF PROGRAM ---

# L: instance of LinkedList manager
L = LinkedList()

print("Welcome to the Multi-Class Linked List Yard!\n")

# Adding data carraiges
L.add(30); L.add(40); L.add(50)

# Show current layout
print("Initial Layout:")
L.show()

# Removing cargo
print("\nRemoving item (30) from the chain...")
L.drop(30)

# Final result
print("\nFinal Layout:")
L.show()
