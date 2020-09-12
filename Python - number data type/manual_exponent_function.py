from functools import reduce

"""
manual_exponent(2, 3)
#> 8

manual_exponent(10, 2)
#> 100
"""

# Iterative Apporoach:
"""
def manual_exponent(num, exp):
    counter = exp - 1
    total = num

    while counter > 0:
        total *= num
        counter -= 1
    
    return total

print(manual_exponent(2, 3))
print(manual_exponent(10, 2))

"""

# Functional Approach:
def manual_exponent(num, exp):
    computed_list = [num] * exp                      # [2] * 3 => 2 * 2 * 2     & [10] * 2 => 10 * 10
    return(reduce(lambda total, element: total * element, computed_list))

print(manual_exponent(2, 3))
print(manual_exponent(10, 2))