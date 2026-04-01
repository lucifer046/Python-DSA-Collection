"""
================================================================================
CONCEPTS AND THEORY: UNION-FIND (DISJOINT SET UNION)
================================================================================

--- TIME COMPLEXITY ANALYSIS ---
- FIND (Leader):  O(1) (In this implementation, it's an instant lookup)
- UNION (Merge): O(n) (We iterate to move members from the smaller team to the larger)
- AVERAGE CASE:  O(n) (For this specific member-moving version)
--------------------------------
- SPACE COMPLEXITY: O(n) (We store a leader for every single person)

STATUS: INDEPENDENT (Self-contained 'UnionFind' class)
================================================================================

1. WHAT IS IT?
   Imagine a room of people who are strangers. As they talk, they form groups. 
   Union-Find is a tool that helps us answer two questions:
   - "Do these two people belong to the same group?" (FIND)
   - "Can we merge these two groups into one big group?" (UNION)

2. THE TWO MAIN OPERATIONS:
   - FIND: Look up who the 'leader' of a person's group is. If two people 
           have the same leader, they are in the same group.
   - UNION: Take two people from different groups and join their groups 
            together under one single leader.

3. OPTIMIZATION - UNION BY RANK:
   When merging two groups, we always make the 'smaller' group join the 
   'larger' one. This keeps the group structure 'flat' and fast to search.

4. WHY DO WE USE IT?
   - To detect cycles in a network (like a computer network or a city road map).
   - In Kruskal's Algorithm to find the Minimum Spanning Tree.
   - To solve connectivity problems (like "Can I get from city A to city B?").

5. TIME COMPLEXITY:
   Union-Find operations are almost INSTANT (nearly O(1) time) when using 
   smart tricks like Union-by-Rank.
   
6. REAL LIFE EXAMPLE:
   Think of a **Company Merger**. If Google buys a smaller startup, 
   all the employees from that startup are now under the Google 
   leadership. Union-Find helps us instantly know: "Is this new engineer 
   on the Google team now?"
================================================================================
"""

class UnionFind:
    """ Keeps track of non-overlapping sets (teams). """
    def __init__(self):
        # p: parent/leader dictionary, m: group members list, s: group sizes
        self.p = {} # p[x] stores the leader of set containing x
        self.m = {} # m[L] stores list of all elements in set led by L
        self.s = {} # s[L] stores total count of members in set led by L
    
    def start(self, x_list):
        """ Initializes each element in x_list as its own set. """
        for x in x_list: # x: current element
            # 1. At start, everyone is their own leader
            self.p[x] = x # self-leader
            # 2. Each set initially contains only the element itself
            self.m[x] = [x] # list containing x
            # 3. Each set size is initially 1
            self.s[x] = 1 # size = 1
    
    def find(self, x):
        """ Returns the official leader of the set containing x. """
        # x: input element to search
        return self.p[x] # O(1) direct lookup
    
    def union(self, a, b):
        """ Merges the sets containing elements 'a' and 'b'. """
        # 1. Find the current leaders of both elements
        L1, L2 = self.find(a), self.find(b) # L: leader

        # 2. If they already share the same leader, they are already merged
        if L1 == L2: 
            return # nothing to do

        # 3. Always merge the smaller set into the larger one (Optimization)
        if self.s[L1] < self.s[L2]:
            # Swap so L1 is always the larger set
            L1, L2 = L2, L1 

        # 4. Move all members from set L2 into set L1
        for x in self.m[L2]: # x: member being moved
            self.p[x] = L1 # update x's leader to L1
            self.m[L1].append(x) # add x to L1's member list
        
        # 5. Clear L2's list and update L1's total size
        self.m[L2] = [] # L2 set is now gone
        self.s[L1] += self.s[L2] # combine sizes
        self.s[L2] = 0 # L2 size is now zero

# --- START OF PROGRAM ---

# UF: instance of UnionFind class
UF = UnionFind()

# P: list of players (0 to 9)
P = list(range(10))

# Initialize everyone in their own group
UF.start(P)

# Combine teams
links = [(0,1), (1,2), (3,4), (4,5), (0,5)]
for a, b in links:
    UF.union(a, b)

# Output results
print("Group leaders for each player:")
for x in P:
    print(f"Player {x} -> Leader {UF.find(x)}")

print("\nFinal Group Memberships:")
for L in UF.m:
    if len(UF.m[L]) > 0:
        print(f"Group {L}: {UF.m[L]}")