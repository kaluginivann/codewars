# Jack and Jill are twins. When they are 10 years of age, Jack leaves earth in his spaceship bound for Altair IV, some 17 light-years distant. Though not equipped with warp drive, Jack's ship is still capable of attaining near light speed. When he returns to Earth he finds that Jill has grown to adulthood while he, Jack, remains a young boy.

# Albert Einstein had predicted this strange quirk of time in his 1905 paper "On the Electrodynamics of Moving Bodies" aka The Theory of Special Relativity. It has been verified experimentally many times.

# Task
# Implement a function that has as its arguments: the twins' age at the time of Jack's departure; the distance in light-years to the destination star; and the speed of Jack's ship as a fraction of the speed of light. The function will return Jack's age and Jill's age at the time of Jack's return to Earth (within a 1% margin to compensate for floating point errors). The math is simple enough for 10-year-old Jack to understand. The aging factor of Jack is:

# α
# =
# 1
# −
# v
# 2
# /
# c
# 2
# α= 
# 1−v 
# 2
#  /c 
# 2
 
# ​
 

# Where 
# v
# v is the velocity and 
# c
# c is the speed of light. As the velocity in this kata is defined as a fraction of the speed of light, the factor is further simplified:

# α
# =
# 1
# −
# v
# 2
# α= 
# 1−v 
# 2
 
# ​
 

# So while the time passed on Earth for Jill is 
# t
# t, the time passed for Jack is 
# α
# ⋅
# t
# α⋅t

# Notes
# For the sake of simplicity we assume that Jack's periods of acceleration and deceleration are negligibly short (this is a huge simplification, but it doesn't invalidate the calculations)
# See wikipedia for more info, if you're interested
# Examples
# 20, 10, 0.4       ➞  65.8, 70   # Jack's age is 65.8, Jill's age is 70.0
# 20, 10, 0.8       ➞  35, 45     # Jack's age is 35.0, Jill's age is 45.0
# 10, 16.73, 0.999  ➞  11.5, 43.5 # Jack's age is 11.5, Jill's age is 43.5


import math

def twins(age, distance, velocity):
    earth_time = 2 * distance / velocity
    
    alpha = math.sqrt(1 - velocity**2)
    
    jack_time = alpha * earth_time
    
    jack_age = age + jack_time
    jill_age = age + earth_time
    
    return jack_age, jill_age