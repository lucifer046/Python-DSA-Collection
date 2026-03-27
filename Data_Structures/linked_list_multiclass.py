"""
================================================================================
CONCEPTS AND THEORY: TWO-CLASS LINKED LIST (THE MANAGER & THE WORKER)
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

# --- CLASS 1: THE WORKER (THE CARRIAGE) ---
class CarriageNode:
    """
    A simple container that holds data and a link to the next carriage.
    """
    def __init__(self, item_value):
        # The 'self.data' stores our information
        self.data = item_value
        # The 'self.next' starts as None until we hook something to it
        self.next = None

# --- CLASS 2: THE MANAGER (THE STATION MANAGER) ---
class TrainManager:
    """
    The 'Boss' class that manages the entire train (Linked List).
    It only needs to know where the very first carriage (the Head) is.
    """
    def __init__(self):
        # When we first start, the train is empty, so there is no Head.
        self.head = None
        
    # A simple check: "Is there any train Engine parked here currently?"
    def is_train_empty(self):
        # If head is None, the train doesn't exist yet!
        return self.head is None
        
    # --- ADD TO THE END ---
    def add_carriage_to_end(self, item_value):
        """
        Takes a value, creates a new carriage, and hooks it to the end of the train.
        """
        # 1. If the train is empty, this new carriage becomes the 'Head' (Engine)
        if self.is_train_empty():
            self.head = CarriageNode(item_value)
        else:
            # 2. Otherwise, start at the Head and 'walk' to the end
            current_node = self.head
            # While the current carriage has something hooked behind it...
            while current_node.next is not None:
                # ...move one step forward
                current_node = current_node.next
            # 3. Once we find the very last carriage, hook our new one there
            current_node.next = CarriageNode(item_value)
            
    # --- DELETE FROM THE TRAIN ---
    def remove_carriage(self, target_value):
        """
        Searches for a carriage with target_value and unhooks it from the train.
        """
        # 1. Error check: If there is no train, we can't delete anything
        if self.is_train_empty():
            return 'Sorry, the train is empty!'
            
        # 2. Special Case: Is the target in the very first carriage (The Head)?
        if self.head.next is None:
            # If there is ONLY one carriage and it's our target:
            if self.head.data == target_value: 
                # Just remove the head!
                self.head = None
            else:
                return 'Target not found in the single carriage.'
        
        # 3. Scanning Move: We need two walkers (one ahead of the other)
        # current_node traces where we are
        # previous_node stays one step behind so we can 're-hook' the chain
        current_node = self.head
        previous_node = self.head
        
        # Keep walking as long as there's a next person AND we haven't found the target
        while current_node.next is not None and current_node.data != target_value: 
            # Move the previous_node to where current_node is
            previous_node = current_node
            # Move current_node one step forward
            current_node = current_node.next
            
        # 4. Now that the loop finished, let's check what we found
        
        # Case A: The target was in the very first carriage
        if current_node.data == target_value and current_node == self.head: 
            # Simply make the second carriage the new Head
            self.head = current_node.next
            
        # Case B: The target was somewhere else in the train
        elif current_node.data == target_value: 
            # Bypass the 'current_node' by hooking 'previous' directly to 'next'
            # (This 'cuts' the current_node out of the chain!)
            previous_node.next = current_node.next
        
        # Case C: We walked the whole train and didn't find it
        else:
            return 'Target value does not exist on this train.'
            
    # --- SHOW THE TRAIN ---
    def show_all_carriages(self):
        """
        Prints the contents of every carriage from start to end.
        """
        if self.is_train_empty():
            print('None')
        else:
            # Start at the Head walker
            current_node = self.head
            while current_node is not None:
                # Print the data in the current carriage
                print(f"[{current_node.data}]", end=" == ")
                # Move to the next one
                current_node = current_node.next
            # Marks the end of the line
            print("END")

# --- START OF PROGRAM ---

# Create our 'Station Manager'
my_train_manager = TrainManager()

print("Welcome to the Multi-Class Train Yard!")

# 1. Add some cargo (Carriages)
print("\n--- Adding Carriages: 30, 40, and 50 ---")
my_train_manager.add_carriage_to_end(30)
my_train_manager.add_carriage_to_end(40)
my_train_manager.add_carriage_to_end(50)

# 2. Let's see our train
print("Current Train Layout:")
my_train_manager.show_all_carriages()

# 3. Unhook the number 30
print("\n--- Unhooking Carriage 30 ---")
my_train_manager.remove_carriage(30)

# 4. Final Result
print("Final Train Layout:")
my_train_manager.show_all_carriages()
