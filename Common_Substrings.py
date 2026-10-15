# Given 2 strings, your job is to find out if there is a substring that appears in both strings. You will return true if you find a substring that appears in both strings, or false if you do not. We only care about substrings that are longer than one character. Substrings are case-insensitive, e.g. "aB" and "Ab" should compare equal in this kata.

# Examples:
# "Something", "Fun"  ==> false
# // because "something" and "fun" contain no common substrings
# // (We do not count the 'n' as a substring in this Kata,
# // because it is only 1 character long)

# "Something", "Home" ==> true
# // because both of the strings contain the substring `"me"`
# // (so**ME**thing and ho**ME**).

def substring_test(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()

    return any(s1[i:i + 2] in s2 for i in range(len(s1) - 1))