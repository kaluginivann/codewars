# Just as the title suggested :D

# For example ->

# n = 1   # --> Should return 7
# n = 2   # --> Should return 97
# ...
# Do not mind the pattern as it is just an incident!

# And make sure to return false if the input is not an integer :D

# This might seem simple at first, it is, but keep an eye on the performance.

# Go for it!

def largest(n):
    if not isinstance(n, int) or isinstance(n, bool):
        return False
    if n < 1:
        return False
    
    def is_prime(num):
        if num < 2:
            return False
        if num < 4:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        
        if num < 1373653:
            i = 5
            while i * i <= num:
                if num % i == 0 or num % (i + 2) == 0:
                    return False
                i += 6
            return True
        
        d = num - 1
        r = 0
        while d % 2 == 0:
            d //= 2
            r += 1
        
        for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
            if a >= num:
                continue
            x = pow(a, d, num)
            if x == 1 or x == num - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, num)
                if x == num - 1:
                    break
            else:
                return False
        return True
    
    candidate = 10**n - 1
    
    if candidate % 2 == 0:
        candidate -= 1
    
    lower_bound = 10**(n-1)
    
    while candidate >= lower_bound:
        if is_prime(candidate):
            return candidate
        candidate -= 2
    
    return False