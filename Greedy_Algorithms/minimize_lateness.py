"""
================================================================================
CONCEPTS AND THEORY: MINIMIZING MAXIMUM LATENESS (GREEDY ALGORITHM)
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

from operator import itemgetter
    
def calculate_minimum_lateness_schedule(list_of_jobs):
    """
    This function takes a list of jobs and arranges them in a way that
    nobody is 'too late' compared to everyone else.
    """
    # This list will store the result: (Job ID, Start Time, End Time)
    final_schedule = []
    
    # We will track the biggest 'lateness' value we find
    maximum_lateness_found = 0
    
    # 'current_time' tracks when the single worker is free to start the next job
    current_time = 0
        
    # 1. First, we sort the jobs by their DEADLINE (the 3rd item in our tuple, index 2)
    # This is our 'Earliest Deadline First' strategy!
    jobs_sorted_by_deadline = sorted(list_of_jobs, key=itemgetter(2))
        
    # 2. Now we process each job one by one in the sorted order
    for job_details in jobs_sorted_by_deadline:
        # Variables for better readability:
        job_id = job_details[0]           # The unique ID of the job
        job_duration = job_details[1]     # How long the job takes
        job_deadline = job_details[2]     # When it SHOULD be done

        # The job starts as soon as we finish the previous one
        job_start_time = current_time
        # It finishes after its duration is added to the start time
        job_finish_time = current_time + job_duration
    
        # Update our tracker: The worker is now busy until this finish time
        current_time = job_finish_time
        
        # 3. Check if the job is late: 
        # Lateness = (Finish Time - Deadline). If it's done before deadline, lateness is 0.
        if job_finish_time > job_deadline:
            lateness_for_this_job = job_finish_time - job_deadline
            # We only remember the BIGGEST lateness value we've seen so far
            maximum_lateness_found = max(maximum_lateness_found, lateness_for_this_job)
            
        # Add the job's timing to our final schedule list
        final_schedule.append((job_id, job_start_time, job_finish_time))
    
    # Return both the maximum lateness found and the full schedule
    return maximum_lateness_found, final_schedule
    
# --- Let's Try Running It! ---

# Imagine these are 6 jobs you have to complete:
# Format: (Job ID, Duration, Deadline)
job_requests = [
    (1, 3, 6),   # Job 1: Takes 3 hours, due at hour 6
    (2, 2, 9),   # Job 2: Takes 2 hours, due at hour 9
    (3, 1, 8),   # Job 3: Takes 1 hour,  due at hour 8
    (4, 4, 9),   # Job 4: Takes 4 hours, due at hour 9
    (5, 3, 14),  # Job 5: Takes 3 hours, due at hour 14
    (6, 2, 15)   # Job 6: Takes 2 hours, due at hour 15
]

# We run our function to get the best organization
max_lat, schedule_output = calculate_minimum_lateness_schedule(job_requests)

print("Welcome to the Lateness Minimizer!")
print(f"Maximum lateness across all jobs is: {max_lat} hours\n")

print("--- Optimized Work Schedule ---")
for job_record in schedule_output:
    # Unpack the tuple: (ID, Start, Finish)
    task_id, start, finish = job_record
    print(f"Job ID: {task_id} | Starts at: {start:2} | Finishes at: {finish:2}")
