"""
================================================================================
CONCEPTS AND THEORY: LONGEST COMMON SUBSTRING (LCW)
================================================================================

--- TIME COMPLEXITY ANALYSIS ---
- ALL DP VERSIONS: O(m * n) (m and n are lengths of the two strings)
--------------------------------
- SPACE COMPLEXITY:
  - Tabulation:  O(m * n) (2D DP Matrix)
  - Optimized:   O(min(m, n)) (Only two rows of memory!)

STATUS: INDEPENDENT (Contains Tabulation and Optimized implementations)
================================================================================

1. THE PROBLEM:
   Find the length of the longest contiguous piece of text that appears in 
   both strings. Unlike LCS, the characters MUST be next to each other.
   Example: "photograph", "tomography" -> "ograph" (6)

2. THE "DECISION" AT EACH CHARACTER:
   Compare s1[i] and s2[j]:
   - IF CHARS MATCH: Increment the streak from the previous characters.
     Total = 1 + Result(i-1, j-1)
   - IF CHARS DON'T MATCH: The contiguous streak is broken!
     Total = 0

3. THE FORMULA:
   dp[i][j] = 1 + dp[i-1][j-1] if match
   dp[i][j] = 0 if no match
   Global result = MAX(any cell in dp)
================================================================================
"""

# ================================================================================
# APPROACH 1: TABULATION (BOTTOM-UP)
# ================================================================================

def lcs_substring_tabulation(s1, s2):
    m, n = len(s1), len(s2)
    # 1. Create a 2D matrix
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_len = 0
    
    # 2. Build the table character by character
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Characters match? Look at diagonal + 1
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                # Update the global maximum length found so far
                max_len = max(max_len, dp[i][j])
            # No match? The streak resets to 0
            else:
                dp[i][j] = 0
                
    return max_len

# ================================================================================
# APPROACH 2: SPACE OPTIMIZED (O(n) Memory)
# ================================================================================

def lcs_substring_optimized(s1, s2):
    """
    To calculate the current row, we only need information from 
    the PREVIOUS row's diagonal (prev[j-1]).
    """
    m, n = len(s1), len(s2)
    if m < n:
        s1, s2 = s2, s1
        m, n = n, m
        
    prev = [0] * (n + 1)
    max_len = 0
    
    for i in range(1, m + 1):
        curr = [0] * (n + 1)
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                curr[j] = 1 + prev[j-1]
                max_len = max(max_len, curr[j])
            else:
                curr[j] = 0
        prev = curr
        
    return max_len

# --- PERFORMANCE DEMONSTRATION ---

if __name__ == "__main__":
    text1, text2 = "photograph", "tomography"
    print("--- Contiguous Substring Analysis ---")
    print(f"String 1: {text1}\nString 2: {text2}")
    
    print(f"Tabulation Result:    {lcs_substring_tabulation(text1, text2)}")
    print(f"Space Optimized Result: {lcs_substring_optimized(text1, text2)}")
    
    print("\nThe longest common substring 'ograph' has a length of 6! ")
