# SCHEDULE YOUR DA(RRA)Y

# The best way to have a productive day is to plan out your work schedule. Given the following three inputs, please create an array of time alloted to work, broken up with time alloted with breaks:

# Input 1: Hours - Number of hours available to you to get your work done!
# Input 2: Tasks - How many tasks you have to do througout the day
# Input 3: Duration (minutes)- How long each of your tasks will take to complete

# Criteria to bear in mind:

# Your schedule should start with work and end with work.
# It should also be in minutes, rounded to the nearest whole minute.
# If your work is going to take more time than you have, return "You're not sleeping tonight!"
# Example:

# day_plan(8, 5, 30) == [ 30, 82, 30, 82, 30, 82, 30, 82, 30 ]
# day_plan(3, 5, 60) == "You're not sleeping tonight!"

def day_plan(hours, tasks, duration):
    total_work = tasks * duration
    total_available = hours * 60
    
    if total_work > total_available:
        return "You're not sleeping tonight!"
    
    if tasks <= 1:
        return [duration] * tasks if tasks > 0 else []
    
    break_duration = round((total_available - total_work) / (tasks - 1))
    
    schedule = []
    for i in range(tasks):
        schedule.append(duration)
        if i < tasks - 1:
            schedule.append(break_duration)
    
    return schedule