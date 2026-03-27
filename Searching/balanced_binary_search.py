"""
================================================================================
CONCEPTS AND THEORY: BALANCED BINARY SEARCH TREE (AVL TREE)
================================================================================

1. WHAT IS A BINARY SEARCH TREE (BST)?
   A tree where each spot (node) can have at most two children. 
   Rule: ALL numbers to the left are smaller, and ALL numbers to the right are larger.

2. THE PROBLEM (Why do we need a Balanced Tree?):
   If you add numbers in order like [1, 2, 3, 4], a normal BST becomes one long line
   instead of a tree. This makes searching slow (O(n) time).

3. THE SOLUTION: THE AVL TREE
   - Invented by Adelson-Velsky and Landis in 1962.
   - It is a "Self-Balancing" tree.
   - It uses a 'Balance Factor' (Height of Left side - Height of Right side).
   - Rule: For EVERY node, the Balance Factor must be between -1 and 1.

4. HOW IT WORKS: ROTATIONS
   If a tree gets too 'tilted' (Balance factor becomes -2 or +2), we perform
   'Rotations' (like shifting pieces of a puzzle) to pull the tree back into balance.
   - Single Rotation: Used for a simple tilt (Left-Left or Right-Right).
   - Double Rotation: Used for a zigzag tilt (Left-Right or Right-Left).

5. WHY IS THIS AWESOME? (The Theorem):
   An AVL tree guarantees that the tree's height will always be about log2(n).
   This means that even with 1 MILLION numbers, you only need to check about 
   20 spots to find what you're looking for! (O(log n) search time).

6. REAL LIFE EXAMPLE:
   Imagine a Librarian using a smart bookshelf. If all the 'A' books are 
   piling up on one side, the bookshelf automatically shifts some 'A' books 
   to keep the weight balanced. This ensures the librarian never has to 
   climb too many stairs to find a book!
================================================================================
"""

