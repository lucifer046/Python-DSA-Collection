<!-- +------------------------------------------------------+ -->
<!-- |  THE HOUSE ROBBER PROBLEM — OPTIMAL PLANNING         | -->
<!-- +------------------------------------------------------+ -->

# The House Robber Problem — Optimal Planning

## The Scenario (Without the Contradiction)

**The Challenge:** You are a professional planner (a "cat burglar") eyeing a street of houses. Each house has a specific stash of cash. However, there's a strict security rule: **Adjacent houses share a connected alarm system.** If you break into two houses right next to each other, the alarm triggers and your mission ends!

> **Goal:** What is the absolute maximum amount of money you can collect in one night without triggering any alarms?

---

## 1. The "Greedy" Trap

You might think: _"I'll just pick the biggest houses!"_
But look at this example: `[1, 100, 1, 1, 100, 1]`
- If you pick the **100s**, they are far apart, so you get **200**. Good!
- But what if you picked a house that blocked you from getting two even bigger houses later?
- We need a strategy that looks at the **dependency** of each choice.

---

## 2. The Decision Factor

At every house, you face a binary choice. Let's look at the current house $i$:

```text
Decision for House [i]:
-----------------------
1. ROB IT:    You get Money[i] + whatever you robbed up to 2 houses ago (i-2).
2. SKIP IT:   You keep whatever you robbed up to the previous house (i-1).

The Answer: MAX(Robbing [i], Skipping [i])
```

---

## 3. Visualizing the DP Table (Tabulation)

Imagine the houses: `[2, 7, 9, 3, 1]`

### Step-by-Step Table Filling:

We build a `Loot_Table` where each slot $i$ stores: _"The most money I could have by the time I reach this house."_

```text
House Index:   0    1    2    3    4
House Value:  [2]  [7]  [9]  [3]  [1]
              -------------------------

Loot_Table[0]: 2
(Only one house? Just rob it.)

Loot_Table[1]: 7
(Two houses? Pick the bigger one. MAX(2, 7) = 7)

Loot_Table[2]: 11
(Decision: Rob 9 + Loot[0]=2 => 11, OR keep Loot[1]=7. Max is 11!)

Loot_Table[3]: 11
(Decision: Rob 3 + Loot[1]=7 => 10, OR keep Loot[2]=11. Max is 11!)

Loot_Table[4]: 12
(Decision: Rob 1 + Loot[2]=11 => 12, OR keep Loot[3]=11. Max is 12!)

Final Result: 12
```

---

## 4. Space Optimization (The "Window" Method)

Did you notice? To calculate the next value in the `Loot_Table`, we only ever looked at the **last two numbers**. We don't need the whole table!

```text
[ Prev2 ]  [ Prev1 ]  -->  [ Current ]
   (i-2)      (i-1)            (i)

As we move to the next house, we "Slide the window" forward:
Prev2 = Prev1
Prev1 = Current
```

**Memory saved:** We went from $O(n)$ space to $O(1)$ space!

---

## 5. Summary of Strategies

| Approach | Logic | Performance |
| :--- | :--- | :--- |
| **Memoization** | Start at the end, ask "Should I rob this?", save answers to avoid re-asking. | $O(n)$ Time, $O(n)$ Space |
| **Tabulation** | Start at the beginning, build the max loot for 1 house, 2 houses, etc. | $O(n)$ Time, $O(n)$ Space |
| **Optimized** | Same as Tabulation, but only remember the last two houses' max loot. | $O(n)$ Time, **$O(1)$ Space** |

> [!TIP]
> **Teacher's Perspective:** "The House Robber is a classic example of how a simple 'Rob or Skip' decision at each step can grow into a complex problem. By breaking it down and realizing that the best choice for house #10 only depends on what we decided for #9 and #8, we turn a scary exponential problem into a very simple, linear walk down the street!"
