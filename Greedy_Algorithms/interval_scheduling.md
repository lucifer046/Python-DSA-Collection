<!-- ╔══════════════════════════════════════════════════════╗ -->
<!-- ║  INTERVAL SCHEDULING — THE MEETING ROOM PROBLEM      ║ -->
<!-- ╚══════════════════════════════════════════════════════╝ -->
# Interval Scheduling — The Meeting Room Problem

## What is Interval Scheduling?

Imagine you have **one meeting room** and **8 friends** all want to use it. Each friend has a **start time** and an **end time** for their meeting. Your goal: **fit as many meetings as possible** without any overlap!

> **Simple Definition:** Given a list of tasks (each with a start time and end time), pick the **maximum number** of non-overlapping tasks.

---

## The Greedy Strategy

A **Greedy Algorithm** means: At each step, make the **best looking choice** right now, and hope it leads to the best overall result!

### Which "best choice" works?

| Strategy | Does it Work? |
|---|---|
| Pick the **shortest** meeting? | [X] Fails! A short meeting might overlap with two longer ones |
| Pick the one that **starts earliest**? | [X] Fails! It might be very long and block everything |
| Pick the one that **ends earliest**? | [done] YES! Finishing earliest leaves the most room for others |

> **The Optimal Rule: Always pick the meeting that ENDS EARLIEST!**

---

## Step-by-Step Example

### All Meeting Requests:

```
  Time:  0  1  2  3  4  5  6  7  8  9 10 11
         │  │  │  │  │  │  │  │  │  │  │  │
  A:        ████████░░░░░░░░░░░░░░░░░░░░░░    [1, 4]
  B:           ░░████████░░░░░░░░░░░░░░░░░    [3, 5]
  C:     ██████████████████░░░░░░░░░░░░░░░    [0, 6]
  D:              ░░░░░████████░░░░░░░░░░░    [5, 7]
  E:           ░░░░░░░░░░░░████████████░░░    [3, 8]
  F:              ░░░░░░░░░████████████████   [5, 9]
  G:                 ░░░░░░░░████████████████ [6, 10]
  H:                       ░░░░████████████████ [8, 11]
```

### Step 1: Sort all meetings by END TIME

```
  Sorted by end time:
  ┌─────────┬───────┬─────────┐
  │ Meeting │ Start │  End    │
  ├─────────┼───────┼─────────┤
  │    A    │   1   │   4 ←   │
  │    B    │   3   │   5     │
  │    C    │   0   │   6     │
  │    D    │   5   │   7     │
  │    E    │   3   │   8     │
  │    F    │   5   │   9     │
  │    G    │   6   │  10     │
  │    H    │   8   │  11     │
  └─────────┴───────┴─────────┘
```

### Step 2: Greedily pick meetings

```
  Room is free at time: 0

  Check A [1, 4]:  Start (1) ≥ Free time (0)?  YES → PICK A! [done]
  Room is now free at: 4

  Check B [3, 5]:  Start (3) ≥ Free time (4)?  NO → SKIP! [X] (Overlaps!)

  Check C [0, 6]:  Start (0) ≥ Free time (4)?  NO → SKIP! [X]

  Check D [5, 7]:  Start (5) ≥ Free time (4)?  YES → PICK D! [done]
  Room is now free at: 7

  Check E [3, 8]:  Start (3) ≥ Free time (7)?  NO → SKIP! ❌

  Check F [5, 9]:  Start (5) ≥ Free time (7)?  NO → SKIP! ❌

  Check G [6, 10]: Start (6) ≥ Free time (7)?  NO → SKIP! ❌

  Check H [8, 11]: Start (8) ≥ Free time (7)?  YES → PICK H! [done]
  Room is now free at: 11
```

### Result: 3 meetings booked!

```
  Time:  0  1  2  3  4  5  6  7  8  9 10 11
         │  │  │  │  │  │  │  │  │  │  │  │
  A:        ████████                            [1, 4]  [done] PICKED
  D:                    ████████                [5, 7]  [done] PICKED
  H:                             ████████████   [8, 11] [done] PICKED
  
  No overlaps! Maximum meetings = 3! 🎉
```

---

## Visual: Why "Earliest End" Works

```
  Strategy: Earliest END time

  ████  ████  ████████    3 meetings fit! [done]
  
  Strategy: Earliest START time

  ██████████████████████  Only 1 meeting fits! ❌
  (Because the first meeting was very long!)
```

By finishing early, we leave the **maximum room** for future meetings.

---

## Decision Flowchart

```
  For each meeting (sorted by end time):
  
  ┌─────────────────────────┐
  │ Does this meeting start │
  │ AFTER the last one      │     YES ──▶ PICK IT! [done]
  │ ended?                  │──────────▶ Update free time
  │                         │
  │                         │     NO ──▶ SKIP IT! ❌
  └─────────────────────────┘──────────▶ Check next meeting
```

---

## Real-Life Examples

| Scenario | How Greedy Scheduling Helps |
|---|---|
| **Hospital Consultant** | Fit the most patient appointments in a shift |
| **Conference Room** | Schedule the most presentations without overlap |
| **TV Broadcasting** | Choose which shows to air to fill the most time slots |
| **Job Scheduling** | Assign the most jobs to a single machine |

---

## Key Takeaways

1. **Sort by end time** (earliest first)
2. **Pick greedily** — if a meeting starts after the room is free, take it!
3. This gives the **maximum number** of non-overlapping meetings
4. Time complexity: **O(n log n)** (just the sorting step!)
5. This is mathematically **proven** to be the optimal strategy
