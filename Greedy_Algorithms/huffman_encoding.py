"""
================================================================================
CONCEPTS AND THEORY: HUFFMAN ENCODING (DATA COMPRESSION)
================================================================================

--- TIME COMPLEXITY ANALYSIS ---
- SIMPLE VERSION: O(n^2) (Repeatedly sorting the list to find minimums)
- HEAP VERSION:   O(n log n) (Using a Min-Heap/Priority Queue for efficiency)
- BEST/AVG/WORST: O(n log n) (For the optimized heap version)
--------------------------------
- SPACE COMPLEXITY: O(n) (To store the Huffman tree and resulting code map)

STATUS: INDEPENDENT (Contains both a simple and a heap-optimized implementation)
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

6. REAL LIFE EXAMPLE:
   Think of **Morse Code**. In Morse code, the letter 'E' is just a single dot (.)
   because it's the most common letter in English. A rare letter like 'Q' is 
   much longer (--.-). This is exactly what Huffman Encoding does for computer files!
================================================================================
"""

from heapq import heappush, heappop, heapify # h: heap tools for efficiency

# --- NODE CLASS ---
class Node:
    """ A single spot in the Huffman Tree. """
    def __init__(self, f, s=None, l=None, r=None):
        # f: frequency, s: symbol letter, l/r: children links
        self.f = f # f = frequency count
        self.s = s # s = character symbol (e.g. 'A')
        self.l = l # l = left child (path 0)
        self.r = r # r = right child (path 1)
        
    def __lt__(self, other):
        # Comparison used by Heap to prioritize smaller frequencies
        return self.f < other.f

# ================================================================================
# VERSION 1: SIMPLE HUFFMAN (USING SORTING)
# ================================================================================

def huffman_simple(txt):
    """ Builds codes by repeatedly sorting leaf nodes. """
    # 1. f_list: frequency list of unique chars in txt
    chars = set(txt) # get unique characters
    # create leaf nodes for each char
    nodes = [Node(txt.count(c), c) for c in chars] # c = character
    
    # 2. Tree Building Loop: connect nodes with lowest frequencies
    while len(nodes) > 1:
        # sort nodes from rarest to most frequent
        nodes.sort(key=lambda n: n.f) # n: node iterator
        
        # 3. Take two rarest nodes as left (l) and right (r)
        l, r = nodes.pop(0), nodes.pop(0) # l: rarest, r: next rarest
        
        # 4. Create a parent (p) merging their data
        p = Node(l.f + r.f, l.s + r.s, l, r) # p = parent node
        nodes.append(p) # put parent back into pool
        
    # 5. Extract Huffman Codes from the resulting tree root root
    root = nodes[0] # the only node left is the root
    res = {} # res: results map {char: binary_code}
    
    # Trace code for each char by walking down the tree
    for c in chars:
        curr = root # curr: current node in walk
        code = "" # code: binary string being built
        while c != curr.s:
            if c in curr.l.s:
                code += "0"; curr = curr.l # walk left
            else:
                code += "1"; curr = curr.r # walk right
        res[c] = code # save code for char c
        
    return res

# ================================================================================
# VERSION 2: OPTIMIZED HUFFMAN (USING MIN-HEAP)
# ================================================================================

def huffman_heap(txt):
    """ Uses a Min-Heap (heapq) for O(n log n) efficiency. """
    # 1. Count frequencies and create initial Priority Queue (Heap)
    counts = {c: txt.count(c) for c in set(txt)} # c: character
    # pq: priority queue list of Leaf nodes
    pq = [Node(f, c) for c, f in counts.items()] 
    heapify(pq) # transform list into a min-heap structure
    
    # 2. Build the Huffman tree greedily
    while len(pq) > 1:
        # 3. Instantly pop the two lightest nodes (i, j)
        i = heappop(pq) # i: minimum frequency node
        j = heappop(pq) # j: next minimum
        
        # 4. Push their parent back into the heap
        p = Node(i.f + j.f, i.s + j.s, i, j) # combined parent
        heappush(pq, p) # auto-reorders the heap
        
    # 5. Result Extraction (recursive helper is cleaner for heaps)
    root = heappop(pq) # root of the final tree
    codes = {} # codes: final mapping
    
    def walk(node, cur_bits):
        """ Recursively traverses the tree to find leaf codes. """
        # node: current node, cur_bits: binary path string
        if len(node.s) == 1: # found a single character leaf
            codes[node.s] = cur_bits
            return
        walk(node.l, cur_bits + "0") # branch left (0)
        walk(node.r, cur_bits + "1") # branch right (1)
        
    walk(root, "") # start walk from tree root
    return codes

# --- START OF PROGRAM ---

# T: raw test string for compression
T = 'abbcaaaabbcdddeee'

print("Huffman Data Compression Simulator!\n")

print("--- Testing Version 1: Simple Sorting ---")
codes1 = huffman_simple(T)
for ch in sorted(codes1): print(f" '{ch}': {codes1[ch]}")

print("\n--- Testing Version 2: Optimized Heap ---")
codes2 = huffman_heap(T)
for ch in sorted(codes2): print(f" '{ch}': {codes2[ch]}")

print("\nCompression Successful! 📊")
