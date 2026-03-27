"""
================================================================================
CONCEPTS AND THEORY: QUEUE (FIRST-IN, FIRST-OUT)
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

class TicketQueue:
    """
    A class that represents a physical line (queue) of items.
    """
    def __init__(self):
        # We use a standard Python list as our internal 'waiting line'
        self.waiting_line = []
        
    def is_queue_empty(self):
        """
        Simply checks if anyone is currently in line.
        """
        # If the list equals an empty list [], it returns True
        return self.waiting_line == []
        
    def join_back_of_line(self, new_customer_value):
        """
        Adds a new person to the very back of the line.
        """
        # Python's 'append' adds an item to the end (the Back)
        self.waiting_line.append(new_customer_value)
        print(f"Joined: {new_customer_value} (Back of Line)")
        
    def serve_front_person(self):
        """
        Serves (removes) the person who is currently at the front.
        """
        # 1. Create a variable to hold our served customer
        served_customer = None
        
        # 2. Safety Check: We can't serve anyone if the line is empty!
        if not self.is_queue_empty():
            # In a Queue, the 'Front' person is at Index 0
            served_customer = self.waiting_line[0]
            
            # --- THE SHIFT STEP ---
            # Now we remove the person we served and SHIFT everyone forward.
            # Python's [1:] slice creates a new list from the 2nd person onwards.
            self.waiting_line = self.waiting_line[1:]
            
            print(f"Served: {served_customer} (Front of Line)")
        else:
            print("Notice: The line is already empty!")
            
        # Give back the person we served
        return served_customer    
        
    # This special function tells Python how to print our queue
    def __str__(self):
        return f"Current Line (Front to Back): {self.waiting_line}"

# --- START OF PROGRAM ---

# Create our Queue manager
my_queue = TicketQueue()

print("Welcome to the Ticket Counter!")

# 1. Customers join the line
my_queue.join_back_of_line(10)
my_queue.join_back_of_line(20)
my_queue.join_back_of_line(30)
my_queue.join_back_of_line(40)

# Show the queue after they joined
print(f"\n{my_queue}")

# 2. Serve the customers from the front (Notice they come off in the SAME order!)
print("\n--- Serving 2 Customers ---")
first_served = my_queue.serve_front_person()
second_served = my_queue.serve_front_person()

# 3. Final Result
print(f"Final {my_queue}")
