<!-- +------------------------------------------+ -->
<!-- |  STACK USING QUEUES — THE BRAIN TEASER   | -->
<!-- +------------------------------------------+ -->
# Stack Implementation using Queues

## What is this Challenge?

In computer science, we often like to see if we can "rebuild" one tool using another. Here, the challenge is: **Can you build a Stack (LIFO) using only Queues (FIFO)?**

- **Stack (LIFO):** The last person to arrive is served first (like a stack of plates).
- **Queue (FIFO):** The first person to arrive is served first (like a line at the supermarket).

> **The Problem:** A Queue is designed to be "fair," but a Stack is "unfair" to the people who arrived first. To make a Queue act like a Stack, we have to do some heavy shuffling!

---

## Strategy 1: Using Two Queues

Think of this like having a **Main Room** and a **Waiting Room**.

### How it works (The Push Shuffe):
1. Every time a new person arrives, they go into the **Waiting Room**.
2. We then ask everyone in the **Main Room** to move into the **Waiting Room**, standing *behind* the new person.
3. Now, the new person is at the very front of the line!
4. We swap the room names. The Waiting Room becomes our new Main Room.

| Operation | Complexity | Why? |
|---|---|---|
| **PUSH** | **O(n)** | We move every single item from one queue to another. |
| **POP** | **O(1)** | The newest item is already at the front of the queue. |

---

## Strategy 2: Using Only One Queue

This is even more clever! We use a single line and make people **"Loop Around"**.

### How it works (The Rotation Trick):
1. Add the new person to the **BACK** of the line.
2. Now, for every person who was *already* in the line, ask them to leave the front and join the back again.
3. Once everyone has "cycled around," the person who just arrived is now at the very **FRONT**.

> [!TIP]
> **Visual Analogy:** Imagine a line of people. A new person joins at the end. Then, every person in front of them leaves the line and goes to the back, one by one, until the new person is the leader of the line.

---

## Visual Comparison

| | Stack (Normal) | Stack using Queues |
|---|---|---|
| **Storage** | A simple list/pile | One or more FIFO lines |
| **Push Speed** | Super Fast (O(1)) | Slow (O(n)) due to shuffling |
| **Pop Speed** | Super Fast (O(1)) | Super Fast (O(1)) |
| **Main Use** | Efficiency | Logic puzzles & Interviews |

---

## Why learn this?

1. **Interview Classic:** This is a very common question to test if you understand the fundamental difference between LIFO and FIFO.
2. **System Constraints:** In some very old or specialized hardware, you might only have a "Queue" buffer and need to implement "Undo" (Stack) logic.
3. **Logic Building:** It teaches you how to manipulate data structures to change their behavior.

---

## Key Takeaways

1. You can build a **Stack** using either **one** or **two** queues.
2. The "trick" is always to move the **newest** item to the **front** of the queue.
3. Because Queues only let you take from the front, we must shuffle items during the **Push** operation to keep them in the right order.
4. While this works perfectly, it is **slower** than a normal stack because of the extra shuffling (O(n) instead of O(1)).
