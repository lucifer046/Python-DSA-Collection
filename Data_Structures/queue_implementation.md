<!-- +------------------------------------------+ -->
<!-- |  QUEUE — FIRST IN, FIRST OUT (FIFO)      | -->
<!-- +------------------------------------------+ -->
# Queue — First In, First Out (FIFO)

## What is a Queue?

Think of a **cinema ticket counter**.

- When a new customer arrives, they join at the **BACK** of the line.
- The ticket seller only talks to the person at the very **FRONT**.
- The person who has been **waiting the longest** is always served first!

> **Simple Definition:** A Queue is a data structure where the **first item added** is the **first item removed**. This rule is called **FIFO — First In, First Out**.

---

## The Two Main Operations

| Operation | What it Does | Real-Life Analogy |
|---|---|---|
| **ENQUEUE** | Add a new item to the **BACK** | Customer joins the back of the line |
| **DEQUEUE** | Remove the item from the **FRONT** | Customer at the front gets served |

---

## Visual Representation

![Queue "FIFO" Ticket Line Diagram](docs/images/queue_diagram.png)

> [!NOTE]
> **Teacher's Perspective:** "Think of a **Cinema Ticket Counter**! When a new customer arrives, they join at the **BACK** of the line (Enqueue). The ticket seller only talks to the person at the very **FRONT** (Dequeue). The person who has been waiting the longest is always served first! This fair rule is called **FIFO**—First In, First Out."

---

## Step-by-Step Breakdown (Teacher's Guide)

Let's build a queue with the numbers `[10, 20, 30, 40]`:

### 1. Joining the Line (The "Enqueue" Phase)
- **Enqueue 10:** 10 is the first person in line. He's at the **Front** AND the **Back**.
- **Enqueue 20:** 20 joins the back. Now 10 is at the Front, 20 is at the Back.
- **Enqueue 30:** 30 joins behind 20.
- **Enqueue 40:** 40 is now the last person in line.

### 2. Being Served (The "Dequeue" Phase)
The ticket seller only speaks to the person at the **Front**:
1. **Dequeue:** 10 is at the front, so 10 is served first.
2. **Dequeue:** Now 20 has moved to the front. He's served next.
3. **Dequeue:** 30 is now at the front.
4. **Dequeue:** Finally, 40 is served. The line is now empty!

---

## Why is this so useful?
The Queue is the "Fairness King" of your computer. When you send 5 documents to a **Printer**, they don't print in random order—they print in exactly the order you sent them! When millions of people visit a website, a **Web Server** puts them in a queue so everyone gets served fairly.

---


---

## Where Are Queues Used in Real Life?

| Use Case | How Queue Works |
|---|---|
| **Printer** | Documents print in the order you sent them |
| **Web Server** | When millions visit a website, requests are queued |
| **Customer Support** | "You are caller #5 in the queue" |
| **Loading Screen** | Tasks load one by one in order |

---

## Key Takeaways

1. A Queue follows the **FIFO** rule — First In, First Out
2. **ENQUEUE** = Join the BACK, **DEQUEUE** = Served from the FRONT
3. Items come out in the **SAME order** they went in
4. It's the opposite of a Stack (Stack = reverse order, Queue = same order)
5. Used everywhere: printers, web servers, customer support lines

