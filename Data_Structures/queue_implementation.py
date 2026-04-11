"""
================================================================================
CONCEPTS AND THEORY: QUEUE (FIRST-IN, FIRST-OUT)
================================================================================

--- TIME COMPLEXITY ANALYSIS ---
- ENQUEUE (Join): O(1) (Adding to the very back is instant)
- DEQUEUE (Serve):O(n) (In this list implementation, shifting everyone forward takes time)
- PEEK (Look):    O(1) (Instantly seeing who is at the front)
- SEARCH:         O(n) (Must scan every single person in line)
--------------------------------
- SPACE COMPLEXITY: O(n) (Memory scales with every person in the line)

STATUS: INDEPENDENT (Self-contained 'Queue' class)
================================================================================

1. WHAT IS A QUEUE?
   A Queue is a very 'fair' data structure that follows the 
   **FIRST-IN, FIRST-OUT (FIFO)** rule. 

2. THE TWO MAIN ACTIONS:
   - 1. **ENQUEUE**: Adding a new item to the BACK of the line.
   - 2. **DEQUEUE**: Removing the item from the FRONT of the line.

3. THE RULES:
   Unlike a Stack (where you only use the 'Top'), a Queue has TWO 
   active ends:
   - **THE BACK**: Where everyone joins.
   - **THE FRONT**: Where everyone gets served.

4. WHY IS IT USEFUL?
   - **Printer Tasks**: Your computer prints documents in the order 
     you sent them.
   - **Web Servers**: When millions of people visit a website simultaneously, 
     the server places them in a 'Queue' so no one gets left out.

5. REAL LIFE EXAMPLE:
   Think of a **CINEMA TICKET COUNTER**. 
   - When a new customer arrives, they join at the BACK of the line (Enqueue).
   - The ticket seller only talks to the person at the very FRONT (Dequeue).
   - You never serve a customer in the middle of the line. The person who has 
     been waiting the longest is ALWAYS served first!
================================================================================
"""

class Queue:
    """
    Simulates a First-In, First-Out (FIFO) queue.
    """
    def __init__(self):
        # q: internal list to store queue elements
        self.q = [] # q = queue storage
        
    def is_empty(self):
        """ Checks if the queue is empty. """
        # Returns True if list q has no elements
        return len(self.q) == 0
        
    def enqueue(self, x):
        """ Adds item x to the back of the queue. """
        # x: data item to join the line
        self.q.append(x) # add x to end of list (back of queue)
        print(f"Enqueued: {x} ")
        
    def dequeue(self):
        """ Removes and returns the front item of the queue. """
        # 1. Safety check for empty queue dequeueing
        if self.is_empty():
            print("Notice: Queue is empty! ")
            return None
            
        # 2. In a simple list queue, the front is at index 0
        v = self.q[0] # v: value at the front of the line
        
        # 3. Shift everyone forward by slicing the list from index 1
        self.q = self.q[1:] # ignore the first item (O(n) shift)
        print(f"Dequeued: {v} ")
        
        # 4. Return the removed item
        return v    
        
    def __str__(self):
        """ Displays the queue's current state. """
        # Shows list starting from Front [0] to Back [-1]
        return f"Current Queue: {self.q}"

# --- START OF PROGRAM ---

# Q: instance of our Queue class
Q = Queue()

print("Welcome to the Queue Simulator!\n")

# 1. Join the line using enqueue
Q.enqueue(10); Q.enqueue(20); Q.enqueue(30)

# Show queue status
print(f"\n{Q}")

# 2. Serve from the front using dequeue
v1 = Q.dequeue() # v1: first served person
v2 = Q.dequeue() # v2: second served person

# Final status
print(f"\nFinal State: {Q} ✅")
