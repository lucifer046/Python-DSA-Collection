<!-- +---------------------------------------------+ -->
<!-- |  TOPOLOGICAL SORT — THE TASK SCHEDULER       | -->
<!-- +---------------------------------------------+ -->

# Topological Sort — The Task Scheduler

## What is Topological Sort?

Imagine you're **getting dressed** in the morning. You can't put on **shoes before socks**, and you can't put on a **shirt before undershirt**. Some tasks MUST happen before others!

**Topological Sort** finds a **legal order** to complete all tasks so that every task starts AFTER its prerequisites are done.

> **Simple Definition:** Given tasks with dependencies (Task A must finish before Task B can start), Topological Sort finds a valid order to complete all tasks.

## 🖼️ Visual Representation

```mermaid
graph LR
    A((1. Socks)) --> B((2. Shoes))
    C((3. Undershirt)) --> D((4. Shirt))
    D --> E((5. Jacket))
    B --> F((6. Ready!))
    E --> F
    style A fill:#4f46e5,color:#fff
    style B fill:#4f46e5,color:#fff
    style C fill:#ec4899,color:#fff
    style D fill:#ec4899,color:#fff
    style E fill:#ec4899,color:#fff
    style F fill:#10b981,color:#fff
```

> [!NOTE]
> **Teacher's Perspective:** "Imagine you're **getting dressed** 👔 in the morning. You can't put on your shoes before your socks, and your jacket must come after your shirt. **Topological Sort** is your personal 'Task Planner.' It looks at all your tasks and their rules (dependencies) and creates a perfect **legal sequence**. It ensures that by the time you reach any task, every single one of its prerequisites is already finished!"

---

## 🎓 Step-by-Step Breakdown (Teacher's Guide)

Let's organize our task list:

### 1. The "Prerequisite Count" (In-Degree)

First, we look at every task and count how many other tasks must finish before it (we call this its **In-Degree**).

- Tasks with **0 In-Degree** are "Ready to Start" right now (like your socks!).

### 2. Picking the Ready Tasks

- We start our To-Do list by picking all tasks that have **0 prerequisites**.
- Let's say we pick "Socks."

### 3. Knocking Out the Hurdles

- Once "Socks" is finished, we look at the tasks that were waiting for it (like "Shoes").
- We reduce the prerequisite count for "Shoes" by 1.
- If "Shoes" now has **0 prerequisites**, it becomes "Ready to Start"!

### 4. Mission AccomplISHED

We keep repeating this—pick a ready task, knock out its dependencies, and find new ready tasks—until every single task is finished. If we get stuck, it means we have a **circular dependency** (like needing a key that is locked inside the box the key opens!), which topological sort neatly helps us identify as impossible!

---

## 🧠 Why is it a "Task Scheduler"?

Topological Sort is the brain behind how **Excel** recalculates formulas, how **compilers** build software from thousands of files, and how **NASA** schedules complex space missions. It ensures nothing happens a second before it's supposed to!

---

---

## Real-Life Examples

### Getting Dressed:

```
  Socks > Shoes
  Underwear > Pants > Shoes
  Shirt > Jacket

  Valid order: Underwear, Socks, Shirt, Pants, Jacket, Shoes ✅
  Invalid:    Shoes, Socks ❌ (Can't put shoes before socks!)
```

### University Course Planning:

```
  Math 101 > Math 201 > Math 301
  CS 101 > CS 201
  Math 101 > CS 201

  Valid: Math 101, CS 101, Math 201, CS 201, Math 301 ✅
```

---

## Key Takeaways

1. Topological Sort finds a **valid ordering** of tasks with dependencies
2. It only works on **DAGs** (Directed Acyclic Graphs) — no circular dependencies!
3. **In-Degree** = number of prerequisites a task has
4. Tasks are **ready** when their In-Degree drops to **0**
5. There may be **multiple valid orderings** — all are correct!
6. Used in **course planning, build systems, project management**
