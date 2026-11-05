# This is the simple version of Shortest Code series. If you need some challenges, please try the challenge version

# Task:
# Every uppercase letter is a father, the corresponding lowercase letters are its sons.

# Given a string:

# if father and son both exist, keep them both
# if one exists but not the other, delete them
# one father can have multiple sons. keep it if it has at least one.
# one son can have multiple fathers. keep it if it has at least one.
# return the filtered string.
# Examples (input --> output)
# "Aab" --> "Aa"
# "AabBc" -->  "AabB"
# "AaaaAaab" --> "AaaaAaa"
# "aAAAaAAb" --> "aAAAaAA"


def sc(s: str) -> str:
    chars = set(s)
    result = []
    for c in s:
        pair = c.lower() if c.isupper() else c.upper()
        if pair in chars:
            result.append(c)
    return ''.join(result)