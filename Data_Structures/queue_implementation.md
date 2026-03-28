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

## Step-by-Step Example

### ENQUEUE Operations — Building the Queue

**Enqueue 10:**  
```
  FRONT & BACK
       |
       v
    +------+
    |  10  |
    +------+
```

**Enqueue 20:**  
```
  FRONT       BACK
    |           |
    v           v
  +------+------+
  |  10  |  20  |
  +------+------+
```

**Enqueue 30:**  
```
  FRONT               BACK
    |                   |
    v                   v
  +------+------+------+
  |  10  |  20  |  30  |
  +------+------+------+
```

**Enqueue 40:**  
```
  FRONT                     BACK
    |                         |
    v                         v
  +------+------+------+------+
  |  10  |  20  |  30  |  40  |
  +------+------+------+------+
```

### DEQUEUE Operations — Serving from the Front

**Dequeue (serves 10):**  
```
  BEFORE:
  FRONT                              BACK
    |                                  |
    v                                  v
  +------+------+------+------+
  |  10  |  20  |  30  |  40  |
  +------+------+------+------+
    ^
    SERVED! ✅

  AFTER:
  FRONT                         BACK
    |                             |
    v                             v
  +------+------+------+
  |  20  |  30  |  40  |
  +------+------+------+

  Served customer: 10
```

**Dequeue again (serves 20):**  
```
  AFTER:
  FRONT                    BACK
    |                       |
    v                       v
  +------+------+
  |  30  |  40  |
  +------+------+

  Served customer: 20
```

---

## Complete Flow Diagram

```
  Action:    ENQUEUE 10  ENQUEUE 20  ENQUEUE 30  ENQUEUE 40  DEQUEUE     DEQUEUE
             ----------- ----------- ----------- ----------- ----------- -----------
  Queue:     [10]        [10, 20]    [10,20,30]  [10,20,30,40] [20,30,40]  [30, 40]
                                                                ^           ^
                                                            Served 10   Served 20
```

Notice: Items come out in the **SAME** order they went in! First in = First out!

---

## Stack vs Queue — The Big Difference

```
  STACK (LIFO):                 QUEUE (FIFO):
  +------+                     +------+------+------+
  |  30  | < IN/OUT from TOP   |  10  |  20  |  30  |
  +------+                     +------+------+------+
  |  20  |                       ^                ^
  +------+                      OUT               IN
  |  10  |                    (FRONT)            (BACK)
  +------+
  
  Stack: Last In, First Out     Queue: First In, First Out
  Like plates                   Like a ticket line
```

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
