<!-- +------------------------------------------------------+ -->
<!-- |  HUFFMAN ENCODING — DATA COMPRESSION MADE SIMPLE    | -->
<!-- +------------------------------------------------------+ -->
# Huffman Encoding — Data Compression Made Simple

## What is Huffman Encoding?

Imagine you're sending a **secret message** using a walkie-talkie, but you can only say **"beep"** (0) and **"boop"** (1). Normally, every letter gets the same length code (like 8 beeps/boops each). But some letters are used way more often than others!

**Huffman Encoding** is a clever trick:
- Give **SHORT codes** to letters that appear often (like 'E' and 'A')
- Give **LONG codes** to letters that are rare (like 'Z' and 'Q')

This way, your message becomes **much shorter** overall!

> **Simple Definition:** Huffman Encoding compresses data by assigning shorter binary codes to frequent characters and longer codes to rare characters.

---

![Regular vs Huffman Comparison](docs/images/huffman_encoding_comparison.png)

![Huffman Encoding Tree Structure](docs/images/huffman_encoding_tree_diagram.png)

---

## Step-by-Step Example

### The Text: `abbcaaaabbcdddeee`

### Step 1: Count the frequency of each character

```
  +----------+-----------+
  | Character| Frequency |
  +----------+-----------+
  |    a     |     6     |  < Most common!
  |    b     |     3     |
  |    c     |     2     |
  |    d     |     3     |
  |    e     |     3     |  
  +----------+-----------+
  
  Total characters: 17
```

### Step 2: Build the Huffman Tree (Bottom-Up)

Start with every character as a **leaf node** sorted by frequency:

```
  [c:2]  [b:3]  [d:3]  [e:3]  [a:6]
```

**Round 1:** Take the TWO smallest (c:2, b:3), merge them:
```
       [cb:5]
      ╱      ╲
   [c:2]    [b:3]
   
  Remaining: [d:3]  [e:3]  [cb:5]  [a:6]
```

**Round 2:** Take the TWO smallest (d:3, e:3), merge them:
```
       [de:6]
      ╱      ╲
   [d:3]    [e:3]
   
  Remaining: [cb:5]  [a:6]  [de:6]
```

**Round 3:** Take the TWO smallest (cb:5, a:6), merge them:
```
        [cba:11]
       ╱        ╲
    [cb:5]     [a:6]
   ╱      ╲
[c:2]    [b:3]

  Remaining: [de:6]  [cba:11]
```

**Round 4 (Final):** Merge the last two:
```
               [ROOT:17]
              ╱          ╲
           [de:6]      [cba:11]
          ╱     ╲      ╱      ╲
       [d:3]  [e:3]  [cb:5]  [a:6]
                     ╱      ╲
                  [c:2]    [b:3]
```

### Step 3: Assign codes by tracing paths

**Rule:** Going **LEFT** = add **0**, Going **RIGHT** = add **1**

```
               [ROOT]
              ╱   0   ╲   1
           [de]         [cba]
         ╱ 0  ╲ 1     ╱ 0   ╲ 1
       [d]    [e]   [cb]     [a]
                   ╱ 0  ╲ 1
                 [c]    [b]
  
  Tracing paths from ROOT:
  d: LEFT, LEFT         > Code: 00
  e: LEFT, RIGHT        > Code: 01
  c: RIGHT, LEFT, LEFT  > Code: 100
  b: RIGHT, LEFT, RIGHT > Code: 101
  a: RIGHT, RIGHT       > Code: 11
```

### Step 4: Final Code Table

```
  +----------+-----------+----------+-------------------+
  | Character| Frequency |   Code   | Bits Used         |
  +----------+-----------+----------+-------------------+
  |    a     |     6     |    11    | 6 × 2 = 12 bits   |
  |    b     |     3     |   101    | 3 × 3 = 9 bits    |
  |    c     |     2     |   100    | 2 × 3 = 6 bits    |
  |    d     |     3     |    00    | 3 × 2 = 6 bits    |
  |    e     |     3     |    01    | 3 × 2 = 6 bits    |
  +----------+-----------+----------+-------------------+
  
  Total with Huffman: 12+9+6+6+6 = 39 bits
  Total with Fixed (3 bits each): 17 × 3 = 51 bits
  
  Space saved: 23.5%! 
```

---

## The Prefix-Free Rule

A critical rule: **No code can be the START of another code!**

```
  ✅ VALID codes:       ❌ INVALID codes:
  a = 0                  a = 0
  b = 10                 b = 01    < Starts with 'a's code (0)!
  c = 11                 c = 011
  
  Why? If a=0 and b=01, how would the computer read "001"?
  Is it "0, 01" (a, b) or "00, 1" (something else)?
  CONFUSION!
  
  Huffman codes are ALWAYS prefix-free because
  characters are only at LEAF nodes in the tree!
```

---

## Simple vs Heap Version

The code provides TWO implementations:

| Feature | Simple Version | Heap Version |
|---|---|---|
| **Finding 2 smallest** | Sort the entire list each time | Uses a Min-Heap (pyramid) |
| **Speed** | O(n²) — Slow for large data | O(n log n) — Fast! |
| **Concept** | Same tree-building logic | Same tree-building logic |

### What's a Min-Heap?

```
  A pyramid where the LIGHTEST (smallest) item is always on TOP!
  
        [2]         < Smallest always on top!
       ╱   ╲
     [5]   [3]
    ╱   ╲
  [8]   [6]
  
  Getting the smallest = O(1) — just grab the top!
  Adding a new item = O(log n) — bubble it up
```

---

## Real-Life Uses of Huffman Encoding

| Use Case | How It Helps |
|---|---|
| **ZIP files** | Compress files to take less disk space |
| **JPEG images** | Part of how photos are compressed |
| **MP3 audio** | Part of audio compression |
| **Network data transfer** | Send less data over the internet |

> **Fun Fact:** Morse Code uses a similar idea! 'E' (most common) = single dot (·), while 'Q' (rare) = dash-dash-dot-dash (--·-).

---

## Key Takeaways

1. **Frequent characters** get **short codes**, **rare characters** get **long codes**
2. Build a tree by repeatedly merging the **two rarest** characters
3. **LEFT = 0, RIGHT = 1** when reading the tree
4. Codes are **prefix-free** — no code starts with another code
5. Results in **significant space savings** (often 20-50% compression)
6. The **Heap version** is faster (O(n log n)) for large files
