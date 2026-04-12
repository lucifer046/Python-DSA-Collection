"""
================================================================================
CONCEPTS AND THEORY: BINARY HEAP (THE 'PRIORITY TRIAGE')
================================================================================

--- TIME COMPLEXITY ANALYSIS ---
- GET MIN/MAX (Root):    O(1) (Always at the top)
- INSERTION:             O(log n) (Must bubble up to its place)
- EXTRACTION (Root):     O(log n) (Must bubble down new root)
- UPDATE (Known Index):  O(log n) 
- UPDATE (By Value):     O(n) (Must search linearly first)
- HEAP SORT:             O(n log n)
--------------------------------
- SPACE COMPLEXITY: O(n) (Stored in a contiguous array)

STATUS: COMPLETE (Supports Min-Heap, Max-Heap, and HeapSort)
================================================================================

1. WHAT IS A BINARY HEAP?
   A Binary Heap is a 'Semi-Sorted' tree structure that is always 
   represented as an **ARRAY**. It is a 'Complete Binary Tree' - all 
   levels are full except possibly the last, which is filled left to right.

2. THE HEAP PROPERTY:
   - **MIN-HEAP**: Parent <= Children. (Smallest value is always at the Root)
   - **MAX-HEAP**: Parent >= Children. (Largest value is always at the Root)

3. ARRAY MAPPING (The Math):
   For any element at index 'i':
   - Parent Index: (i - 1) // 2
   - Left Child:   2*i + 1
   - Right Child:  2*i + 2

4. KEY OPERATIONS:
   - **Heapify Up**: Used when inserting at the bottom; we 'swap' the 
     new value upwards until it finds its rank.
   - **Heapify Down**: Used when removing the root; we move the last 
     element to the top and 'sink' it down until it finds its rank.

5. REAL LIFE EXAMPLE:
   Think of a **HOSPITAL EMERGENCY ROOM (Triage)**. 
   - New patients arrive with different priority levels.
   - The computer doesn't sort every single patient perfectly from 1 to 100.
   - It only cares that the **CHIEF SURGEON** (the Root) always has 
     the highest priority case.
   - When one patient is treated, the next most urgent one 'bubbles up'.
================================================================================
"""

class MinHeap:
    """
    A Min-Heap implementation from scratch.
    The parent is always smaller than its children.
    """
    def __init__(self):
        # We use a standard Python list to store our heap elements.
        self.heap = []

    def _parent(self, i):
        """ Returns the index of the parent node. """
        return (i - 1) // 2

    def _left_child(self, i):
        """ Returns the index of the left child. """
        return 2 * i + 1

    def _right_child(self, i):
        """ Returns the index of the right child. """
        return 2 * i + 2

    def insert(self, val):
        """ 
        1. Add new value to the end of the array.
        2. 'Heapify Up' to restore the Min-Heap property.
        """
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, i):
        """
        Compares the node with its parent and swaps if the node is smaller.
        Repeats until the root or until the parent is smaller.
        """
        # While we aren't at the root and the parent is bigger
        while i > 0 and self.heap[self._parent(i)] > self.heap[i]:
            # SWAP: Bring the smaller child up, push parent down
            self.heap[self._parent(i)], self.heap[i] = self.heap[i], self.heap[self._parent(i)]
            i = self._parent(i) # Move up to the next parent

    def extract_min(self):
        """
        1. Capture the root (the minimum).
        2. Move the last element to the root.
        3. 'Heapify Down' to restore order.
        """
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        # 1. Store the smallest element to return later
        root = self.heap[0]
        
        # 2. Overwrite the root with the last element and remove last
        self.heap[0] = self.heap.pop()
        
        # 3. Sink the new root down to its correct position
        self._heapify_down(0)
        return root

    def _heapify_down(self, i):
        """
        Compares node with children and swaps with the SMALLEST child.
        """
        smallest = i
        left = self._left_child(i)
        right = self._right_child(i)

        # 1. Find the smallest among Parent, Left Child, and Right Child
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        # 2. If one of the children was smaller, swap and recurse down
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._heapify_down(smallest)

    def update_at_index(self, index, new_val):
        """
        Updates a specific index. 
        If new value is smaller than old, bubble UP.
        If new value is larger than old, sink DOWN.
        """
        if index < 0 or index >= len(self.heap):
            return False
        
        old_val = self.heap[index]
        self.heap[index] = new_val
        
        if new_val < old_val:
            self._heapify_up(index)
        else:
            self._heapify_down(index)
        return True

    def update_value(self, old_val, new_val):
        """ 
        Linear search (O(n)) to find a value, then O(log n) update.
        """
        try:
            # Find the first occurrence of old_val
            index = self.heap.index(old_val)
            return self.update_at_index(index, new_val)
        except ValueError:
            return False

    def get_min(self):
        """ Returns the min without removing it. O(1). """
        return self.heap[0] if self.heap else None

    def __str__(self):
        return str(self.heap)


