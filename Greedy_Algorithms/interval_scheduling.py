"""
================================================================================
CONCEPTS AND THEORY: INTERVAL SCHEDULING (GREEDY ALGORITHM)
================================================================================

--- TIME COMPLEXITY ANALYSIS ---
- BEST CASE:    O(n log n) (Due to sorting the intervals by end-time)
- AVERAGE CASE: O(n log n) 
- WORST CASE:   O(n log n) 
--------------------------------
- SPACE COMPLEXITY: O(n) (To store the final scheduled list of intervals)

STATUS: INDEPENDENT (Contains a single complete implementation)
================================================================================

1. THE PROBLEM:
   You have a list of tasks (intervals), each with a Start time and an End time.
   You want to pick as many tasks as possible without any of them overlapping.

2. THE GREEDY STRATEGY:
   A 'Greedy Algorithm' is a problem-solving approach where you make the 
   BEST POSSIBLE choice at the current moment, hoping it leads to the best result overall.

3. THE OPTIMAL CHOICE (THE THEOREM):
   There are many ways to pick tasks, but the mathematical proof says:
   "To get the MAXIMUM number of tasks, ALWAYS pick the one that finishes EARLIEST."
   
   Why? Because the sooner a task is finished, the MORE ROOM you have left
   on your timeline for the next potential task!

4. OTHER IDEAS (And why they fail):
   - Pick the shortest task? (Fails if it overlaps with two longer ones).
   - Pick the one that starts earliest? (Fails if it's very long).
   - Pick the one with the fewest overlaps? (Usually good, but harder to code).

5. TIME COMPLEXITY:
   This algorithm is extremely fast. It takes O(n log n) time because 
   we only need to sort the tasks once and then check them in a single pass.
   
6. REAL LIFE EXAMPLE:
   Think of a **Busy Hospital Consultant**. Many patients want an 
   appointment, but the consultant can only see one at a time. By always 
   taking the appointment that **ends earliest**, the consultant can help 
   the maximum number of patients in their 8-hour shift!
================================================================================
"""

def schedule(intervals):
    """
    Selects the maximum number of non-overlapping intervals.
    intervals: list of [start, end] pairs
    """
    # 1. Logic: Sort the meetings by their END times primarily.
    # The sooner a meeting finishes, the more room remains for future tasks.
    # i: interval iterator [start, end]
    intervals.sort(key=lambda i: i[1]) # i[1] is the end_time

    # 2. res: list to store the final successfully scheduled intervals
    res = [] # res = result list
    
    # 3. f_time: tracks when the room becomes available after the last meeting.
    # initialized to 0 (assuming meetings occur after time 0)
    f_time = 0 # f_time = current finish time boundary

    # 4. Greedy Selection loop
    for i in intervals: # i: current meeting request
        # 5. Rule: can we FIT this meeting if it starts after the room is free?
        # i[0]: start_time of current meeting
        if i[0] >= f_time:
            # 6. Yes! Add to schedule and update the boundary to its end_time
            res.append(i) # add i to result
            f_time = i[1] # set new boundary to current meeting end_time

    # 7. Return the final collection of maximum possible meetings
    return res

# --- START OF PROGRAM ---

# reqs: sample meeting requests [start, end]
reqs = [
    [1, 4], [3, 5], [0, 6], [5, 7], 
    [3, 8], [5, 9], [6, 10], [8, 11]
]

print("Welcome to the Greedy Interval Scheduler!\n")

# Run the scheduling algorithm
final_list = schedule(reqs)

# Display results
print(f"Total meetings scheduled: {len(final_list)} ✅")
for m in final_list: # m: meeting record
    print(f" -> Meeting scheduled from {m[0]} to {m[1]}")
    
print("\nSchedule Optimization Complete! ")