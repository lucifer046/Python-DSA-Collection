"""
================================================================================
CONCEPTS AND THEORY: THE HOUSE ROBBER PROBLEM (MAXIMUM LOOT)
================================================================================

--- TIME COMPLEXITY ANALYSIS ---
- ALL VERSIONS (Memo, Tab, Space): O(n) (We visit each house exactly once)
--------------------------------
- SPACE COMPLEXITY:
  - Memoization: O(n) (Recursion stack + Cache)
  - Tabulation:  O(n) (DP Table)
  - Optimized:   O(1) (Only two variables!)

STATUS: INDEPENDENT (Contains all three implementations)
================================================================================

1. THE PROBLEM:
   You are a cat burglar planning to rob houses along a street. Each house has 
   a certain amount of money. The catch? If you rob two ADJACENT houses, 
   the alarm goes off!

2. THE "DECISION" AT EACH HOUSE:
   At every house (i), you have two choices:
   - CHOICE A: ROB house 'i'. If you do this, you CANNOT rob house 'i-1'.
     Total = Money[i] + MaxLoot(i-2)
   - CHOICE B: SKIP house 'i'. If you do this, you are free to rob house 'i-1'.
     Total = MaxLoot(i-1)

3. THE FORMULA (RECURRENCE):
   Loot(i) = MAX( Loot(i-2) + Money[i],  Loot(i-1) )

4. DYNAMIC PROGRAMMING LAYERS:
   - MEMOIZATION (Top-Down): Start from the last house and remember previous 
     heists in a notebook.
   - TABULATION (Bottom-Up): Start from the first house and fill a 'Loot Table'.
   - SPACE OPTIMIZED: Since we only need the last two answers, we only keep 
     two numbers in memory.
================================================================================
"""

# ================================================================================
# APPROACH 1: MEMOIZATION (TOP-DOWN) - The "Notebook" Method
# ================================================================================

def rob_memo(nums):
    memo = {}
    
    def solve(i):
        # 1. Base Case: If no houses left, no money!
        if i < 0: return 0
        
        # 2. Check notebook: Did we already solve this house?
        if i in memo: return memo[i]
        
        # 3. Decision: Rob this house + jump back 2, OR skip this house.
        res = max(nums[i] + solve(i - 2), solve(i - 1))
        
        # 4. Save to notebook
        memo[i] = res
        return res
        
    return solve(len(nums) - 1)

# ================================================================================
# APPROACH 2: TABULATION (BOTTOM-UP) - The "DP Table" Method
# ================================================================================

def rob_tabulation(nums):
    if not nums: return 0
    if len(nums) == 1: return nums[0]
    
    n = len(nums)
    # 1. dp_table: stores the max loot possible up to house 'i'
    dp = [0] * n
    
    # 2. Base Cases
    dp[0] = nums[0]                 # Only one house? Rob it.
    dp[1] = max(nums[0], nums[1])   # Two houses? Rob the richer one.
    
    # 3. Fill the table from left to right
    for i in range(2, n):
        # Max of (rob current + loot from 2 houses back) or (skip current/keep prev loot)
        dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
    return dp[n-1]

# ================================================================================
# APPROACH 3: SPACE OPTIMIZED (O(1) Memory) - The "Two Variable" Method
# ================================================================================

def rob_optimized(nums):
    """
    To calculate current loot, we only need the results of i-1 and i-2.
    We don't need a whole table!
    """
    if not nums: return 0
    
    prev2 = 0 # Max loot 2 houses back
    prev1 = 0 # Max loot 1 house back
    
    for x in nums:
        # current = MAX(rob this house + prev2, skip this house/keep prev1)
        current = max(prev1, x + prev2)
        
        # Slide the window forward
        prev2 = prev1
        prev1 = current
        
    return prev1

# --- PERFORMANCE DEMONSTRATION ---

if __name__ == "__main__":
    houses = [2, 7, 9, 3, 1]
    
    print("--- House Robber Heist Simulator ---")
    print(f"Houses money: {houses}")
    
    # 1. Test Memoization
    print(f"Memoization Result:   {rob_memo(houses)}")
    
    # 2. Test Tabulation
    print(f"Tabulation Result:    {rob_tabulation(houses)}")
    
    # 3. Test Optimized
    print(f"Space Optimized Result: {rob_optimized(houses)}")
    
    print("\nConclusion: All roads lead to 12! [2 + 9 + 1]")
