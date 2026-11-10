# Write a function that takes a list of lists of integers and returns the sum of all distinct numbers that appear in two or more of the inner list.

# Examples
# [[1, 2, 3], [2, 8, 9], [7, 123, 8]]
# # sum of [2, 8]
# return 10

# [[1], [2], [3, 4, 4, 4], [123456789]]
# # sum of []
# return 0

# [[1, 8, 8], [8, 8, 8], [8, 8, 8, 1]]
# # sum of [1,8]
# return 9


def repeat_sum(l):
    counts = {}
    for sublist in l:
        for num in set(sublist):
            counts[num] = counts.get(num, 0) + 1
    
    return sum(num for num, count in counts.items() if count >= 2)