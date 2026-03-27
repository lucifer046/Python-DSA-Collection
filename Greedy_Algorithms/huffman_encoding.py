"""
================================================================================
CONCEPTS AND THEORY: HUFFMAN ENCODING (DATA COMPRESSION)
================================================================================

1. WHAT IS IT?
   Usually, computers store every letter using the same amount of space (like 8 bits).
   But in real life, some letters are used ALL the time (like 'E' or 'A'), 
   while others are very rare (like 'Z' or 'Q'). 
   Storing them all with the same length is a waste of space!

2. THE HUFFMAN STRATEGY:
   Huffman Encoding is a way to compress data by:
   - Giving SHORT codes to frequent letters.
   - Giving LONG codes to rare letters.
   This way, the overall file size becomes much smaller!

3. THE PREFIX-FREE RULE:
   A critical rule here is that no code can be the start of another code. 
   (e.g., if 'A' is '0', 'B' cannot be '01'). This ensures the computer doesn't 
   get confused when reading the compressed 0s and 1s.

4. THE ALGORITHM STEPS:
   - 1. Count how many times each character appears (Frequency).
   - 2. Put each character into a 'Priority' list.
   - 3. Take the TWO rarest characters and merge them into a 'Parent' node.
   - 4. Put that parent back into the list and repeat until only one 'Root' remains.
   - 5. Trace the path: Left = 0, Right = 1.

5. HEAP OPTIMIZATION:
   - Without a Heap: We have to search the whole list to find the two rarest 
     characters every time (Slow).
   - With a Min-Heap: The rarest characters are always sitting right at the 
     top, so we can grab them instantly (Fast!).

6. TIME COMPLEXITY:
   - Simple Version: O(n^2) because of repeated sorting.
   - Heap Version: O(n log n), which is much better for large files.

7. REAL LIFE EXAMPLE:
   Think of **Morse Code**. In Morse code, the letter 'E' is just a single dot (.)
   because it's the most common letter in English. A rare letter like 'Q' is 
   much longer (--.-). This is exactly what Huffman Encoding does for computer files!

8. ALGORITHM VS. ENCODING:
   - THE ALGORITHM: The step-by-step 'recipe' we use to build the tree.
   - THE ENCODING: The final 'secret code' (result) we get at the end.
================================================================================
"""

# --- SHARED CLASS FOR BOTH VERSIONS ---

# A class represents a 'blueprint' for an object. 
# Think of this as a blueprint for a single 'Spot' in our tree.
class HuffmanNode:
    """
    A single spot (node) in our Huffman Tree.
    Each node stores a character, its frequency, and its two children.
    """
    def __init__(self, frequency, symbol=None, left_child=None, right_child=None):
        # 'self.frequency' stores how many times this letter appears
        self.frequency = frequency
        # 'self.symbol' is the actual letter (e.g., 'A')
        self.symbol = symbol  
        # 'self.left' is the '0' path (child) in the tree
        self.left = left_child
        # 'self.right' is the '1' path (child) in the tree
        self.right = right_child

# ================================================================================
# VERSION 1: SIMPLE HUFFMAN (NO HEAP)
# ================================================================================

