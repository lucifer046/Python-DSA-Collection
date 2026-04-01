"""
================================================================================
CONCEPTS AND THEORY: MINIMIZING MAXIMUM LATENESS (GREEDY ALGORITHM)
================================================================================

--- TIME COMPLEXITY ANALYSIS ---
- BEST CASE:    O(n log n) (Sorting the tasks by their deadlines takes most time)
- AVERAGE CASE: O(n log n) 
- WORST CASE:   O(n log n) 
--------------------------------
- SPACE COMPLEXITY: O(n) (To store the final sorted schedule and job results)

STATUS: INDEPENDENT (Contains a single complete implementation)
================================================================================

1. THE PROBLEM:
   You have a list of tasks. Each task has:
   - A DURATION (how long it takes to finish).
   - A DEADLINE (the time it SHOULD be finished by).

   If a task is finished AFTER its deadline, it is 'LATE'. 
   Your goal is to organize the tasks so that the MOST late any task gets 
   is kept as small as possible. This is called 'Minimizing Maximum Lateness'.

2. THE GREEDY STRATEGY (EARLIEST DEADLINE FIRST):
   The secret to solving this is to always pick the task whose DEADLINE is 
   coming up soonest. This is like how you might do your homework: tackle 
   the project that is due tomorrow before the one due next week!

3. THE THEOREM (WHY IT WORKS):
   A famous rule in scheduling theory says that organizing tasks by their 
   DEADLINE (Earliest Deadline First) is the best way to keep the maximum 
   lateness as low as possible. 

4. COMPARISON WITH OTHER IDEAS:
   - Doing the shortest task first? (Doesn't work if a long task has an urgent deadline).
   - Doing the task with the smallest "slack time" (deadline - duration)? (Surprisingly, this is also NOT as good as deadlines!)

5. TIME COMPLEXITY:
   Like Interval Scheduling, this takes O(n log n) time because the main
   work is just sorting the tasks by their deadlines once.
   
6. REAL LIFE EXAMPLE:
   Think of a **Busy Baker** with 5 Wedding Cake orders. Each cake takes 
   time to decorate and has a strict delivery time. Even if some cakes 
   will definitely be a bit late, the baker organizes them so that the 
   most delayed bride is only late by minutes, not hours!
================================================================================
"""

def schedule(jobs):
    """
    Minimizes max lateness by sorting jobs by deadline.
    jobs: list of (id, duration, deadline)
    """
    # 1. Strategy: Sort all jobs by their DEADLINE (3rd item, index 2).
    # Logic: Earliest Deadline First (EDF) minimizes the maximum delay.
    # j: job record (id, duration, deadline)
    jobs.sort(key=lambda j: j[2]) # j[2] is the deadline

    # 2. res: stores scheduled jobs as (id, start, finish)
    res = [] # res = result schedule
    
    # 3. L_max: tracks the worst-case (maximum) lateness found in the schedule.
    # lateness is defined as (Finish Time - Deadline) if > 0.
    L_max = 0 # L_max = maximum lateness
    
    # 4. t: current time clock. Tracks when the worker completes a job.
    t = 0 # t = current time boundary

    # 5. Iterative scheduling loop
    for j in jobs: # j: job details tuple (id, dur, dline)
        jid, dur, dline = j # unpack: id, duration, deadline
        
        # 6. Calc: the job starts at current time t and ends after duration dur
        s, f = t, t + dur # s: start, f: finish
        
        # 7. Update system clock to the finish time of current job
        t = f 
        
        # 8. Check lateness for this specific job
        # if the job finishes AFTER its deadline, calculate by how much
        if f > dline:
            l = f - dline # l: current job lateness
            # update the global worst-case lateness value
            L_max = max(L_max, l)
            
        # 9. Record the job timings in final schedule list
        res.append((jid, s, f))
    
    # 10. Return the worst lateness found and the full sorted schedule
    return L_max, res

# --- START OF PROGRAM ---

# reqs: sample jobs (id, duration, deadline)
reqs = [
    (1, 3, 6), (2, 2, 9), (3, 1, 8), 
    (4, 4, 9), (5, 3, 14), (6, 2, 15)
]

print("Maximum Lateness Minimizer (Earliest Deadline First)!\n")

# Run the greedy scheduling algorithm
worst_lat, final_schedule = schedule(reqs[:]) # use slice to preserve list

# Display outcome
print(f"Worst-case lateness across all jobs: {worst_lat} hours ✅\n")

print("--- Optimized Timetable ---")
for task in final_schedule: # task: record (id, start, finish)
    tid, ts, tf = task # id, start, finish
    print(f" Job ID {tid}: Starts at hour {ts:2} | Finishes at hour {tf:2}")

print("\nWorkday Optimal Scheduling Complete! 🕒")