class AVLTree:
    """
    An AVL Tree is a special type of 'Family Tree' for numbers. 
    It follows two main rules:
    1. Numbers smaller than the 'Parent' go to the Left child.
    2. Numbers larger than the 'Parent' go to the Right child.
    3. The tree always stays 'balanced' (no side is way taller than the other) 
       so searching is super fast!
    """

    # This 'init' function runs whenever we create a new node (a spot in the tree)
    def __init__(self, initial_value=None):
        # 'self.value' is the number we are storing in this spot
        self.value = initial_value
        
        # If we actually gave it a number (it's not empty):
        if self.value is not None:
            # Every node starts with two 'ghost' children (empty trees)
            # This is like having empty seats ready for new numbers
            self.left = AVLTree()
            self.right = AVLTree()
            # Since it has a value, its height (layer count) is 1
            self.height = 1
        # If we didn't give it a number, it's an empty 'ghost' node:
        else:
            # It has no children yet
            self.left = None
            self.right = None
            # An empty spot has 0 height
            self.height = 0
        return

    # A simple way to check: "Is this spot empty?"
    def isempty(self):
        # If value is None, it means no number lives here
        return (self.value == None)

    # A 'leaf' is a node that has a number but no children (it's at the very bottom)
    def isleaf(self):
        # Check: 1. I have a value. 2. My left seat is empty. 3. My right seat is empty.
        return (self.value != None and self.left.isempty() and self.right.isempty())

    # Left rotation: Imagine the tree is leaning too much to the right.
    # We 'pull' the right child up to be the new boss of this section.
    def leftrotate(self):
        # We save all the pieces before moving them around:
        old_boss_value = self.value             
        new_boss_value = self.right.value      
        old_left_side_family = self.left             
        middle_family_branch = self.right.left      
        right_most_family_branch = self.right.right     
        
        # We create a new 'left child' using the old boss's value
        new_left_child = AVLTree(old_boss_value)
        new_left_child.left = old_left_side_family          
        new_left_child.right = middle_family_branch        
        
        # Now we promote the right child to be the current boss
        self.value = new_boss_value
        self.right = right_most_family_branch           
        self.left = new_left_child        
        return

    # Right rotation: Imagine the tree is leaning too much to the left.
    # We 'pull' the left child up to be the new boss.
    def rightrotate(self):
        # Save the current pieces:
        old_boss_value = self.value             
        new_boss_value = self.left.value       
        left_most_family_branch = self.left.left       
        middle_family_branch = self.left.right      
        old_right_side_family = self.right            
        
        # Create a new 'right child' using the old boss's value
        new_right_child = AVLTree(old_boss_value)
        new_right_child.left = middle_family_branch        
        new_right_child.right = old_right_side_family        
        
        # Promote the left child to be the new boss
        self.value = new_boss_value
        self.left = left_most_family_branch            
        self.right = new_right_child      
        return

    # This is how we add a new number to the tree
    def insert(self, new_number):
        # Rule of thumb: If you find an empty seat, take it!
        if self.isempty():
            self.value = new_number
            self.left = AVLTree()   
            self.right = AVLTree()
            self.height = 1         
            return        
        
        # If the number is already in the tree, we don't need to do anything
        if self.value == new_number:
            return        
        
        # If the new number is smaller, it belongs somewhere on the LEFT
        if new_number < self.value:
            # Recursively insert
            self.left.insert(new_number)
            # Rebalance
            self.rebalance()
            # Update height
            self.height = 1 + max(self.left.height, self.right.height)            
            
        # If the new number is bigger, it belongs somewhere on the RIGHT
        if new_number > self.value:
            # Recursively insert
            self.right.insert(new_number)
            # Rebalance
            self.rebalance()            
            # Update height
            self.height = 1 + max(self.left.height, self.right.height)    
                                
    # This function checks if one side of the tree is much taller than the other
    def rebalance(self):
        # Get the height of the left and right sides
        if self.left == None:
            left_side_height = 0
        else:
            left_side_height = self.left.height
        
        if self.right == None:
            right_side_height = 0
        else:
            right_side_height = self.right.height                        
        
        # If the LEFT side is more than 1 layer taller than the right:
        if left_side_height - right_side_height > 1:
            # Left-Left case
            if self.left.left.height > self.left.right.height:
                self.rightrotate()
            # Left-Right case
            if self.left.left.height < self.left.right.height:
                self.left.leftrotate()   
                self.rightrotate()       
            self.updateheight()        
            
        # If the RIGHT side is more than 1 layer taller than the left:
        if left_side_height - right_side_height < -1:
            # Right-Right case
            if self.right.left.height < self.right.right.height:
                self.leftrotate()
            # Right-Left case
            if self.right.left.height > self.right.right.height:
                self.right.rightrotate() 
                self.leftrotate()        
            self.updateheight()
            
    # Whenever we move things around, we need to recount the layers (heights)
    def updateheight(self):
        if self.isempty():
            return
        else:
            self.left.updateheight()
            self.right.updateheight()
            self.height = 1 + max(self.left.height, self.right.height)       
    
    # Printing the numbers in Sorted Order
    def inorder(self):
        if self.isempty():
            return([])
        else:
            return(self.left.inorder() + [self.value] + self.right.inorder())

    # Printing Root first
    def preorder(self):
        if self.isempty():
            return([])
        else:
            return([self.value] + self.left.preorder() + self.right.preorder())

    # Printing children first
    def postorder(self):
        if self.isempty():
            return([])
        else:
            return(self.left.postorder() + self.right.postorder() + [self.value])

# --- START OF PROGRAM ---

# 1. Create a blank Tree 'Family'
my_avl_tree = AVLTree()

# 2. Get list of numbers
node_values = eval(input("Please enter a list of numbers to put in the tree (e.g., [4, 2, 8]): "))

# 3. Insert each number
for number in node_values:
    my_avl_tree.insert(number)

# 4. Show the results!
print("\n--- Tree Sorted (Inorder) ---")
print(my_avl_tree.inorder())

print("\n--- Tree structure (Preorder) ---")
print(my_avl_tree.preorder())

print("\n--- Tree structure (Postorder) ---")
print(my_avl_tree.postorder())