# This function takes a string of text and finds the best codes
def huffman_simple(input_text):
    """
    Standard Huffman implementation that uses sorting to find the lowest frequencies.
    """
    # Create an empty dictionary to store the final result (e.g., 'A': '01')
    char_to_code_map = {}
    
    # Use 'set()' to extract every UNIQUE letter from our text
    unique_characters = set(input_text)
    
    # Create a blank list to store frequencies (counts) of each letter
    frequency_list = []
    
    # For every unique character we found in the text:
    for char in unique_characters:
        # Count how many times it appears and add it as a (count, character) pair
        frequency_list.append((input_text.count(char), char))
    
    # Create a blank list to store our tree 'nodes'
    node_list = []
    
    # For every (count, character) pair in our frequency list:
    for freq, char in sorted(frequency_list):
        # Create a new Node using our class and add it to our list
        # We store it as ((freq, char), Node) so it's easy to sort later
        node_list.append(((freq, char), HuffmanNode(freq, char)))
        
    # As long as we have more than one 'branch' left in our forest:
    while len(node_list) > 1:
        # Sort the whole list so the nodes with the SMALLEST frequencies are at the front
        node_list.sort()
        
        # Pull out the first node (lowest frequency) as the left child
        left_node = node_list[0][1]
        # Pull out the second node (next lowest) as the right child
        right_node = node_list[1][1]
        
        # Combine their frequencies to get the 'Parent' frequency
        combined_freq = left_node.frequency + right_node.frequency
        # Combine their letters so the parent 'contains' both (e.g., 'AB')
        combined_symbol = left_node.symbol + right_node.symbol
        
        # Create a NEW parent node that connects to these two children
        new_parent_node = HuffmanNode(combined_freq, combined_symbol, left_node, right_node)
        
        # Remove the two nodes we just used from the list
        node_list.pop(0) # Remove first
        node_list.pop(0) # Remove second (which is now at index 0)
        
        # Add our newly created 'parent' back into the list
        node_list.append(((combined_freq, combined_symbol), new_parent_node))

    # After merging everyone, the very last node left is the 'Top' of our whole tree
    root_node = node_list[0][1]

    # Now, for every unique character, let's trace its path from the top
    for char in unique_characters:
        # Start at the top of the tree
        current_node = root_node
        # Start with an empty string of 0s and 1s
        bit_code = ''
        
        # Keep moving down until the current spot only contains one letter (our target char)
        while char != current_node.symbol:           
            # Check: Is our character in the 'left' side's list of letters?
            if char in current_node.left.symbol:
                bit_code += '0'          # If yes, add '0' to the code
                current_node = current_node.left # And move the current pointer left
            # If it's not on the left, it MUST be on the right
            else:
                bit_code += '1'          # Add '1' to the code
                current_node = current_node.right # Move right
        
        # Once we found the letter, save the code we built for it
        char_to_code_map[char] = bit_code   
        
    # Give back the final map of all character codes
    return char_to_code_map

# ================================================================================
# VERSION 2: OPTIMIZED HUFFMAN (USING MIN-HEAP)
# ================================================================================

