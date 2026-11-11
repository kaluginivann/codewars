# The Watchtower
# Task
# Each uppercase letter represents a watchtower.
# Each lowercase letter represents a civilian.
# A watchtower's vision radius corresponds to its 1-based alphabetical index (A = 1, B = 2, ..., Z = 26).
# Given a string containing only alphabetical characters, return the filtered string based on the following rules:

# Watchtowers: All watchtowers are always retained.
# Civilians: A civilian is retained if, and only if they fall within the vision radius of at least one watchtower.
# Output: Return a string formed by concatenating all retained characters in their original relative order.
# Examples
# "abAcd"        -->  "bAc"
# "abc"          -->  ""
# "Acd"          -->  "Ac"
# "xxxxxxxxxxA"  -->  "xA"
# "aZzZ"         -->  "aZzZ"
# "ABCDEF"       -->  "ABCDEF"
# "b"            -->  ""

def watchtower(s: str) -> str:
    n = len(s)
    covered = [False] * n
    
    for i, ch in enumerate(s):
        if ch.isupper():
            covered[i] = True
            radius = ord(ch) - ord('A') + 1
            lo = max(0, i - radius)
            hi = min(n, i + radius + 1)
            for j in range(lo, hi):
                covered[j] = True
    
    return ''.join(s[i] for i in range(n) if covered[i])