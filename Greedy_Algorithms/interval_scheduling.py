"""
================================================================================
CONCEPTS AND THEORY: INTERVAL SCHEDULING (GREEDY ALGORITHM)
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

def schedule_intervals(meeting_requests):
    """
    Imagine you have a single room and several friends want to use it for meetings.
    Each meeting has a START time and an END time.
    Your goal is to fit as many meetings as possible in that one room without overlapping!
    """

    # 1. First, we sort the meetings by their END times.
    # Logic: The sooner a meeting finishes, the sooner the room is free for the next one!
    # 'meeting_info[1]' refers to the index 1 (the end time) of each meeting.
    meeting_requests.sort(key=lambda meeting_info: meeting_info[1])

    # This 'scheduled_list' will keep track of the meetings we pick
    scheduled_list = []
    
    # This 'last_finish_time' tracks when the room becomes empty after the last meeting we chose
    # We start it at 0 (assuming meetings start at or after 0)
    last_finish_time = 0

    # 2. Now we check every single meeting one by one
    for current_meeting in meeting_requests:
        start_time = current_meeting[0]  # When this meeting wants to START
        end_time = current_meeting[1]    # When this meeting wants to END

        # 3. Rule: If the new meeting starts AFTER or EXACTLY when the last one finished...
        if start_time >= last_finish_time:
            # ...then we can FIT it!
            scheduled_list.append(current_meeting)
            # Update our tracker to show when the room will be free next
            last_finish_time = end_time

    # Finally, we return the list of meetings we managed to fit in for our room
    return scheduled_list

# --- Let's Try Running It! ---

# Imagine these are your friends' meeting requests:
# Each bracket [start, end] is a meeting.
all_requests = [
    [1, 4],   # Meeting A: Starts at 1, ends at 4
    [3, 5],   # Meeting B: Starts at 3, ends at 5 (Ouch! This overlaps with A)
    [0, 6],   # Meeting C: Starts at 0, ends at 6 (Very long meeting!)
    [5, 7],   # Meeting D: Starts at 5, ends at 7
    [3, 8],   # Meeting E: Starts at 3, ends at 8
    [5, 9],   # Meeting F: Starts at 5, ends at 9
    [6, 10],  # Meeting G: Starts at 6, ends at 10
    [8, 11]   # Meeting H: Starts at 8, ends at 11
]

print("Welcome to the Meeting Scheduler!")
print("Here are all the requests:")
print(all_requests)

# We call our function 'schedule_intervals' with our list of requests
optimized_schedule = schedule_intervals(all_requests)

print("\n--- Optimized Schedule (Total:", len(optimized_schedule), "meetings) ---")
# Let's show the meetings we picked!
for chosen_meeting in optimized_schedule:
    print(f"Meeting from {chosen_meeting[0]} to {chosen_meeting[1]}")