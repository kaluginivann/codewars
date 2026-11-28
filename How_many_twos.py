# Write a function that returns the number of '
# 2
# 2's in the factorization of a number.
# For example,

# 24
# 24 should return 
# 3
# 3, since the factorization of 
# 24
# 24 is 
# 2
# 3
# ×
# 3
# 2 
# 3
#  ×3.
# 17280
# 17280 should return 
# 7
# 7, since the factorization of 
# 17280
# 17280 is 
# 2
# 7
# ×
# 5
# ×
# 3
# 3
# 2 
# 7
#  ×5×3 
# 3
#  .
# The number passed to your function will always be a positive integer greater than or equal to 
# 1
# 1.

def two_count(n):
    return (n & -n).bit_length() - 1