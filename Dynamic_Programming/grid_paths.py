"""
================================================================================
CONCEPTS AND THEORY: THE UNIQUE GRID PATHS PROBLEM
================================================================================

--- TIME COMPLEXITY ANALYSIS ---
- ALL DP VERSIONS: O(m * n) (We visit each cell in the grid exactly once)
--------------------------------
- SPACE COMPLEXITY:
  - Memoization: O(m * n) (Recursion stack + Map)
  - Tabulation:  O(m * n) (2D DP Table)
  - Optimized:   O(n)     (Only one row of memory!)

STATUS: INDEPENDENT (Contains all three implementations)
================================================================================

1. THE PROBLEM:
   You are at the top-left corner (0,0) of an m x n grid. You want to reach 
   the bottom-right corner (m-1, n-1). You can only move RIGHT or DOWN.
   How many unique paths are there?

2. THE "DECISION" AT EACH CELL (r, c):
   To arrive at cell (r, c), you must have come from:
   - The cell ABOVE: (r-1, c)
   - The cell to the LEFT: (r, c-1)
   
   Total Paths(r, c) = Paths(r-1, c) + Paths(r, c-1)

3. THE FORMULA (RECURRENCE):
   Paths(r, c) = Paths(r-1, c) + Paths(r, c-1)
   Base Case: cell (0,0) = 1 path. Cells on the top row or left column only 
   have one way to be reached (straight line).
================================================================================
"""

# ================================================================================
# APPROACH 1: MEMOIZATION (TOP-DOWN)
# ================================================================================

def unique_paths_memo(m, n):
    memo = {}
    
    def solve(r, c):
        # 1. Base Case: Start position
        if r == 0 and c == 0: return 1
        # 2. Out of bounds: No paths
        if r < 0 or c < 0: return 0
        
        # 3. Check notebook
        state = (r, c)
        if state in memo: return memo[state]
        
        # 4. Result = paths from above + paths from left
        memo[state] = solve(r - 1, c) + solve(r, c - 1)
        return memo[state]
        
    return solve(m - 1, n - 1)

# ================================================================================
# APPROACH 2: TABULATION (BOTTOM-UP)
# ================================================================================

def unique_paths_tabulation(m, n):
    # 1. Create a 2D grid to store path counts
    dp = [[0] * n for _ in range(m)]
    
    # 2. Fill the first column (only one way to go: Down)
    for r in range(m): dp[r][0] = 1
        
    # 3. Fill the first row (only one way to go: Right)
    for c in range(n): dp[0][c] = 1
        
    # 4. Fill the rest of the grid
    for r in range(1, m):
        for c in range(1, n):
            # Current cell = Above + Left
            dp[r][c] = dp[r-1][c] + dp[r][c-1]
            
    return dp[m-1][n-1]

# ================================================================================
# APPROACH 3: SPACE OPTIMIZED (O(n) Memory)
# ================================================================================

def unique_paths_optimized(m, n):
    """
    To calculate a cell, we only need the value above it (current row's prev state)
    and the value to its left (current row's updated state).
    We only need ONE ROW of memory!
    """
    # Start with a row of 1s (representing the first row paths)
    row = [1] * n
    
    for r in range(1, m):
        for c in range(1, n):
            # row[c] currently holds the 'Above' value
            # row[c-1] holds the 'Left' value
            row[c] = row[c] + row[c-1]
            
    return row[n-1]

# --- PERFORMANCE TEST ---

if __name__ == "__main__":
    M, N = 3, 7
    print(f"--- Grid Navigator Simulation ({M}x{N}) ---")
    
    print(f"Memoization Output:   {unique_paths_memo(M, N)}")
    print(f"Tabulation Output:    {unique_paths_tabulation(M, N)}")
    print(f"Space Optimized Output: {unique_paths_optimized(M, N)}")
    
    print(f"\nThere are exactly {unique_paths_optimized(M, N)} ways to reach the goal! ")
