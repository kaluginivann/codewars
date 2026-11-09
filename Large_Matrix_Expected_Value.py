# Problem Statement:

# You are given a matrix 
# M
# M that is defined as follows:

# M
# =
# [
# 0
# −
# 1
# −
# 2
# ⋯
# −
# c
# 1
# 0
# −
# 1
# ⋯
# −
# (
# c
# −
# 1
# )
# 2
# 1
# 0
# ⋯
# −
# (
# c
# −
# 2
# )
# ⋱
# r
# r
# −
# 1
# r
# −
# 2
# ⋯
# r
# −
# c
# ]
# M= 
# ⎣
# ⎡
# ​
  
# 0
# 1
# 2
# ⋮
# r
# ​
  
# −1
# 0
# 1
# ⋮
# r−1
# ​
  
# −2
# −1
# 0
# ⋮
# r−2
# ​
  
# ⋯
# ⋯
# ⋯
# ⋱
# ⋯
# ​
  
# −c
# −(c−1)
# −(c−2)
# ⋮
# r−c
# ​
  
# ⎦
# ⎤
# ​
 
# The dimensions of the matrix are 
# (
# r
# +
# 1
# )
# ×
# (
# c
# +
# 1
# )
# (r+1)×(c+1) where 
# 0
# ≤
# r
# ,
# c
# ≤
# 1
# 0
# 18
# 0≤r,c≤10 
# 18
#  .

# Your task is to calculate the expected value of a random element from this matrix.

# Input:

# Two integers 
# r
# r and 
# c
# c representing the number of rows and columns of the matrix, respectively.
# Output:

# An integer representing the expected value of a random element from the matrix rounded down.
# Example:

# Input:

# 11 5
# Output:

# 3
# Explanation:

# The matrix 
# M
# M is:

# M
# =
# [
# 0
# −
# 1
# −
# 2
# −
# 3
# −
# 4
# −
# 5
# 1
# 0
# −
# 1
# −
# 2
# −
# 3
# −
# 4
# 2
# 1
# 0
# −
# 1
# −
# 2
# −
# 3
# 3
# 2
# 1
# 0
# −
# 1
# −
# 2
# 4
# 3
# 2
# 1
# 0
# −
# 1
# 5
# 4
# 3
# 2
# 1
# 0
# 6
# 5
# 4
# 3
# 2
# 1
# 7
# 6
# 5
# 4
# 3
# 2
# 8
# 7
# 6
# 5
# 4
# 3
# 9
# 8
# 7
# 6
# 5
# 4
# 10
# 9
# 8
# 7
# 6
# 5
# 11
# 10
# 9
# 8
# 7
# 6
# ]
# M= 
# ⎣
# ⎡
# ​
  
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# ​
  
# −1
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# ​
  
# −2
# −1
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# ​
  
# −3
# −2
# −1
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# ​
  
# −4
# −3
# −2
# −1
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# ​
  
# −5
# −4
# −3
# −2
# −1
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# ​
  
# ⎦
# ⎤
# ​
 
# Now, let's calculate the sum and the expected value:

# Summing the Elements:

# Add up all the elements within the matrix to find the total sum. In this case we get 
# 216
# 216.
# Number of Elements:

# With 12 rows and 6 columns, the matrix contains 
# 12
# ×
# 6
# =
# 72
# 12×6=72 elements.
# Expected Value:

# The expected value is then calculated as the total sum divided by the number of elements:
# E
# =
# 216
# 72
# =
# 3
# E= 
# 72
# 216
# ​
#  =3
# Thus, the expected value of a random element from the matrix is 3.

# Constraints:

# 0
# ≤
# r
# ,
# c
# ≤
# 1
# 0
# 18
# 0≤r,c≤10 
# 18
 
# Instructions:

# Implement a function expected_value(r: int, c: int) -> int that returns the expected value of a random element in the matrix.
# Consider the large constraints when designing your solution.
# Note:

# The expected value 
# E
# E of a matrix element is calculated by summing all elements in the matrix and then dividing by the number of elements.



def expected_value(r: int, c: int) -> int:
    return (r - c) // 2