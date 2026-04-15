"""
================================================================================
CONCEPTS AND THEORY: LONGEST COMMON SUBSEQUENCE (LCS)
================================================================================

--- TIME COMPLEXITY ANALYSIS ---
- ALL DP VERSIONS: O(m * n) (m and n are lengths of the two strings)
--------------------------------
- SPACE COMPLEXITY:
  - Memoization: O(m * n) (Recursion depth + Memo map)
  - Tabulation:  O(m * n) (2D DP Matrix)
  - Optimized:   O(min(m, n)) (Only two rows of memory!)

STATUS: INDEPENDENT (Contains all three implementations)
================================================================================

1. THE PROBLEM:
   Find the length of the longest subsequence that is present in both 
   strings. A subsequence is an ordered set of characters that do NOT have 
   to be contiguous (next to each other).
   Example: "apple", "ale" -> "ale" (3)

2. THE "DECISION" AT EACH CHARACTER:
   Compare s1[i] and s2[j]:
   - IF CHARS MATCH: That character is part of our subsequence!
     Total = 1 + LCS(i-1, j-1)
   - IF CHARS DON'T MATCH: We must try skipping one from either string.
     Total = MAX( LCS(i-1, j), LCS(i, j-1) )

3. THE FORMULA:
   dp[i][j] = 1 + dp[i-1][j-1] if match
   dp[i][j] = max(dp[i-1][j], dp[i][j-1]) if no match
================================================================================
"""

# ================================================================================
# APPROACH 1: MEMOIZATION (TOP-DOWN)
# ================================================================================

def lcs_memo(s1, s2):
    memo = {}
    
    def solve(i, j):
        # 1. Base Case: If one string is empty, LCS is 0
        if i < 0 or j < 0: return 0
        
        # 2. Check notebook
        state = (i, j)
        if state in memo: return memo[state]
        
        # 3. If characters match, add 1 and shrink both
        if s1[i] == s2[j]:
            memo[state] = 1 + solve(i - 1, j - 1)
        # 4. If they don't match, take the best of skipping one or the other
        else:
            memo[state] = max(solve(i - 1, j), solve(i, j - 1))
            
        return memo[state]
        
    return solve(len(s1) - 1, len(s2) - 1)

# ================================================================================
# APPROACH 2: TABULATION (BOTTOM-UP)
# ================================================================================

def lcs_tabulation(s1, s2):
    m, n = len(s1), len(s2)
    # 1. Create a 2D matrix (plus one row/col for empty string cases)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # 2. Build the table character by character
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Characters match? Look at diagonal + 1
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            # No match? Best of Up or Left
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
    return dp[m][n]

# ================================================================================
# APPROACH 3: SPACE OPTIMIZED (O(n) Memory)
# ================================================================================

def lcs_optimized(s1, s2):
    """
    To calculate the current row, we only need information from 
    the PREVIOUS row. We can reduce space to O(n).
    """
    m, n = len(s1), len(s2)
    # Use the shorter string for columns to minimize space
    if m < n:
        s1, s2 = s2, s1
        m, n = n, m
        
    prev = [0] * (n + 1)
    
    for i in range(1, m + 1):
        curr = [0] * (n + 1)
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                curr[j] = 1 + prev[j-1]
            else:
                curr[j] = max(prev[j], curr[j-1])
        prev = curr
        
    return prev[n]

# --- PERFORMANCE DEMONSTRATION ---

if __name__ == "__main__":
    text1, text2 = "ABCDE", "ACE"
    print("--- Subsequence Analysis ---")
    print(f"String 1: {text1}\nString 2: {text2}")
    
    print(f"Memoization Result:   {lcs_memo(text1, text2)}")
    print(f"Tabulation Result:    {lcs_tabulation(text1, text2)}")
    print(f"Space Optimized Result: {lcs_optimized(text1, text2)}")
    
    print("\nThe longest common subsequence 'ACE' has a length of 3! ")
