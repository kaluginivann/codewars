# Take debugging to a whole new level:

# Given a string, remove every single bug.

# This means you must remove all instances of the word 'bug' from within a given string, unless the word is plural ('bugs').

# For example, given 'obugobugobuoobugsoo', you should return 'ooobuoobugsoo'.

# Another example: given 'obbugugo', you should return 'obugo'.

# Note that all characters will be lowercase.

# Happy squishing!

def debug(s):
    result = []
    i = 0
    while i < len(s):
        if s[i:i+3] == "bug":
            if s[i+3:i+4] == 's':
                result.append("bug")
                i += 3
            else:
                i += 3
        else:
            result.append(s[i])
            i += 1
    return ''.join(result)