"""
================================================================================
CONCEPTS AND THEORY: BALANCED BINARY SEARCH TREE (AVL TREE)
================================================================================

--- TIME COMPLEXITY ANALYSIS ---
- SEARCH:       O(log n) (Guaranteed because the tree always stays balanced!)
- INSERT:       O(log n) 
- DELETE:       O(log n) 
- BEST CASE:    O(1) (Target is found exactly at the root)
- AVERAGE CASE: O(log n)
- WORST CASE:   O(log n)
--------------------------------
- SPACE COMPLEXITY: O(n) (To store every node in the tree)

STATUS: INDEPENDENT (Self-contained AVL Tree implementation)
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
    Self-balancing binary search tree.
    Guarantees O(log n) search time.
    """

    def __init__(self, val=None):
        # 1. v: value stored in this specific node
        self.v = val # v = value (integer/data)
        
        # 2. Check if this is a real node or just an empty seat
        if self.v is not None:
            # 3. l: left child link (points to smaller numbers)
            self.l = AVLTree() # l = left subtree
            # 4. r: right child link (points to larger numbers)
            self.r = AVLTree() # r = right subtree
            # 5. h: height of the node (max path to a leaf)
            self.h = 1 # h = height tracker
        else:
            # 6. Ghost node initialization (empty placeholder)
            self.l = None # no left child exists here
            self.r = None # no right child exists here
            self.h = 0 # height of empty space is zero
        return

    def is_empty(self):
        """ Returns True if the node is a placeholder (no value). """
        return (self.v == None) # check if value is None

    def is_leaf(self):
        """ Returns True if the node has a value but no children. """
        # check if value exists AND both left/right children are empty
        return (self.v != None and self.l.is_empty() and self.r.is_empty())

    def rotate_l(self):
        """ Left Rotation: Shifting the tree to fix a Right-Heavy tilt. """
        # 1. ov: backup old root value
        ov = self.v # ov = old value
        # 2. nv: grab value of the right child (the new leader)
        nv = self.r.v # nv = new value
        # 3. ol: backup the current left subtree
        ol = self.l # ol = old left
        # 4. mb: middle branch (left subtree of the right child)
        mb = self.r.l # mb = mid branch
        # 5. rb: rightmost branch (right subtree of the right child)
        rb = self.r.r # rb = right branch
        
        # 6. Build the new left child using old root and middle branch
        nl = AVLTree(ov) # nl = new left child
        nl.l = ol # attach old left subtree
        nl.r = mb # attach middle branch
        
        # 7. Update current node to reflect the new hierarchy
        self.v = nv # set current node value to nv
        self.r = rb # point right link to rb
        self.l = nl # point left link to nl (the new subtree)
        return

    def rotate_r(self):
        """ Right Rotation: Shifting the tree to fix a Left-Heavy tilt. """
        # 1. Store temporary variables for the pivot shift
        ov = self.v # ov = old value
        nv = self.l.v # nv = new value
        lb = self.l.l # lb = left branch
        mb = self.l.r # mb = middle branch
        or_sub = self.r # or_sub = old right subtree
        
        # 2. Re-anchor nodes to balance out the tree
        nr = AVLTree(ov) # nr = new right child
        nr.l = mb # attach middle branch to the left of new right child
        nr.r = or_sub # attach old right subtree to the right
        
        # 3. Finalize the root node transition
        self.v = nv # current node takes value of left child
        self.l = lb # link to leftmost branch
        self.r = nr # link to the newly constructed right subtree
        return

    def insert(self, x):
        """ Inserts a new value x and rebalances the tree. """
        # 1. Base case: If current spot is empty, take the seat
        if self.is_empty():
            self.v = x # set value to x
            self.l = AVLTree() # create empty left slot
            self.r = AVLTree() # create empty right slot
            self.h = 1 # starting height is 1
            return        
        
        # 2. Prevent duplicate entries
        if self.v == x: return        
        
        # 3. If x is smaller than current value, go left
        if x < self.v:
            self.l.insert(x) # recursive insertion on left
            self.rebalance() # check for balance violations
            # 4. Update current node's height based on children
            self.h = 1 + max(self.l.h, self.r.h) # add 1 to tallest child
            
        # 5. If x is larger than current value, go right
        else:
            self.r.insert(x) # recursive insertion on right
            self.rebalance() # perform AVL rebalancing checks           
            self.h = 1 + max(self.l.h, self.r.h) # update height
                                
    def rebalance(self):
        """ Checks balance factors and performs rotations if needed. """
        # 1. hl/hr: calculate heights of sub-branches
        hl = self.l.h if self.l else 0 # hl = left height
        hr = self.r.h if self.r else 0 # hr = right height
        
        # 2. Trigger: Left side is too heavy (gap > 1)
        if hl - hr > 1:
            # 3. Logic: Determine if it is a simple tilt or a zigzag
            if self.l.l.h > self.l.r.h: self.rotate_r() # simple left-left
            else:
                self.l.rotate_l() # double tilt fix (left-right)
                self.rotate_r()       
            self.update_h() # recalculate heights after rotation
            
        # 4. Trigger: Right side is too heavy (gap < -1)
        elif hl - hr < -1:
            # 5. Case detection for right-side tilts
            if self.r.l.h < self.r.r.h: self.rotate_l() # simple right-right
            else:
                self.r.rotate_r() # double tilt fix (right-left)
                self.rotate_l()        
            self.update_h() # refresh height data
            
    def update_h(self):
        """ Recomputes heights top-down for the whole subtree. """
        if self.is_empty(): return
        self.l.update_h() # refresh left subtree height
        self.r.update_h() # refresh right subtree height
        # self height is 1 plus the taller of the two children
        self.h = 1 + max(self.l.h, self.r.h) 
    
    def inorder(self):
        """ Traversal: Left -> Root -> Right (produces sorted list). """
        return [] if self.is_empty() else self.l.inorder() + [self.v] + self.r.inorder()

    def preorder(self):
        """ Traversal: Root -> Left -> Right (visualizes root hierarchy). """
        return [] if self.is_empty() else [self.v] + self.l.preorder() + self.r.preorder()

# --- START OF PROGRAM ---

# T: initialize a blank AVL Tree, L: list of test numbers
T = AVLTree()
L = [4, 2, 8, 1, 5, 9, 3]

print("AVL Balanced Binary Search Tree Simulator (The Smart Librarian)!\n")
print(f"Feeding numbers into the tree: {L}")

# Process insertions one by one
for n in L: # n: current number to add
    T.insert(n)

# Display the sorted outcome and the structural hierarchy
print(f"\nFinal Sorted List:  {T.inorder()} ✅")
print(f"Final Tree Layout:  {T.preorder()}")

print("\nAVL Tree is perfectly Balanced! ⚖️")
