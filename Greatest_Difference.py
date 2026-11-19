# Task: Find the number couple with the greatest difference from a list of number-couples.

# Input: A list of number-couples, where each couple is represented as a string containing two positive integers separated by a hyphen ("-").

# Output: The number couple with the greatest difference, or False if there is no difference among any of the couples or in case of an empty list.

# Additional Information:

# All number couples will be given as strings.
# All numbers in the couples are positive integers.
# If multiple couples have the same greatest difference, return the first one encountered in the input list.
# If there is no difference (both numbers in a couple are equal), return False.

def diff(arr):
    if not arr:
        return False
    
    max_diff = -1
    result = False
    
    for couple in arr:
        a, b = map(int, couple.split('-'))
        d = abs(a - b)
        if d > max_diff:
            max_diff = d
            result = couple
    
    return result if max_diff > 0 else False