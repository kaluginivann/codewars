# Your task is to take a given range and return an array of the prime numbers in that range.

# You will write a function with the following parameters:

# start is the integer from which your range starts. (inclusive)

# end is the integer at which your range ends. (inclusive)

# If the range does not contain any prime numbers return an empty value in your language (for example null / None / nil).

# Examples:

# primes(5, 7)  # [5, 7]
# primes(8, 9)  # None
# primes(1, 10) # [2, 3, 5, 7]

def primes(start: int, end: int) -> list[int] | None:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    
    result = [n for n in range(start, end + 1) if is_prime(n)]
    return result if result else None