# A 'Heap' is like a pyramid where the smallest (lightest) item is always on top
class MinHeapManager:
    """
    A helper tool that keeps our nodes organized so the 'smallest' (rarest)
    is always easy to find at the top of the pyramid.
    """
    def __init__(self, initial_nodes):
        # 'heap_storage' is our internal list for the nodes
        self.heap_storage = initial_nodes
        # 'current_size' is how many nodes we currently have
        self.current_size = len(initial_nodes)
        # Call the special 'build_heap' function to organize the pyramid at the start
        self.build_heap()
    
    # Simple check: Is the heap empty?
    def is_empty(self):
        return len(self.heap_storage) == 0
    
    # This function moves an item down the pyramid if it's too 'heavy' for its spot
    def maintain_heap_property(self, start_index):
        # Find where its children would be in the list
        left_child_idx = 2 * start_index + 1
        right_child_idx = 2 * start_index + 2
        # Assume the current item is the smallest initially
        smallest_idx = start_index
        
        # If the left child exists and is LIGHTER (has fewer frequency count):
        if left_child_idx < self.current_size and self.heap_storage[left_child_idx][0][0] < self.heap_storage[smallest_idx][0][0]:
            smallest_idx = left_child_idx
            
        # If the right child exists and is even LIGHTER:
        if right_child_idx < self.current_size and self.heap_storage[right_child_idx][0][0] < self.heap_storage[smallest_idx][0][0]:
            smallest_idx = right_child_idx
            
        # If one of the children was actually the smallest:
        if smallest_idx != start_index:
            # Swap the parent with the lightest child
            self.heap_storage[smallest_idx], self.heap_storage[start_index] = self.heap_storage[start_index], self.heap_storage[smallest_idx]
            # Recursively call this function on the child's spot to keep it 'sinking'
            self.maintain_heap_property(smallest_idx)

    # Organizes the whole list into a valid Min-Heap (lightest things on top)
    def build_heap(self):
        # We start from the middle and move upwards, making every part 'sink' correctly
        for i in range((self.current_size // 2) - 1, -1, -1):
            self.maintain_heap_property(i)
    
    # Adds a new node to our pyramid
    def add_item(self, new_item):
        # Add the item to the very end of our list
        self.heap_storage.append(new_item)
        # Increase our size count
        self.current_size += 1
        # It's at the very end (index = size - 1)
        child_index = self.current_size - 1
        
        # Now we 'bubble' it UP if it's lighter than its parent
        while child_index > 0:
            parent_index = (child_index - 1) // 2
            # Compare frequencies (weights)
            if self.heap_storage[parent_index][0][0] > self.heap_storage[child_index][0][0]:
                # Swap them to move the lighter child up
                self.heap_storage[parent_index], self.heap_storage[child_index] = self.heap_storage[child_index], self.heap_storage[parent_index]
                # Move up to the next parent level
                child_index = parent_index
            else:
                # If parent is already lighter, stop!
                break
    
    # Takes the LIGHTEST (smallest frequency) item out of the top of the pyramid
    def remove_smallest_item(self):
        # If there's nothing here, just return None
        if self.is_empty():
            return None
        
        # Swap the top (smallest) item with the last item in the list
        self.heap_storage[0], self.heap_storage[-1] = self.heap_storage[-1], self.heap_storage[0]
        # 'Pop' (remove and get) the smallest item which is now at the end
        lightest_item = self.heap_storage.pop()
        # Decrease size count
        self.current_size -= 1
        
        # Re-organize from top-down so the NEW top item sinks if it's too heavy
        self.maintain_heap_property(0)
        # Return that lightest item to the user
        return lightest_item

# --- Optimized algorithm using our special Bucket (Min-Heap) ---
def huffman_with_heap(input_text):
    """
    Optimized Huffman implementation that uses a Min-Heap for maximum speed.
    """
    # 1. Preparation: split letters and count frequencies
    char_list = list(input_text)
    unique_chars = set(char_list)
    initial_nodes = []
    
    # Create the starting nodes for each character
    for char in unique_chars:
        # Count occurrences in the original text
        freq = char_list.count(char)
        # Store as ((freq, char), Node) for the heap to use
        initial_nodes.append(((freq, char), HuffmanNode(freq, char)))
    
    # 2. Put all nodes into our automated pyramid bucket (Min-Heap)
    heap_manager = MinHeapManager(initial_nodes)

    # 3. Build the Tree by merging the two lightest items repeatedly
    while heap_manager.current_size > 1:
        # Grab the lightest branch from the heap (log n speed)
        left_branch = heap_manager.remove_smallest_item()[1]
        # Grab the next lightest branch
        right_branch = heap_manager.remove_smallest_item()[1]
        
        # Merge them into a single parent node
        parent_freq = left_branch.frequency + right_branch.frequency
        parent_symbol = left_branch.symbol + right_branch.symbol
        new_parent = HuffmanNode(parent_freq, parent_symbol, left_branch, right_branch)
        
        # Push the new parent back into the heap bucket for the next round
        heap_manager.add_item(((parent_freq, parent_symbol), new_parent))

    # The very last node left in the bucket is the 'Root' (entire tree)
    final_root = heap_manager.remove_smallest_item()[1]
    
    # 4. Generate the 0s and 1s result map (same walking logic as the simple version)
    final_codes = {}
    for char in unique_chars:
        temp_node = final_root
        code_string = ''
        while char != temp_node.symbol:
            # If target character is on the left path, add '0'
            if char in temp_node.left.symbol:
                code_string += '0'
                temp_node = temp_node.left
            # Otherwise, move right and add '1'
            else:
                code_string += '1'
                temp_node = temp_node.right
        # Save the resulting code
        final_codes[char] = code_string
        
    return final_codes

# ================================================================================
# --- TEST PROGRAM ---
# ================================================================================

# This is our sample text to compress
test_string = 'abbcaaaabbcdddeee'

print("--- TESTING VERSION 1: SIMPLE HUFFMAN ---")
# Call the simple function and save the dictionary
simple_results = huffman_simple(test_string)
# Print each character and its code in alphabetical order
for letter in sorted(simple_results):
    print(f"'{letter}' code: {simple_results[letter]}")

print("\n--- TESTING VERSION 2: HEAP-OPTIMIZED HUFFMAN ---")
# Call the fast heap-optimized function
heap_results = huffman_with_heap(test_string)
for letter in sorted(heap_results):
    print(f"'{letter}' code: {heap_results[letter]}")
