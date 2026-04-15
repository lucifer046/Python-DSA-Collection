## 📋 Table of Contents

[Q1 — Function Analysis f(60)−f(59)](#q1)  
[Q2 — Selection Sort Condition Count](#q2)  
[Q3 — Linked List Operation Function](#q3)  
[Q4 — Hash Table with Linear Probing](#q4)  
[Q5 — Hash Table with Linear Probing](#q5)  
[Q5 — DAG Max Edges with Unique Topological Sort](#q5)  
[Q6 — Big-O Notation (MSQ)](#q6)  
[Q7 — Merge Sort Properties (MSQ)](#q7)  
[Q8 — Quicksort Properties (MSQ)](#q8)  
[Q9 — Linked List Constant Time Operations (MSQ)](#q9)  
[Q10 — Degree Sequences of Graphs (MSQ)](#q10)  
[Q11 — BFS Properties (MSQ)](#q11)  
[Q12 — Find Single Occurrence Element](#q12)  
[Q13 — Binary Search Last Occurrence](#q13)  
[Q14 — Stack and Queue Operations](#q14)  
[Q15 — Connected Graph Edge Bounds](#q15)  
[Q16 — DFS Time Complexity with Adjacency Matrix](#q16)  
[Q17 — Data Structure Matching](#q17)

---

<a id="q1"></a>

## Q1 — Function Analysis: What is f(60) − f(59)?

**Marks: 3 | Type: Short Answer (Numeric)**

### The Code

```python
def f(n):
    s = 0
    for i in range(2, n):
        if n % i == 0 and i % 2 == 1:
            s = s + 1
    return s
```

### What Does This Function Do?

Read the condition carefully:

```
if n % i == 0   → i is a divisor of n
and i % 2 == 1  → i is an ODD number
```

So **f(n) counts the number of ODD divisors of n** (excluding 1, since range starts at 2).

> [!TIP]
> **Teacher's Note:** Always decode what the function computes before plugging in values. Here, `n % i == 0` means "i divides n" and `i % 2 == 1` means "i is odd". Together: count odd divisors of n in range [2, n-1].

---

### Step 1: Compute f(60)

Find all divisors of 60 in range [2, 59]:

**Divisors of 60:** 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60

**Divisors in range [2, 59]:** 2, 3, 4, 5, 6, 10, 12, 15, 20, 30

**Odd ones among these:** 3, 5, 15 → **Count = 3**

```
f(60) = 3
```

---

### Step 2: Compute f(59)

59 is a **prime number** → its only divisors are 1 and 59.

Divisors in range [2, 58]: **None**

```
f(59) = 0
```

---

### Step 3: Final Answer

```
f(60) − f(59) = 3 − 0 = 3
```

### ✅ Answer: **3**

---

<a id="q2"></a>

## Q2 — Selection Sort: How Many Times Does the Condition Evaluate to True?

**Marks: 3 | Type: Short Answer (Numeric)**

### The Code

```python
def selectionsort(L):
    n = len(L)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if L[j] < L[min_idx]:   # ← Count how many times this is TRUE
                min_idx = j
        (L[i], L[min_idx]) = (L[min_idx], L[i])
    return L
```

**Input:** `L = [4, 1, 3, 2, 5]`

---

### Step-by-Step Trace

> [!TIP]
> **Teacher's Note:** Track `min_idx` carefully. Every time a new minimum is found and `min_idx` is updated, the condition `L[j] < L[min_idx]` was TRUE.

#### Pass i=0 (min_idx starts at 0, L[0]=4)

| j   | L[j] | L[min_idx] | L[j] < L[min_idx]? | min_idx |
| --- | ---- | ---------- | ------------------ | ------- |
| 1   | 1    | 4          | TRUE ✅            | → 1     |
| 2   | 3    | 1          | false              | 1       |
| 3   | 2    | 1          | false              | 1       |
| 4   | 5    | 1          | false              | 1       |

TRUE count this pass: **1**  
Swap L[0] and L[1]: `[1, 4, 3, 2, 5]`

---

#### Pass i=1 (min_idx starts at 1, L[1]=4)

| j   | L[j] | L[min_idx] | L[j] < L[min_idx]? | min_idx |
| --- | ---- | ---------- | ------------------ | ------- |
| 2   | 3    | 4          | TRUE ✅            | → 2     |
| 3   | 2    | 3          | TRUE ✅            | → 3     |
| 4   | 5    | 2          | false              | 3       |

TRUE count this pass: **2**  
Swap L[1] and L[3]: `[1, 2, 3, 4, 5]`

---

#### Pass i=2 (min_idx starts at 2, L[2]=3)

| j   | L[j] | L[min_idx] | L[j] < L[min_idx]? | min_idx |
| --- | ---- | ---------- | ------------------ | ------- |
| 3   | 4    | 3          | false              | 2       |
| 4   | 5    | 3          | false              | 2       |

TRUE count this pass: **0**

---

#### Pass i=3 (min_idx starts at 3, L[3]=4)

| j   | L[j] | L[min_idx] | L[j] < L[min_idx]? | min_idx |
| --- | ---- | ---------- | ------------------ | ------- |
| 4   | 5    | 4          | false              | 3       |

TRUE count this pass: **0**

---

### Total TRUE Count

```
Pass 0: 1
Pass 1: 2
Pass 2: 0
Pass 3: 0
─────────
Total:  3
```

### ✅ Answer: **3**

---

<a id="q3"></a>

## Q3 — Linked List: Output of the Operation Function

**Marks: 3 | Type: Short Answer (Numeric)**

### The Setup

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

**Linked List:**

```
8 → 3 → 6 → 1 → 9 → 4 → 7 → None
```

### The Function

```python
def operation(head):
    ptr1 = head
    ptr2 = head.next
    total = 0

    while ptr2 is not None:
        total = total + ptr2.data
        if ptr2.next is None:
            break
        ptr2 = ptr2.next.next
        ptr1 = ptr1.next

    print(total - ptr1.data)
```

---

### Step-by-Step Trace

> [!TIP]
> **Teacher's Note:** This is a two-pointer problem. `ptr2` jumps **two steps** at a time, while `ptr1` moves **one step** at a time. This is the classic "fast & slow pointer" pattern used to find the middle of a linked list.

**Iteration Trace:**

- **Initial:** total = 0, ptr2 at 3, ptr1 at 8
- **Iter 1:** total = 3, ptr2 moves to 1, ptr1 moves to 3
- **Iter 2:** total = 3 + 1 = 4, ptr2 moves to 4, ptr1 moves to 6
- **Iter 3:** total = 4 + 4 = 8, ptr2 moves to None, ptr1 moves to 1
- **End:** ptr2 is None.

**Final Calculation:**
`total - ptr1.data = 8 - 1 = 7`

### ✅ Answer: **7**

---

<a id="q4"></a>

## Q4 — Hash Table with Linear Probing: Where Does 42 Go?

**Marks: 3 | Type: Short Answer (Numeric)**

### Setup

- Hash table with **8 buckets** (indices 0 to 7)
- Hash function: `h(key) = key mod 8`
- Keys inserted: **18, 10, 12, 21**, then **42**

---

### Insertion Order

1. **18:** 18%8 = **2** (Available)
2. **10:** 10%8 = **2** (Occupied, try index 3 → Available)
3. **12:** 12%8 = **4** (Available)
4. **21:** 21%8 = **5** (Available)
5. **42:** 42%8 = **2**
   - Index 2: 18 (X)
   - Index 3: 10 (X)
   - Index 4: 12 (X)
   - Index 5: 21 (X)
   - Index 6: **Available** ✅

### ✅ Answer: **6**

---

<a id="q5"></a>

## Q5 — DAG with Unique Topological Sort: Max Edges?

**Marks: 3 | Type: Short Answer (Numeric)**

### Problem

A **Directed Acyclic Graph (DAG)** has **6 vertices**. It is guaranteed to have a **unique topological sort**. What is the **maximum** number of edges it can have?

---

### Step-by-Step Logic

1.  **Topological Sort condition:** For a unique topological sort $v_1, v_2, v_3, v_4, v_5, v_6$ to exist, there MUST be a directed path that visits every vertex in that specific order. This is a **Hamiltonian Path**: $v_1 \to v_2 \to v_3 \to v_4 \to v_5 \to v_6$.
2.  **Adding extra edges:** To maximize edges while keeping the DAG property and the unique sort, we can add any directed edge $(v_i, v_j)$ as long as $i < j$.
3.  **Counting:**
    *   $v_1$ can connect to: $v_2, v_3, v_4, v_5, v_6$ (5 edges)
    *   $v_2$ can connect to: $v_3, v_4, v_5, v_6$ (4 edges)
    *   $v_3$ can connect to: $v_4, v_5, v_6$ (3 edges)
    *   $v_4$ can connect to: $v_5, v_6$ (2 edges)
    *   $v_5$ can connect to: $v_6$ (1 edge)
    *   $v_6$ can connect to: None (0 edges)
4.  **Total:** $5 + 4 + 3 + 2 + 1 = 15$.

### ✅ Answer: **15**

---

<a id="q6"></a>

## Q6 — Big-O Notation: Which Statements are FALSE?

**Marks: 3 | Type: Multiple Select Question**

### Detailed Justification

We are looking for **FALSE** statements.

*   **A. $f(n) = O(g(n))$:**
    *   $f(n) \approx n^3$, $g(n) \approx n^2 \log n$.
    *   Is $n^3 \le c \cdot n^2 \log n$? No. Dividing by $n^2$ gives $n \le c \cdot \log n$, which is false for large $n$.
    *   **Result: FALSE** ✅
*   **B. $g(n) = O(h(n))$:**
    *   $g(n) \approx n^2 \log n$, $h(n) \approx n^3 \log n$.
    *   Since $n^2 < n^3$, this is clearly true.
    *   **Result: TRUE**
*   **C. $f(n) = O(h(n))$:**
    *   $f(n) \approx n^3$, $h(n) \approx n^3 \log n$.
    *   Since $1 < \log n$ for large $n$, $n^3$ grows slower than $n^3 \log n$.
    *   **Result: TRUE**
*   **D. $h(n) = O(f(n))$:**
    *   $h(n) \approx n^3 \log n$, $f(n) \approx n^3$.
    *   Is $n^3 \log n \le c \cdot n^3$? No. $\log n$ is not bounded by a constant.
    *   **Result: FALSE** ✅

### ✅ Answers (False Statements): **A and D**

---

<a id="q7"></a>

## Q7 — Merge Sort Properties: Which are TRUE?

**Marks: 3 | Type: Multiple Select Question**

- **A. Stability:** The condition `if A[i] <= B[j]` preserves the relative order of equal elements. **(TRUE)** ✅
- **B. Worst-case Complexity:** Merge sort is always $O(n \log n)$. **(TRUE)** ✅
- **C. Best-case Complexity:** It cannot magically do $O(n)$; even sorted input takes $O(n \log n)$. **(FALSE)**
- **D. Unstable variant:** Removing `=` in `<=` makes it unstable. **(TRUE)** ✅

### ✅ Answers (True Statements): **A, B, and D**

---

<a id="q8"></a>

## Q8 — Quicksort Properties: Which are TRUE?

**(First element always chosen as pivot)**

- **A. Sorted Input Ascending:** Pivot is the smallest element. Splits are 0 and $n-1$. $O(n^2)$. **(TRUE)** ✅
- **B. Sorted Input Descending:** Pivot is the largest element. Splits are $n-1$ and 0. $O(n^2)$ (not $O(n \log n)$). **(FALSE)**
- **C. Stability:** Quicksort is generally not stable. **(FALSE)**
- **D. Average-case:** Generally expected to be $O(n \log n)$. **(TRUE)** ✅

### ✅ Answers (True Statements): **A and D**

---

<a id="q9"></a>

## Q9 — Singly Linked List: Which Operations are NOT O(1)?

**(With head and tail pointer)**

- **A. Insert front:** $O(1)$
- **B. Insert end:** $O(1)$ (thanks to tail pointer)
- **C. Delete front:** $O(1)$
- **D. Delete end:** $O(n)$ (must traverse to find second-to-last node to update tail). ✅
- **E. Access second last:** $O(n)$ ✅

### ✅ Answers (Not O(1)): **D and E**

---

<a id="q10"></a>

## Q10 — Degree Sequences of Connected Graphs (5 vertices)

### Justification using Handshaking Lemma

The **Handshaking Lemma** states: $\sum \text{deg}(v) = 2|E|$.
This means the sum of degrees MUST be **even**.

*   **A. [4, 3, 2, 1, 1]:** Sum = 11. **Impossible** (Must be even).
*   **B. [3, 3, 2, 1, 1]:** Sum = 10. Possible. (e.g., Two triangles sharing a vertex). ✅
*   **C. [2, 2, 2, 2, 2]:** Sum = 10. Possible. This is a **Cycle Graph** $C_5$. ✅
*   **D. [4, 2, 2, 1, 1]:** Sum = 10. Possible. This is a **Star Graph** where center has degree 4. ✅
*   **E. [5, 2, 1, 1, 1]:** Even if sum was even, a vertex can have at most $n-1 = 4$ neighbors in a simple graph with 5 vertices. Degree 5 is **impossible**.

### ✅ Answers (Valid sequences): **B, C, and D**

---

<a id="q11"></a>

## Q11 — BFS Properties: Which are TRUE?

- **A.** BFS visits level-by-level, not deep paths. **(FALSE)**
- **B.** BFS finds shortest edge count, not arbitrary weights. **(FALSE)**
- **C.** BFS uses a **Queue** (FIFO). **(TRUE)** ✅
- **D.** Traversal order depends on start vertex. **(TRUE)** ✅
- **E.** Core level-order property. **(TRUE)** ✅

### ✅ Answers (True Statements): **C, D, and E**

---

<a id="q12"></a>

## Q12 — Single Occurrence Element in Sorted List: Efficiency?

### Detailed Logic

To find an element in a sorted list, we can use **Binary Search**.

1.  Compare the middle element with its neighbors.
2.  In a list where every element appears twice except one, the single element changes the **parity** of matching pairs.
3.  By checking index pairs (even, odd), we can decide whether to move left or right in $O(\log n)$ time.

> [!TIP]
> **Teacher's Note:** Whenever you see **"Sorted List"** and **"Find [Something]"**, $O(\log n)$ should be your first thought!

### ✅ Answer: **D. O(log n)**

---

<a id="q13"></a>

## Q13 — Binary Search for Last Occurrence: How to Proceed?

### Step-by-Step Logic

In standard Binary Search, when `L[mid] == target`, we return `mid`. However, to find the **LAST** occurrence:

1.  If `L[mid] == target`, we know this *could* be the answer, but there might be more occurrences to the **right**.
2.  We **save** the current `mid` in a variable `ans`.
3.  We continue searching the **right half** by setting `low = mid + 1`.
4.  If we find another match later, it will overwrite `ans`, thus giving us the last position.

### ✅ Answer: **C. Store mid as potential answer, continue right (low = mid + 1)**

---

<a id="q14"></a>

## Q14 — Stack and Queue Operations: Resulting Q?

### The Operation Trace

Let's maintain the state of the Queue `Q` and Stack `S` after each step.

| Step | Operation | Resulting Q | Resulting S |
| :--- | :--- | :--- | :--- |
| 0 | Initial | `[12, 35, 7, 40, 18]` | `[]` |
| 1 | `S.push(Q.dequeue())` | `[35, 7, 40, 18]` | `[12]` |
| 2 | `S.push(Q.dequeue())` | `[7, 40, 18]` | `[12, 35]` |
| 3 | `Q.enqueue(S.pop())` | `[7, 40, 18, 35]` | `[12]` |
| 4 | `S.push(Q.dequeue())` | `[40, 18, 35]` | `[12, 7]` |
| 5 | `Q.enqueue(S.pop())` | `[40, 18, 35, 7]` | `[12]` |
| 6 | `Q.enqueue(S.pop())` | `[40, 18, 35, 7, 12]` | `[]` |

**Final State of Q:** `[40, 18, 35, 7, 12]`
*   **Front:** 40
*   **Rear:** 12

### ✅ Answer: **front: 40, rear: 12**

---

<a id="q15"></a>

## Q15 — Connected Undirected Graph (n=7): Min/Max Edges?

- **Min:** Tree = $n-1 = 6$
- **Max:** Complete = $\frac{n(n-1)}{2} = \frac{7 \times 6}{2} = 21$

### ✅ Answer: **C. Min: 6, Max: 21**

---

<a id="q16"></a>

## Q16 — DFS Time Complexity with Adjacency Matrix

### The "Matrix Penalty" Explained

1.  **Traversal Mechanism:** In DFS (or BFS), to find neighbors of a vertex $u$, you must look at its entry in the data structure.
2.  **Adjacency Matrix:** Each vertex has a row of size $V$ (or $n$). To find neighbors, you MUST scan all $n$ columns to check for `1`s.
3.  **Total Cost:** Since you visit each of the $n$ vertices once, and each visit requires an $O(n)$ scan:
    *   Total Time = $n$ vertices $\times$ $O(n)$ per vertex = **$O(n^2)$**.

> [!NOTE]
> Even if the graph is **sparse** (few edges), the matrix forces you to look at every possible edge slot, leading to $O(n^2)$.

### ✅ Answer: **C. O(n²)**

---

<a id="q17"></a>

## Q17 — Data Structure Matching

1. **Undo-Redo:** Stack (ii)
2. **Printer:** Queue (i)
3. **Road Map:** Undirected Graph (iii)
4. **Task Dependencies:** Directed Graph (iv)

### ✅ Answer: **A. 1-ii, 2-i, 3-iii, 4-iv**

---

## 📊 Summary Table

| Q#  | Topic             | Answer       | Key Concept                 |
| --- | ----------------- | ------------ | --------------------------- |
| Q1  | Function Analysis | 3            | Count odd divisors          |
| Q2  | Selection Sort    | 3            | Trace condition updates     |
| Q3  | Linked List       | 7            | Fast/Slow pointers          |
| Q4  | Hash Table        | 6            | Linear probing              |
| Q5  | DAG Max Edges     | 15           | Hamiltonian Path            |
| Q6  | Big-O Logic       | A, D         | Dominant growth             |
| Q7  | Merge Sort        | A, B, D      | Stability/Always $n \log n$ |
| Q8  | Quicksort         | A, D         | Pivot selection impact      |
| Q9  | Singly LL Limits  | D, E         | No back-pointers            |
| Q10 | Degree Sequences  | B, C, D      | Handshaking lemma           |
| Q11 | BFS Insights      | C, D, E      | FIFO level traversal        |
| Q12 | Efficiency Hint   | O(log n)     | Sorted = Binary Search      |
| Q13 | BS Strategy       | Search Right | Scan for last position      |
| Q14 | S/Q Trace         | 40 / 12      | Step-by-step simulator      |
| Q15 | Edge Counts       | 6 / 21       | Connectivity constraints    |
| Q16 | Matrix Penalty    | $O(n^2)$     | Scanning rows recursively   |
| Q17 | Application Fit   | Match DS     | Core behaviors              |

---

## Key Takeaways

1. Mastering **manual tracing** of code is essential for exam success.
2. Selection Sort condition counts reveal the inner mechanics of the algorithm.
3. Two-pointer techniques in Linked Lists (Fast/Slow) are powerful for finding midpoints.
4. Hash collisions and Linear Probing follow a systematic index-shift pattern.
5. Unique Topological Sorts in DAGs imply the existence of a Hamiltonian Path.
6. Binary Search logic (searching right for last occurrence) is key for finding bounds.
7. Adjacency Matrix DFS costs $O(n^2)$ due to mandatory $O(n)$ degree scans per vertex.
