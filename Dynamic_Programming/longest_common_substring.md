<!-- +------------------------------------------------------+ -->
<!-- |  LONGEST COMMON SUBWORD (LCW) — THE STREAK METER    | -->
<!-- +------------------------------------------------------+ -->

# Longest Common Subword (LCW) — The Streak Meter

## Theoretical Definition & Comparisons

**Theoretical Definition:** 
Longest Common Subword (LCW) or Substring finds the longest contiguous block of characters shared by two strings.

**Comparison (LCS vs LCW):**
*   **LCW:** Focuses on consecutive "streaks".
*   **LCS:** Focuses on overall "sequence" regardless of gaps.

---


## The Scenario

Imagine you are investigating **plagiarism**. You have two essays, and you want to see if any **exact sentences or phrases** have been copied-pasted. Unlike subsequences (LCS), where characters can be scattered, a copied phrase must be **contiguous** (no gaps allowed).

> **Goal:** Find the length of the longest identical "block" of characters shared by both strings.

---

![LCW "Streak" DP Table Walkthrough](docs/images/lcw_diagram.png)

## 1. LCS vs. LCW: The "Streak" Rule

The primary difference between standard Dynamic Programming for Subsequences and Substrings is how we handle **mismatches**.

- **LCS (Subsequence):** If characters don't match, we keep the previous best result. We "look back" to find a match.
- **LCW (Substring):** If characters don't match, the **streak is broken!** The current value resets to **0**.

---

## 2. Visualizing the Streak (Tabulation)

Strings: `PHOTO` and `TOMO`

```text
       ""   T   O   M   O
  "" [ 0 | 0 | 0 | 0 | 0 ]
  P  [ 0 | 0 | 0 | 0 | 0 ]
  H  [ 0 | 0 | 0 | 0 | 0 ]
  O  [ 0 | 0 | 1 | 0 | 1 ] <-- "O" matches "O"! Streak = 1
  T  [ 0 | 1 | 0 | 0 | 0 ] <-- "T" matches "T"! Streak = 1
  O  [ 0 | 0 | 2 | 0 | 1 ] <-- "O" matches "O"! Since "T" matched before,
                               Diag value (1) + 1 = 2!
```

**Max Streak Found:** 2 (The subword "TO")

---

## 3. Comparison of Core Logic

**Longest Common Subsequence (LCS):**
```python
if match:
    dp[i][j] = 1 + dp[i-1][j-1]
else:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1]) # Keep previous results
```

**Longest Common Substring (LCW):**
```python
if match:
    dp[i][j] = 1 + dp[i-1][j-1]
else:
    dp[i][j] = 0 # STREAK BROKEN!
```

---

## 4. Summary Table

| Approach | Logic | Complexity |
| :--- | :--- | :--- |
| **Tabulation** | Fill a 2D grid and track the global maximum. | $O(m \times n)$ |
| **Space Optimized** | Only keep the "Current Row" and "Previous Row". | $O(n)$ |

> [!TIP]
> **Teacher's Perspective:** "Think of LCW as a **High-Score Meter** in a game. As long as you keep hitting correctly, your multiplier grows. The moment you miss, you go back to zero. This 'Local' property is what makes substring searching different from global subsequence alignment."
