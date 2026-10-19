# Statistics puzzle
# Your function will receive an array of 10000 integer values randomly selected from a uniform distribution (a range of values with equal selection probability). Your function will also receive the minimum and maximum possible values in the range (inclusive). A constant has been added to every value in the array, after it was randomly selected. You must find the constant.

# There are no example tests in this kata, so as not to spoil the trick.
# Do not worry *too* much about precision. The tests are lenient.

def find_constant(arr, lb, ub):
    c_from_min = min(arr) - lb
    c_from_max = max(arr) - ub
    return (c_from_min + c_from_max) / 2