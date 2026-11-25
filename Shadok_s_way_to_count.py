# In this kata you have to make a function shadok(n) that takes a positive or zero integer n and return it in "Shadok".

# You don't know what Shadoks are? I think not... You should. If you want to know more you can take a look on the Shadok's wikipedia. (you will like it for sure)

# For this kata you only need to know that they are counting.... in a really special way. Because of their brain that have four cells they only know the four syllables "GA", "BU", "ZO" and "MEU" (read : [mø]).

# Rules
# "GA" means 0 item.
# "BU" means 1 item.
# "ZO" means 2 items.
# "MEU" means 3 items.
# After that they repeat this by putting four items in a little bin. And they count these bins with the same syllables.
# When they have 4 four little bins they put them in a bigger little bins... And count them with same syllables...
# When they have four of these bigger little bins they put them in a normal bin... And repeating the same thing.
# And repeating this with always bigger bins. Yeah, it's a bit of pain.
# Like us they place the syllable of the bigger bin before the other. (ex: 10, 1 is equivalent to the syllable of the bigger bin but we say that it is the ten and not a "little bin").
# Examples
# shadok(7)     =>   "BUMEU"
# shadok(33)    =>   "ZOGABU" 
# shadok(356)   =>   "BUBUZOBUGA"
# Good luck, I hope that you will have fun with my first kata <3.

def shadok(n: int) -> str:
    syllables = ["GA", "BU", "ZO", "MEU"]
    
    if n == 0:
        return "GA"
    
    result = []
    while n > 0:
        result.append(syllables[n % 4])
        n //= 4
    
    return "".join(reversed(result))