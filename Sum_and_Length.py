# Sum and Length
# In this kata you must return a string value, where the first part is the sum of positive numbers and the second part is the number of negative numbers.

# Knowing that the first 0 is negative, the second is positive, the third is negative, and so on...

# Examples
# [-1,2,3,4,0,1,0,-2,0,-3]

# ==> '10 5'

# sum of positives: 10 = 2 + 3 + 4 + 0 (second) + 1
# count of negatives: 5 ( -1, 0 (first), -2, 0 (third), -3 )

def sum_length(arr: list[int]) -> str:
    total_sum = sum(x for x in arr if x > 0)
    neg_count = sum(1 for x in arr if x < 0)
    
    zero_counter = 0
    for num in arr:
        if num == 0:
            if zero_counter % 2 == 0:
                neg_count += 1
            zero_counter += 1
    
    return f'{total_sum} {neg_count}'