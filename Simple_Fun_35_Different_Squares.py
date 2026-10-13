# Task
# Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.

# Example
# For

# matrix = [[1, 2, 1],
#           [2, 2, 2],
#           [2, 2, 2],
#           [1, 2, 3],
#           [2, 2, 1]]
# the output should be 6.

# Here are all 6 different 2 × 2 squares:

# 1 2
# 2 2

# 2 1
# 2 2

# 2 2
# 2 2

# 2 2
# 1 2

# 2 2
# 2 3

# 2 3
# 2 1
# Input/Output
# [input] 2D integer array matrix

# Constraints:

# 1 ≤ matrix.length ≤ 100,

# 1 ≤ matrix[i].length ≤ 100,

# 0 ≤ matrix[i][j] ≤ 9.

# [output] an integer

# The number of different 2 × 2 squares in matrix.

def different_squares(matrix):
    if len(matrix) < 2 or len(matrix[0]) < 2:
        return 0
    
    unique_squares = set()
    
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) - 1):
            square = (
                matrix[i][j], matrix[i][j+1],
                matrix[i+1][j], matrix[i+1][j+1]
            )
            unique_squares.add(square)
    
    return len(unique_squares)