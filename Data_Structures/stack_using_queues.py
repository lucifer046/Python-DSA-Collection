"""
================================================================================
CONCEPTS AND THEORY: STACK USING QUEUES
================================================================================

--- TIME COMPLEXITY ANALYSIS ---

1. STACK USING TWO QUEUES (Push costly):
   - PUSH: O(n) (Must move everyone back and forth)
   - POP:  O(1) (Instantly taking from the front)

2. STACK USING ONE QUEUE:
   - PUSH: O(n) (Must rotate the entire line)
   - POP:  O(1) (Instantly taking from the front)

--------------------------------
- SPACE COMPLEXITY: O(n) (Still need space for every item)

STATUS: INDEPENDENT (Self-contained 'Stack' implementations)
================================================================================

1. WHAT IS THIS?
   This is a "Brain Teaser" in computer science. We are trying to build a 
   **Stack** (LIFO - Last In, First Out) using only the tools of a 
   **Queue** (FIFO - First In, First Out).

2. THE CHALLENGE:
   - A Queue is like a line at a store (first person in is served first).
   - A Stack is like a stack of plates (last plate on top is used first).
   - How do you make a "fair" line behave like an "unfair" stack?

3. THE TWO STRATEGIES:
   - **Strategy A (Two Queues)**: We use a "Waiting Room" (Queue 2) to 
     shuffle items around until the newest item is at the very front.
   - **Strategy B (One Queue)**: We add an item to the back, then 
     everyone else in front of it circles around to stand behind it!

4. WHY DO THIS?
   In the real world, you'd just use a list. But in interviews or low-level 
   systems, you might only have "Queue" hardware and need to simulate a 
   Stack for undo-history or backtracking.
================================================================================
"""

from collections import deque

class StackTwoQueues:
    """
    Implements a Stack (LIFO) using TWO Queues.
    In this version, we make 'Push' costly to keep 'Pop' fast.
    """
    def __init__(self):
        # q1: Primary queue (holds the stack items in LIFO order)
        # q2: Helper queue for shuffling
        self.q1 = deque()
        self.q2 = deque()
        
    def push(self, x):
        """ Adds item x to the stack. (Costly O(n) operation) """
        # 1. Add new item to the empty helper queue (q2)
        self.q2.append(x)
        
        # 2. Move everything from q1 to q2 (behind our new item)
        while self.q1:
            self.q2.append(self.q1.popleft())
            
        # 3. Swap the names: q1 becomes the full stack, q2 becomes empty
        self.q1, self.q2 = self.q2, self.q1
        print(f"[TwoQueues] Pushed: {x}")
        
    def pop(self):
        """ Removes the top item. (Fast O(1) operation) """
        if not self.q1:
            print("[TwoQueues] Notice: Stack is empty!")
            return None
        v = self.q1.popleft()
        print(f"[TwoQueues] Popped: {v}")
        return v

    def __str__(self):
        return f"Stack (Two Queues): {list(self.q1)}"

class StackOneQueue:
    """
    Implements a Stack (LIFO) using only ONE Queue.
    We rotate the queue to make the newest item sit at the front.
    """
    def __init__(self):
        # q: Single queue for storage
        self.q = deque()
        
    def push(self, x):
        """ Adds item x to the stack. (O(n) rotation) """
        # 1. Get current size before adding new item
        size = len(self.q)
        
        # 2. Add the new item to the back
        self.q.append(x)
        
        # 3. Rotate: Move all previous items to the back of the new item
        for _ in range(size):
            # Take from front and put at back
            self.q.append(self.q.popleft())
            
        print(f"[OneQueue] Pushed: {x}")
        
    def pop(self):
        """ Removes the top item. (Fast O(1) operation) """
        if not self.q:
            print("[OneQueue] Notice: Stack is empty!")
            return None
        v = self.q.popleft()
        print(f"[OneQueue] Popped: {v}")
        return v

    def __str__(self):
        return f"Stack (One Queue): {list(self.q)}"

# --- START OF PROGRAM ---

print("--- Method 1: Stack using Two Queues ---")
s2 = StackTwoQueues()
s2.push(10); s2.push(20); s2.push(30)
print(s2)
s2.pop()
print(f"Final State: {s2}\n")

print("--- Method 2: Stack using Single Queue ---")
s1 = StackOneQueue()
s1.push(100); s1.push(200); s1.push(300)
print(s1)
s1.pop()
print(f"Final State: {s1} [DONE]")
