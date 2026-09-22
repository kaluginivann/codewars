# Implement a function which takes a string, and returns its hash value.

# Algorithm steps:

# a := sum of the ascii values of the input characters
# b := sum of every difference between the consecutive characters of the input (second char minus first char, third minus second, ...)
# c := (a OR b) AND ((NOT a) shift left by 2 bits)
# d := c XOR (32 * (total_number_of_spaces + 1))
# return d
# Note: OR, AND, NOT, XOR are bitwise operations.

# Examples
# input = "a"
# a = 97
# b = 0
# result = 64

# input = "ca"
# a = 196
# b = -2
# result = -820
# Give an example why this hashing algorithm is bad?

def string_hash(s):
    a = sum(ord(c) for c in s)
    
    b = 0
    for i in range(1, len(s)):
        b += ord(s[i]) - ord(s[i-1])
    
    c = (a | b) & ((~a) << 2)
    
    num_spaces = s.count(' ')
    d = c ^ (32 * (num_spaces + 1))
    
    return d