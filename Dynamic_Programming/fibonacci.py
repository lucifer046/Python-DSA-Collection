"""
================================================================================
CONCEPTS AND THEORY: DYNAMIC PROGRAMMING (FIBONACCI CASE STUDY)
================================================================================

--- TIME COMPLEXITY ANALYSIS ---
- RECURSIVE:    O(2^n) (Exponential - Forgetful and very slow)
- MEMOIZATION:  O(n)   (Linear - Remembers using a 'Note-book')
- TABULATION:   O(n)   (Linear - Builds from the bottom up)
- OPTIMIZED:    O(n)   (Linear - Same speed, but uses ONLY O(1) space)
--------------------------------
- SPACE COMPLEXITY: 
    - Recursive:   O(n) (Stack depth)
    - Memoization: O(n) (Stack + Notebook)
    - Tabulation:  O(n) (Table array)
    - Optimized:   O(1) (Only 2 variables!)

STATUS: INDEPENDENT (Contains multiple versions for performance comparison)
================================================================================

1. WHAT IS DYNAMIC PROGRAMMING (DP)?
   DP is a method for solving complex problems by breaking them down into 
   simpler subproblems. It solves each subproblem just once and stores 
   their results.

2. MEMOIZATION (TOP-DOWN):
   Start with the big problem and break it down. If you've solved a 
   subproblem before, just look up the answer in your 'memo' dictionary.

3. TABULATION (BOTTOM-UP):
   Start with the smallest base cases and fill up a table until you 
   reach the target. It avoids the overhead of recursion.

4. SPACE OPTIMIZATION:
   For Fibonacci, we don't need the whole table, just the last two 
   results. This saves a lot of memory!

5. PERFORMANCE COMPARISON:
   If you try n=40:
   - Recursive: Takes several seconds.
   - DP Versions: Take almost zero time!
================================================================================
"""

import time

# --- 1. SIMPLE RECURSIVE (The Forgetful Method) ---
def fib_recursive(n):
    """ Standard recursion: extremely slow for large n. """
    # Base cases: fib(0)=0, fib(1)=1
    if n <= 1:
        return n
    # The 'Forgetful' step: calculates the same branches many times
    return fib_recursive(n - 1) + fib_recursive(n - 2)


# --- 2. MEMOIZATION (Top-Down with Notebook) ---
memo = {} # The notebook to store results
def fib_memoization(n):
    """ Uses a dictionary to remember previous results. """
    # 1. Base case
    if n <= 1:
        return n
    
    # 2. Check the notebook
    if n not in memo:
        # 3. Solve and WRITE in the notebook
        memo[n] = fib_memoization(n - 1) + fib_memoization(n - 2)
    
    # 4. Return the saved result
    return memo[n]


# --- 3. TABULATION (Bottom-Up Building Blocks) ---
def fib_tabulation(n):
    """ Builds a table from 0 upwards. """
    if n <= 1:
        return n
        
    # 1. Create a Table of size n+1
    T = [0] * (n + 1)
    
    # 2. Fill in base cases
    T[1] = 1
    
    # 3. Build the skyscraper (solve smaller to larger)
    for i in range(2, n + 1):
        T[i] = T[i - 1] + T[i - 2]
        
    # 4. The top of the building is our answer
    return T[n]


# --- 4. SPACE OPTIMIZED (The Minimalism Method) ---
def fib_optimized(n):
    """ Only keeps the 'last two' numbers. O(1) Space! """
    if n <= 1:
        return n
        
    # We only need two 'memory' slots
    prev2, prev1 = 0, 1
    
    for _ in range(2, n + 1):
        # Calculate current as sum of last two
        curr = prev1 + prev2
        # Shift the memory forward
        prev2 = prev1
        prev1 = curr
        
    return prev1


# --- PERFORMANCE TESTER ---

if __name__ == "__main__":
    try:
        n = int(input("Enter n for Fibonacci (try 35 to see the speed diff): "))
    except ValueError:
        n = 30 # Default if input is messy
        print("Invalid input, using n=30")

    print(f"\nComparing Fibonacci implementations for n = {n}...\n")

    # Test 1: Recursive
    start = time.perf_counter()
    res_rec = fib_recursive(n)
    time_rec = time.perf_counter() - start
    print(f"[RECURSION]  Result: {res_rec} | Time: {time_rec:.6f}s (SLOW)")

    # Test 2: Memoization
    start = time.perf_counter()
    res_memo = fib_memoization(n)
    time_memo = time.perf_counter() - start
    print(f"[MEMOIZE]    Result: {res_memo} | Time: {time_memo:.6f}s (FAST)")

    # Test 3: Tabulation
    start = time.perf_counter()
    res_tab = fib_tabulation(n)
    time_tab = time.perf_counter() - start
    print(f"[TABULATION] Result: {res_tab} | Time: {time_tab:.6f}s (FAST)")

    # Test 4: Optimized
    start = time.perf_counter()
    res_opt = fib_optimized(n)
    time_opt = time.perf_counter() - start
    print(f"[OPTIMIZED]  Result: {res_opt} | Time: {time_opt:.6f}s (BEST)")

    print("\nDynamic Programming Successful! OK")
