# Given an integer, if the length of it's digits is a perfect square, return a square block of sqroot(length) * sqroot(length). If not, simply return "Not a perfect square!".

# Examples:

# 1212 returns:

# "12
# 12"
# Note: 4 digits so 2 squared (2x2 perfect square). 2 digits on each line.

# 123123123 returns:

# "123
# 123
# 123"
# Note: 9 digits so 3 squared (3x3 perfect square). 3 digits on each line.


def square_it(digits):
    s = str(digits)
    r = int(len(s) ** 0.5)
    return '\n'.join(s[i:i+r] for i in range(0, len(s), r)) if r * r == len(s) else 'Not a perfect square!'