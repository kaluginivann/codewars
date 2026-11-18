# Create a function which compares two probabilities, returning true if the first one is most likely otherwise false.

# For this exercise probability is expressed as two numbers separated by a colon e.g. a probability of 1 in 3 will be 1:3.

# So:

# Input: ('1:3','1:2') - returns false as 1 in 3 is less likely than 1 in 2.

from fractions import Fraction

def most_likely(prob1: str, prob2: str) -> bool:
    def to_fraction(p: str) -> Fraction:
        num, denom = p.split(':')
        return Fraction(int(num), int(num) + int(denom))
    
    return to_fraction(prob1) > to_fraction(prob2)