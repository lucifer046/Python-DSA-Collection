"""
================================================================================
CONCEPTS AND THEORY: KARATSUBA'S INTEGER MULTIPLICATION
================================================================================

--- TIME COMPLEXITY ANALYSIS ---
- BEST CASE:    O(n^1.58) (Exponentially faster than O(n^2) for large digits)
- AVERAGE CASE: O(n^1.58) 
- WORST CASE:   O(n^1.58) 
--------------------------------
- SPACE COMPLEXITY: O(n) (Due to the recursion stack of dividing numbers)

STATUS: INDEPENDENT (Contains both full and compact implementations)
================================================================================

1. WHAT IS IT?
   When we multiply numbers like 12 * 13, we usually do 12 * 3 and 12 * 10
   and add them. For 2-digit numbers, that is 4 small multiplications.
   As numbers get huge (millions of digits), doing n^2 multiplications 
   becomes incredibly slow. Karatsuba is a math "hack" that lets us do 
   the same job using only 3 multiplications instead of 4!

2. HOW IT WORKS (THE MATH HACK):
   Divide n-digit numbers into two halves: Left (h) and Right (l).
   Normal math says: 
   (Xh * Yh) + (Xh * Yl + Xl * Yh) + (Xl * Yl)
   Wait! That's 4 multiplications!
   Karatsuba says: 
   Wait, we can calculate (Xh * Yl + Xl * Yh) by doing 
   (Xh + Xl) * (Yh + Yl) - (Xh * Yh) - (Xl * Yl)
   Since we already calculated (Xh * Yh) and (Xl * Yl), we only 
   need ONE more multiplication!

3. WHY CAN'T WE JUST USE 'number_a * number_b'?
   In simple programming, we DO use a * b because Python handles 
   the complexity for us. But imagine you are building a calculator
   that handles numbers with 10,000,000 digits!
   - THE SCHOOL METHOD (O(n^2)): If digits doubling means time goes up by 4x.
   - KARATSUBA (O(n^1.58)): If digits doubling means time goes up by ~3x.
   For massive scientific calculations (like encryption or astronomy), 
   Karatsuba saves hours of computing time.

4. REAL LIFE EXAMPLE:
   Think of **COOKING A MASSIVE FEAST**. 
   If you have to cook 4 different dishes, it takes 4 hours. 
   But if you find a recipe where 2 dishes share the same ingredients 
   and base, you might be able to finish everything in just 3 hours 
   by reusing your work!
================================================================================
"""

def fast_mul(x, y):
    """
    Karatsuba multiplication: Reduces 4 multiplications to 3.
    x, y: large integers to multiply
    """
    # 1. Base case: Single digits
    if x < 10 or y < 10:
        return x * y # multiply normally

    # 2. Get number of digits and find midpoint
    n = max(len(str(x)), len(str(y))) # n: total digits
    m = n // 2 # m: half digits (split point)

    # 3. Split numbers into High (h) and Low (l) parts
    # x = x_h * 10^m + x_l
    xh, xl = x // (10**m), x % (10**m) # xh: high x, xl: low x
    yh, yl = y // (10**m), y % (10**m) # yh: high y, yl: low y

    # 4. Recursive multiplications
    A = fast_mul(xh, yh) # A = high digits product
    B = fast_mul(xl, yl) # B = low digits product
    C = fast_mul(xh + xl, yh + yl) # C = combined digits product

    # 5. Combine using Karatsuba formula
    # result = A * 10^(2m) + (C - A - B) * 10^m + B
    return A * (10**(2*m)) + (C - A - B) * (10**m) + B

# ================================================================================
# VERSION 2: THE MOST COMPACT & SHORTEST WAY
# ================================================================================

def compact_mul(x, y):
    """
    Extremely short Karatsuba. x,y: numbers
    """
    if x < 10 or y < 10: return x * y
    m = max(len(str(x)), len(str(y))) // 2 # m: split
    h1, l1 = divmod(x, 10**m) # h: high, l: low
    h2, l2 = divmod(y, 10**m)
    z0, z2 = compact_mul(l1, l2), compact_mul(h1, h2) # z: subproblems
    z1 = compact_mul(h1 + l1, h2 + l2) - z0 - z2
    return z2 * 10**(2*m) + z1 * 10**m + z0

# --- START OF PROGRAM ---

# n1, n2: input numbers
n1, n2 = 3456, 8902

print("Welcome to the Karatsuba Fast Multiplier!")
print(f"Multiplying {n1} by {n2}...")

# Run fast multiplication
ans = fast_mul(n1, n2)

print(f"\nResult: {ans} ✅")
print(f"Check:  {n1 * n2}")
