# Multiply the adjacent digits which are not separated by a '-' or a '+' in a string, then do the sum.

# Examples
# "53+5"    -->   20  # = 5 * 3 + 5
# "266-66"  -->   36  # = 2 * 6 * 6 - 6 * 6
# "555"     -->  125  # = 5 * 5 * 5

def digit_multiplication(expression):
    result = 0
    sign = 1
    product = 1
    in_number = False
    
    for char in expression:
        if char.isdigit():
            product *= int(char)
            in_number = True
        else:  # '+' or '-'
            if in_number:
                result += sign * product
            sign = 1 if char == '+' else -1
            product = 1
            in_number = False
    
    if in_number:
        result += sign * product
    
    return result