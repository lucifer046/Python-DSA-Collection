"""
================================================================================
CONCEPTS AND THEORY: UNION-FIND (DISJOINT SET UNION)
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
    """
    A class to keep track of elements split into several non-overlapping sets.
    Think of it as a 'Team Manager' that knows which player is on which team.
    """
    def __init__(self):
        # 'set_leader' stores which team leader each person reports to
        self.set_leader = {}
        # 'team_members' stores a list of all people in each team leader's group
        self.team_members = {}
        # 'team_size' stores how many people are in each team leader's group
        self.team_size = {}
    
    def initialize_teams(self, all_players):
        """
        At the start, everyone is a team of ONE. They are their own leaders.
        """
        for player in all_players:
            # Each player is their own leader initially
            self.set_leader[player] = player
            # Each leader starts with just themselves as a member
            self.team_members[player] = [player]
            # Each team starts with a size of 1
            self.team_size[player] = 1
    
    def find_leader(self, player):
        """
        Returns the official 'leader' (representative) of the player's team.
        """
        return self.set_leader[player]
    
    def merge_teams(self, player_a, player_b):
        """
        Joins the team of player_a and the team of player_b together.
        """
        leader_a = self.find_leader(player_a)
        leader_b = self.find_leader(player_b)

        # Rule: If they are already on the same team (same leader), do nothing!
        if leader_a == leader_b:
            return 

        # We always merge the SMALLER team into the LARGER team to save time.
        # Check: Is team_a larger or equal to team_b?
        if self.team_size[leader_a] >= self.team_size[leader_b]:
            # Move everyone from Team B to Team A
            for member in self.team_members[leader_b]:
                # Update their leader to be Leader A
                self.set_leader[member] = leader_a
                # Add them to Leader A's member list
                self.team_members[leader_a].append(member)
            
            # Clear Team B's list since they all moved!
            self.team_members[leader_b] = []  
            # Update Team A's total size
            self.team_size[leader_a] += self.team_size[leader_b]  
            
        else:
            # Otherwise, move everyone from Team A to Team B
            for member in self.team_members[leader_a]:
                # Update their leader to be Leader B
                self.set_leader[member] = leader_b
                # Add them to Leader B's list
                self.team_members[leader_b].append(member)
            
            # Clear Team A's list
            self.team_members[leader_a] = []
            # Update Team B's total size
            self.team_size[leader_b] += self.team_size[leader_a]

# --- START OF PROGRAM ---

# Create our Team Manager
my_manager = UnionFind()

# Let's say we have 14 people (numbered 0 to 13)
all_people = list(range(14))

# Start everyone out in their own individual groups
my_manager.initialize_teams(all_people)

# Imagine these pairs of people become friends and join groups:
friendship_links = [
    (0,1), (0,2), (1,3), (2,3), (3,4), (4,5),
    (5,6), (6,7), (7,8), (8,9), (9,10),
    (10,11), (11,12), (12,13), (1,13)
]

# Process each friendship link to merge teams
for person_1, person_2 in friendship_links:
    my_manager.merge_teams(person_1, person_2)

# Show who the leaders are now
print("--- Final Group Leaders ---")
print(my_manager.set_leader)

# Show the members currently in each leader's group
print("\n--- Final Group Memberships ---")
print(my_manager.team_members)