<!-- +------------------------------------------------------+ -->
<!-- |  LONGEST COMMON SUBSEQUENCE (LCS) — GENETIC MATCHING | -->
<!-- +------------------------------------------------------+ -->

# Longest Common Subsequence (LCS) — Genetic Matching

## Theoretical Definition & Comparisons

**Theoretical Definition:** 
LCS finds the longest sequence of characters that appear in the same relative order in two strings. It is not necessarily contiguous.

**Comparison (LCS vs LCW):**
*   **LCS:** Non-contiguous. If characters don't match, we take $\max(Left, Above)$.
*   **LCW (Substring):** Must be contiguous. If characters don't match, the streak resets to 0.

---


## The Scenario

Imagine you are a biologist comparing the **DNA** of two different species. You want to see how much of their code is shared. However, Evolution is messy—new bits get inserted, and old bits get deleted. 

You need to find characters that appear in the **same relative order** in both strings, even if they aren't right next to each other.

> **Goal:** Find the length of the longest "matching chain" that exists in both strings in the same order.

---

![LCS DP Table Walkthrough](docs/images/lcs_diagram.png)

## 1. Subsequence vs. Substring

It's easy to get these mixed up!
- **Substring:** Must be contiguous (a "slice" of the string).
- **Subsequence:** Must be in order, but can have gaps.

```text
Strings: "APPLE" and "ALE"
- Substring Match: "A", "L", "E" (Length 1)
- Subsequence Match: "A-L-E" (Length 3)
```

---

## 2. The Decision Logic

As we compare character `s1[i]` with character `s2[j]`:

1.  **IT'S A MATCH!** 
    We count this character (+1) and move to the previous characters in both strings.
    Formula: `1 + Result(i-1, j-1)`

2.  **NOT A MATCH?**
    We have to choose: should we skip the character in `s1` or the one in `s2`? We take whichever gives us the better result later.
    Formula: `MAX( Result(i-1, j), Result(i, j-1) )`

---

## 3. Visualizing the DP Table (Tabulation)

Strings: `ABCDE` and `ACE`

```text
       ""   A   C   E
  "" [ 0 | 0 | 0 | 0 ]
  A  [ 0 | 1 | 1 | 1 ] <-- "A" matches "A"!
  B  [ 0 | 1 | 1 | 1 ] <-- "B" matches neither
  C  [ 0 | 1 | 2 | 2 ] <-- "C" matches "C"! (1 + diagonal 1)
  D  [ 0 | 1 | 2 | 2 ]
  E  [ 0 | 1 | 2 | 3 ] <-- "E" matches "E"! (1 + diagonal 2)

Final Result: 3
```

---

## 4. Summary Table

| Approach | Logic | Complexity |
| :--- | :--- | :--- |
| **Recursion** | Try every possible combination of skipping. | $O(2^n)$ - Extremely Slow! |
| **Tabulation** | Fill a 2D grid of matches. | $O(m \times n)$ - Linear! |
| **Space Optimized** | Only keep the "Current Row" and "Previous Row". | $O(n)$ - Memory Efficient! |

> [!TIP]
> **Teacher's Perspective:** "LCS is a 'Global' problem. We don't care where the characters are, just that they exist in the right order. It's the foundation of modern **File Comparison (Diff)** tools and **DNA Sequence Alignment**. If you've ever used `git diff`, you've used LCS!"
