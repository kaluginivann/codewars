# Split & Add
# A sequence satisfies the recurrence relation

# a
# m
# +
# n
# =
# a
# m
# +
# a
# n
# +
# y
# ∗
# m
# ∗
# n
# a 
# m+n
# ​
#  =a 
# m
# ​
#  +a 
# n
# ​
#  +y∗m∗n
# for all non-negative integers 
# m
# m and 
# n
# n, where 
# y
# y is a fixed non-negative integer.

# Given: 
# a
# 1
# =
# 1
# a 
# 1
# ​
#  =1, regardless of the value of 
# y
# y

# Write a function that returns the value of 
# a
# x
# a 
# x
# ​
#   for given 
# x
# ,
# y
# x,y.

# Constraints
# 0 ≤ x ≤ 10^8
# 0 ≤ y ≤ 10^4

def solve_sequence(x, y):
    return x + y * x * (x - 1) // 2