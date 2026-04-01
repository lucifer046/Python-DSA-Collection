"""
================================================================================
CONCEPTS AND THEORY: CLOSEST PAIR OF POINTS (THE 'COLLISION DETECTOR')
================================================================================

--- TIME COMPLEXITY ANALYSIS ---
- BEST CASE:    O(n log n) (Pre-sorting is always done)
- AVERAGE CASE: O(n log n)
- WORST CASE:   O(n log n)
--------------------------------
- SPACE COMPLEXITY: O(n) (For storing sorted copies)
================================================================================

1. WHAT IS THE PROBLEM?
   Given a set of dots on a 2D map, find the two dots that are the 
   minimum distance apart. 
   Checking every possible pair is SLOW (O(n^2)). We want to do it fast!

2. THE DIVIDE AND CONQUER STRATEGY (O(n log n)):
   - 1. SORT the points by their X-coordinates first.
   - 2. SPLIT the map in half with a vertical line.
   - 3. RECURSE: Find the closest pair in the Left half and the Right half.
   - 4. DEFINE 'delta' as the smallest distance found so far.
   - 5. THE STRIP: Someone on the left might be very close to someone on 
        the right. We only need to check points within a distance of 
        'delta' from our vertical split line.

3. THE '7-POINT' RULE:
   In the central strip, if we sort the points by their Y-coordinates, 
   the math proves we only need to compare each point with the next 7 to 15 
   points. This keeps the combination step very fast!

4. WHY IS IT USEFUL?
   - **Air Traffic Control**: Detecting which two planes are currently 
     the closest to each other to avoid a crash.
   - **Computer Graphics**: Detecting if a bullet hit a target in a 
     3D video game.
   - **Epidemiology**: Finding the two closest outbreaks in a city 
     to trace the spread.

5. REAL LIFE EXAMPLE:
   Think of **GPS NAVIGATION IN A CROWDED CITY**. 
   You want to find the two nearest "Electric Vehicle Charging Stations" 
   in all of Mumbai. Instead of calculating the distance between *every* 
   possible pair of chargers, the computer divides the city into zones 
   and only checks the borders where two zones touch!
================================================================================
"""

import math

def dist(p1, p2): # p1, p2: coordinate points (x, y)
    """ Calculate Euclidean distance between two points p1 and p2. """
    # Returns the square root of the sum of squared differences
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def solve(px, py):
    """
    Recursively finds the minimum distance between points.
    px: points sorted by X, py: points sorted by Y
    """
    n = len(px) # n: number of points
    
    # 1. Base case: If 3 or fewer points, check all pairs (brute force)
    if n <= 3:
        d = float('inf') # d: minimum distance
        for i in range(n): # i: index of first point
            for j in range(i + 1, n): # j: index of second point
                d = min(d, dist(px[i], px[j]))
        return d

    # 2. Split: Divide the map into two halves using the median point
    m = n // 2 # m: midpoint index
    mid_x = px[m][0] # mid_x: x-coordinate of split line
    
    # 3. Create Y-sorted lists for each half efficiently
    ly = [p for p in py if p[0] < mid_x] # ly: Y-sorted points on left
    ry = [p for p in py if p[0] >= mid_x] # ry: Y-sorted points on right

    # 4. Recurse: Solve for each half independently
    dL = solve(px[:m], ly) # dL: min distance in left half
    dR = solve(px[m:], ry) # dR: min distance in right half
    d = min(dL, dR) # d: min distance between both halves

    # 5. Strip: Check for points that might cross the split line
    # Only points within 'd' distance of the split line are relevant
    s = [p for p in py if abs(p[0] - mid_x) < d] # s: candidates in the strip
    
    # 6. Optimized loop: Compare current strip point with next 7 neighbours
    # Since they are Y-sorted, a point can only have a few neighbours within distance 'd'
    for i in range(len(s)): # i: current point index in strip
        for j in range(i + 1, min(i + 8, len(s))): # j: neighbour index
            d = min(d, dist(s[i], s[j]))
                
    # 7. Return the absolute minimum distance found
    return d

def find_closest(pts):
    """
    Starter function that pre-sorts points and calls the solver.
    pts: list of input (x, y) coordinates
    """
    if len(pts) < 2: return 0.0 # Not enough points to measure
    
    # Pre-sort for the O(n log n) algorithm
    px = sorted(pts) # px: input points sorted by X
    py = sorted(pts, key=lambda p: p[1]) # py: input points sorted by Y
    
    # Execute solver and round the result
    return round(solve(px, py), 2)

# ================================================================================
# VERSION 2: THE MOST COMPACT & SHORTEST WAY
# ================================================================================

def compact_solve(pts):
    """
    Self-contained lightning-fast version of Closest Pair problem.
    pts: list of points
    """
    # d_fn: distance lambda function
    d_fn = lambda a, b: math.hypot(a[0]-b[0], a[1]-b[1])
    
    def engine(px, py):
        n = len(px) # n: point count
        if n <= 3: return min(d_fn(px[i], px[j]) for i in range(n) for j in range(i+1, n))
        m = n // 2 # m: mid
        mid_x = px[m][0] # mid_x: x-boundary
        ly, ry = [p for p in py if p[0] < mid_x], [p for p in py if p[0] >= mid_x]
        d = min(engine(px[:m], ly), engine(px[m:], ry))
        s = [p for p in py if abs(p[0] - mid_x) < d] # s: strip
        for i in range(len(s)):
            for j in range(i+1, min(i+8, len(s))): d = min(d, d_fn(s[i], s[j]))
        return d

    # Run engine with sorted coordinates
    px = sorted(pts) # px: X-sorted
    py = sorted(pts, key=lambda x: x[1]) # py: Y-sorted
    return round(engine(px, py), 2)

# --- START OF PROGRAM ---

# L: input coordinates list
L = [(2, 15), (40, 5), (20, 1), (21, 14), (1, 4), (3, 11)]

print("Welcome to the Closest Pair of Points Solver!")
print(f"Points: {L}")

# Run the long version
ans1 = find_closest(L)
print(f"\nMin distance (Long version): {ans1} ✅")

# Run the short version
ans2 = compact_solve(L)
print(f"Min distance (Short version): {ans2} ✅")
