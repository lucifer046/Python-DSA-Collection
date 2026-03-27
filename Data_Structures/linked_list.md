<!-- ╔══════════════════════════════════════════╗ -->
<!-- ║  LINKED LIST — THE CHAIN OF CLUES        ║ -->
<!-- ╚══════════════════════════════════════════╝ -->
# Linked List — The Chain of Clues

## What is a Linked List?

Imagine a **treasure hunt**! You find the first clue at the park. That clue gives you a **piece of treasure** (some data) and tells you **where the next clue is hidden**. You go to that location, find more treasure and another clue... and so on, until the last clue says: *"The hunt ends here!"*

That's exactly how a **Linked List** works in a computer!

> **Simple Definition:** A Linked List is a chain of small boxes called **Nodes**. Each box holds two things:
> 1. **A value** (your actual data — like a number)
> 2. **A pointer** (the address/location of the *next* box)

---

## How Does a Node Look?

```
┌──────────┬──────────┐
│  Value   │   Next   │ ──────▶ (points to the next node)
│  (Data)  │ (Pointer)│
└──────────┴──────────┘
```

Each node only knows **two things**: what it's holding, and who comes after it. That's it!

---

## Building a Linked List — Step by Step

Let's say we want to store the numbers **10, 20, 30, 40, 50** in a linked list.

### Step 1: Create the First Node (The Head)

```
    HEAD
     │
     ▼
  ┌──────┬──────┐
  │  10  │ None │
  └──────┴──────┘
```

We start with just **one node** holding the value `10`. Since there's no one after it, the "Next" pointer says `None` (which means "end of the line").

### Step 2: Append 20 (Add to the End)

```
    HEAD
     │
     ▼
  ┌──────┬───┐    ┌──────┬──────┐
  │  10  │ ──┼──▶ │  20  │ None │
  └──────┴───┘    └──────┴──────┘
```

We walk to the end of the chain (node 10), and attach a new node with value `20`.

### Step 3: Append 30, 40, 50

```
    HEAD
     │
     ▼
  ┌──────┬───┐   ┌──────┬───┐   ┌──────┬───┐   ┌──────┬───┐   ┌──────┬──────┐
  │  10  │ ──┼─▶ │  20  │ ──┼─▶ │  30  │ ──┼─▶ │  40  │ ──┼─▶ │  50  │ None │
  └──────┴───┘   └──────┴───┘   └──────┴───┘   └──────┴───┘   └──────┴──────┘
```

Now we have a **complete chain** of 5 nodes. The last node (50) has `None` — meaning there's nobody after it.

---

## How APPEND Works (Adding to the End)

There are two styles used in the code:

### Method 1: Recursive Append ("Pass the Parcel")

Imagine you're at a birthday party and you want to put a gift at the end of a line of gifts. You ask the first person: *"Are you the last one?"*. If they say no, they **pass the question** to the next person. This continues until someone says *"Yes, I'm last!"*, and they place the gift.

```
 "Am I last?" ──▶ "Am I last?" ──▶ "Am I last?" ──▶ "YES! I'll take it!"

  ┌──────┬───┐    ┌──────┬───┐    ┌──────┬──────┐    ┌──────┬──────┐
  │  10  │ ──┼──▶ │  20  │ ──┼──▶ │  30  │ None │──▶ │  40  │ None │ ← NEW!
  └──────┴───┘    └──────┴───┘    └──────┴──────┘    └──────┴──────┘
```

### Method 2: Iterative Append ("Walking")

Instead of passing messages, you personally **walk** from the first node all the way to the last one, and then attach the new node yourself.

```
  Walker starts here ──▶ walks ──▶ walks ──▶ reached the end! Attach new node!

  ┌──────┬───┐    ┌──────┬───┐    ┌──────┬──────┐
  │  10  │ ──┼──▶ │  20  │ ──┼──▶ │  30  │ None │
  └──────┴───┘    └──────┴───┘    └──────┴──────┘
       [walk] ────────▶ [walk] ────────▶ [walk] arrived! → Attach [40]
```

---

## Insert at Front (Adding at the Beginning)

What if we want to add a new number **at the very start** instead of the end?

### Before:
```
    HEAD
     │
     ▼
  ┌──────┬───┐    ┌──────┬───┐    ┌──────┬──────┐
  │  10  │ ──┼──▶ │  20  │ ──┼──▶ │  30  │ None │
  └──────┴───┘    └──────┴───┘    └──────┴──────┘
```

### Insert value 5 at front:

```
    HEAD
     │
     ▼
  ┌──────┬───┐    ┌──────┬───┐    ┌──────┬───┐    ┌──────┬──────┐
  │   5  │ ──┼──▶ │  10  │ ──┼──▶ │  20  │ ──┼──▶ │  30  │ None │
  └──────┴───┘    └──────┴───┘    └──────┴───┘    └──────┴──────┘
    ↑ NEW HEAD!
```

The trick used in the code is a **swap method**:
1. Create a new node with the new value
2. **Swap** the value of the head with the new node
3. **Re-link** the pointers so the new node comes first

---

## Delete a Node (Removing from the Chain)

Let's say we want to **remove the value 30** from our chain.

### Before:
```
  ┌──────┬───┐    ┌──────┬───┐    ┌──────┬───┐    ┌──────┬──────┐
  │  10  │ ──┼──▶ │  20  │ ──┼──▶ │  30  │ ──┼──▶ │  40  │ None │
  └──────┴───┘    └──────┴───┘    └──────┴───┘    └──────┴──────┘
```

### Step 1: Find 30
We walk through the chain: 10 → 20 → **30 found!**

### Step 2: Bypass it!
We make node 20 point **directly** to node 40, skipping 30 entirely.

### After:
```
  ┌──────┬───┐    ┌──────┬───┐    ┌──────┬──────┐
  │  10  │ ──┼──▶ │  20  │ ──┼──▶ │  40  │ None │
  └──────┴───┘    └──────┴───┘    └──────┴──────┘

                           ┌──────┬───┐
                           │  30  │   │  ← Disconnected! Gone!
                           └──────┴───┘
```

---

## Linked List vs Normal List (Array)

| Feature | Normal List (Array) | Linked List |
|---|---|---|
| **Accessing item #5** | [FAST] Instant (jump to index 5) | [SLOW] Walk through 5 nodes |
| **Adding at the end** | [FAST] | [SLOW] Needs to walk to end first |
| **Adding in the middle** | [SLOW] Shift everything | [FAST] Just change pointers |
| **Memory** | All items sit together | Items scattered everywhere |

---

## Key Takeaways

1. A Linked List is a **chain of nodes**, each pointing to the next one
2. The first node is called the **Head** — it's our entry point
3. The last node points to **None** — meaning "the chain ends here"
4. **Adding** to the chain = create a new node and link it
5. **Deleting** from the chain = bypass the node by re-linking its neighbors
6. It's great for **inserting** and **deleting**, but slow for **searching** (you can't jump to the middle!)
