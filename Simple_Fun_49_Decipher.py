# Task
# Consider the following ciphering algorithm:

# For each character replace it with its code.
# Concatenate all of the obtained numbers.
# Given a ciphered string, return the initial one if it is known that it consists only of lowercase letters.

# Note: here the character's code means its decimal ASCII code, the numerical representation of a character used by most modern programming languages.

# Example
# For cipher = "10197115121", the output should be "easy".

# Explanation:

# charCode('e') = 101, 
# charCode('a') = 97, 
# charCode('s') = 115 
# charCode('y') = 121.
# Input/Output
# [input] string cipher

# A non-empty string which is guaranteed to be a cipher for some other string of lowercase letters.

# [output] a string


def decipher(cipher):
    result = ""
    i = 0
    
    while i < len(cipher):
        if cipher[i] == '1':
            code = int(cipher[i:i+3])
            i += 3
        else:
            code = int(cipher[i:i+2])
            i += 2
        
        result += chr(code)
    
    return result