class MaxHeap:
    """
    A Max-Heap implementation from scratch.
    The parent is always larger than its children.
    """
    def __init__(self):
        self.heap = []

    def _parent(self, i):
        return (i - 1) // 2

    def _left_child(self, i):
        return 2 * i + 1

    def _right_child(self, i):
        return 2 * i + 2

    def insert(self, val):
        """ Standard max-heap insertion. """
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, i):
        """ Bubbles up larger elements. """
        while i > 0 and self.heap[self._parent(i)] < self.heap[i]:
            self.heap[self._parent(i)], self.heap[i] = self.heap[i], self.heap[self._parent(i)]
            i = self._parent(i)

    def extract_max(self):
        """ Extractions the largest element (root). """
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_down(self, i):
        """ Sinks down smaller root elements. """
        largest = i
        left = self._left_child(i)
        right = self._right_child(i)

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._heapify_down(largest)

    def update_at_index(self, index, new_val):
        """ Update and re-heapify based on Max-Heap rules. """
        if index < 0 or index >= len(self.heap):
            return False
        
        old_val = self.heap[index]
        self.heap[index] = new_val
        
        if new_val > old_val:
            self._heapify_up(index)
        else:
            self._heapify_down(index)
        return True

    def get_max(self):
        return self.heap[0] if self.heap else None

    def __str__(self):
        return str(self.heap)


# ==============================================================================
# HEAP SORT FUNCTIONS
# ==============================================================================

def heap_sort_min(arr):
    """
    Utilizes a Min-Heap to extract elements in ascending order.
    1. Insert all items into Min-Heap: O(n log n).
    2. Extract all items: O(n log n).
    Result is a sorted list.
    """
    h = MinHeap()
    for x in arr:
        h.insert(x)
    
    sorted_arr = []
    while h.heap:
        sorted_arr.append(h.extract_min())
    return sorted_arr

def heap_sort_max(arr):
    """
    Utilizes a Max-Heap to extract elements (Descending).
    Reverse the result to get Ascending order.
    """
    h = MaxHeap()
    for x in arr:
        h.insert(x)
    
    sorted_arr = []
    while h.heap:
        sorted_arr.append(h.extract_max())
    return sorted_arr[::-1] # Reverse to get Ascending


# ==============================================================================
# START OF PROGRAM (DEMO)
# ==============================================================================

if __name__ == "__main__":
    test_nums = [4, 10, 3, 5, 1]
    
    print("Welcome to the Binary Heap Implementation Demo!\n")
    
    # --- Min-Heap Build ---
    print("Building a Min-Heap step-by-step:")
    min_h = MinHeap()
    for n in test_nums:
        min_h.insert(n)
        print(f"Added {n:2} -> Heap: {min_h}")
    
    print(f"\nSmallest element (Root): {min_h.get_min()}")
    
    # --- Update Demo ---
    print(f"\nUpdating value 10 to 2...")
    min_h.update_value(10, 2)
    print(f"Heap after update: {min_h}")
    
    # --- Heap Sort Demo ---
    print("\n--- Heap Sort Performance ---")
    data = [42, 7, 18, 99, 1, 33]
    print(f"Original Array: {data}")
    print(f"Sorted (via MinHeap): {heap_sort_min(data)}")
    print(f"Sorted (via MaxHeap): {heap_sort_max(data)}")

    print("\nExtraction Process (Min-Heap):")
    while min_h.heap:
        val = min_h.extract_min()
        print(f"Extracted {val:2} | Remaining: {min_h}")

    print("\nAll operations completed successfully!")
