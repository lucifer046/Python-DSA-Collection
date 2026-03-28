<!-- +------------------------------------------+ -->
<!-- |  STACK — LAST IN, FIRST OUT (LIFO)       | -->
<!-- +------------------------------------------+ -->
# Stack — Last In, First Out (LIFO)

## What is a Stack?

Think of a **stack of dinner plates**.

- When you wash a plate, you place it on **TOP** of the pile.
- When you need a plate, you take the one from the **TOP**.
- You **never** pull a plate from the middle — everything above it would crash!

> **Simple Definition:** A Stack is a data structure where the **last item added** is always the **first item removed**. This rule is called **LIFO — Last In, First Out**.

---

## The Two Main Operations

| Operation | What it Does | Real-Life Analogy |
|---|---|---|
| **PUSH** | Add a new item to the **TOP** | Place a plate on top of the pile |
| **POP** | Remove the item from the **TOP** | Take a plate from the top of the pile |

---

## Step-by-Step Example

### PUSH Operations — Building the Stack

**Push 10:**  
```
  +------+
  |  10  |  < TOP
  +------+
```

**Push 20:**  
```
  +------+
  |  20  |  < TOP (new!)
  +------+
  |  10  |
  +------+
```

**Push 30:**  
```
  +------+
  |  30  |  < TOP (new!)
  +------+
  |  20  |
  +------+
  |  10  |
  +------+
```

**Push 40:**  
```
  +------+
  |  40  |  < TOP (new!)
  +------+
  |  30  |
  +------+
  |  20  |
  +------+
  |  10  |  < BOTTOM
  +------+
```

### POP Operations — Removing from the Stack

**Pop (removes 40):**  
```
  +------+
  |  40  |  < REMOVED! ❌
  +------+                      Result:    +------+
  |  30  |                                 |  30  |  < NEW TOP
  +------+                      ------>    +------+
  |  20  |                                 |  20  |
  +------+                                 +------+
  |  10  |                                 |  10  |
  +------+                                 +------+

  Popped value: 40
```

**Pop again (removes 30):**  
```
  +------+
  |  30  |  < REMOVED! ❌
  +------+                      Result:    +------+
  |  20  |                                 |  20  |  < NEW TOP
  +------+                      ------>    +------+
  |  10  |                                 |  10  |
  +------+                                 +------+

  Popped value: 30
```

---

## Complete Flow Diagram

```
  PUSH 10    PUSH 20    PUSH 30    PUSH 40      POP        POP
  -------    -------    -------    -------    -------    -------
  +----+     +----+     +----+     +----+     +----+     +----+
  | 10 |     | 20 |     | 30 |     | 40 |     | 30 |     | 20 |
  +----+     +----+     +----+     +----+     +----+     +----+
             | 10 |     | 20 |     | 30 |     | 20 |     | 10 |
             +----+     +----+     +----+     +----+     +----+
                        | 10 |     | 20 |     | 10 |
                        +----+     +----+     +----+
                                   | 10 |
                                   +----+
```

Notice: Items come out in **REVERSE** order! We pushed 10, 20, 30, 40 — and they pop out as 40, 30, 20, 10.

---

## Where Are Stacks Used in Real Life?

| Use Case | How Stack Works |
|---|---|
| **Undo button** (Ctrl+Z) | Your last action is on top. Pressing Undo removes it (pops). |
| **Browser Back button** | Every page you visit is pushed. Clicking Back pops the current page. |
| **Function calls in programs** | When a function calls another function, the computer "pushes" it. When it finishes, it "pops" back. |

---

## Key Takeaways

1. A Stack follows the **LIFO** rule — Last In, First Out
2. You can only touch the **TOP** — no peeking at the middle!
3. **PUSH** = Add to the top, **POP** = Remove from the top
4. Items come out in **reverse order** from how they went in
5. Stacks are used everywhere: Undo history, browser back, function calls
